from django.db import models
from django.db.models.signals import post_save
from django.utils.safestring import mark_safe
import re
import pprint
# Create your models here.

def render_notes(str):
  if str.strip() == "":
    return ""
  str = str.replace('\r', '')
  paras = str.split('\n\n')
  out = []
  for p in paras:
    r = p.strip()
    r = re.sub(r'\{(.*?)\}', r'<span class="person">\1</span>', r)
    out.append('<p class="notes">' + r + '</p>')
  return mark_safe('\n'.join(out))


class Album(models.Model):
  name = models.CharField(max_length=255)
  release_date = models.DateField()
  cover = models.FileField(null=True, blank=True)
  notes = models.TextField(blank=True, default='')

  def rendered_notes(self):
    return render_notes(self.notes)

  def __str__(self):
    return self.name


class Person(models.Model):
  name = models.CharField(max_length=255)
  notes = models.TextField(blank=True, default='')

  def rendered_notes(self):
    return render_notes(self.notes)

  def __str__(self):
    return self.name


def slug_song(title):
  m = re.match(r'(\d+\. )?(.*)', title).group(2).lower()
  m = m.replace('&', 'and')
  m = m.replace('the ', ' ')

  return filter(lambda x: x.isalpha(), m)


class Song(models.Model):
  name = models.CharField(max_length=255)
  album = models.ForeignKey(Album, blank=True, default=None, null=True, db_index=True)
  notes = models.TextField(blank=True, default='')
  author = models.ForeignKey(Person, null=True, blank=True)
  slug = models.CharField(editable=False, max_length=255, default='')

  def rendered_notes(self):
    return render_notes(self.notes)

  def save(self, *args, **kwargs):
    self.name = re.match(r'(\d+\. )?(.*)', self.name).group(2)
    self.name = self.name.replace('&', 'and')

    self.slug = slug_song(self.name)
    super(Song, self).save(*args, **kwargs)

  def __str__(self):
    if self.author != None:
      return self.name + " / " + self.author.name
    else:
      return self.name

  class Meta:
    ordering = ('name',)


class Venue(models.Model):
  name = models.CharField(max_length=255)
  city = models.TextField(db_index=True)
  state = models.CharField(max_length=255, default='', db_index=True)
  notes = models.TextField(blank=True, default='')

  def rendered_notes(self):
    return render_notes(self.notes)

  def __str__(self):
    return self.name + " (" + self.city + ", " + self.state + ")"

  class Meta:
    ordering = ('name', 'state')


class MasterTour(models.Model):
  name = models.CharField(max_length=120)

  def __str__(self):
    return self.name


class Tour(models.Model):
  name = models.CharField(max_length=120)
  start_date = models.DateField(default='2050-01-01', editable=False)
  notes = models.TextField(blank=True, default='')
  master_tour = models.ForeignKey(MasterTour, null=True, db_index=True)

  def rendered_notes(self):
    return render_notes(self.notes)

  def __str__(self):
    try:
      return self.master_tour.name + ' - ' + self.name
    except:
      return self.name


class Show(models.Model):
  venue = models.ForeignKey(Venue, db_index=True)
  tour = models.ForeignKey(Tour, db_index=True)
  date = models.DateField(db_index=True)
  setlist = models.TextField(blank=True, default='')
  notes = models.TextField(blank=True, default='')
  source = models.TextField(blank=True, default='')


  def rendered_notes(self):
    return render_notes(self.notes)

  def __str__(self):
    return str(self.tour) + ": " + self.date.isoformat() + " " + str(self.venue)

  def shortname(self):
    return self.date.isoformat() + " " + str(self.venue)


class SetlistSong(models.Model):
  show = models.ForeignKey(Show, db_index=True)
  song = models.ForeignKey(Song, db_index=True)
  order = models.IntegerField()
  pos = models.FloatField(default=0.0)
  segue = models.BooleanField(default=False)
  set = models.CharField(max_length=1, choices=[('1', '1st Set'), ('2', '2nd Set'), ('3', '3rd Set'), ('E', 'Encore')])
  notes = models.TextField(blank=True, default='')

  def rendered_notes(self):
    return render_notes(self.notes)

  def __str__(self):
    return str(self.order) + ": " + self.song.name

  class Meta:
    ordering = ('order',)


def saveSetlistFromShow(sender, instance=False, **kwargs):
  SetlistSong.objects.filter(show=instance).delete()

  set = 1
  order = 0
  tot = 0.0
  for line in instance.setlist.split('\n'):
    x = line.strip()
    if x != '---' and x != '':
      tot += 1.0
  for line in instance.setlist.split('\n'):
    x = line.strip().split('|')
    if x[0] == '':
      set = 'E'
      continue
    elif x[0] == '---':
      set += 1
      continue
    else:
      segue = False
      if x[0][-1] == '>':
        x[0] = x[0][:-2]
        segue = True

      song, created = Song.objects.get_or_create(slug=slug_song(x[0]), defaults={'name': x[0]})
      order += 1
      notes = ''
      if len(x) > 1:
        notes = x[1]
      if tot == 1.0:
        tot = 2.0
        order = 2.0
      sls = SetlistSong(show=instance, song=song, order=order, set=str(set), notes=notes, segue=segue,
                        pos=(order - 1.0) / (tot - 1.0))
      sls.save()


post_save.connect(saveSetlistFromShow, sender=Show)