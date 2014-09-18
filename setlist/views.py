from annoying.decorators import render_to
from setlist.models import *

from django.db import connection
# Create your views here.
from django.shortcuts import get_object_or_404


@render_to("base.jinja")
def dummy(request):
  return {}


@render_to("show.jinja")
def show(request, show_id=None):
  show = get_object_or_404(Show, pk=int(show_id))

  return {'show': show, 'songs': show.setlistsong_set.all().order_by('order')}


@render_to("song.jinja")
def song(request, song_id=None):
  song = get_object_or_404(Song, pk=int(song_id))
  shows = Show.objects.select_related('tour', 'venue', 'tour__master_tour').filter(
    setlistsong__song_id=song.id).order_by('date')
  return {'song': song, 'shows': shows}


@render_to("matrix.jinja")
def tour(request, tour_id=None):
  order = request.GET.get('order', 'name')
  sorts = {'name': 's.name', 'count': 'c desc, s.name', 'first': 'mindate,s.name', 'last': 'maxdate desc,s.name',
           'least': 'maxdate asc,s.name', 'setlist': 'pos, s.name'}
  sort_names = [('name', 'Title'), ('count', 'Most Played'), ('first', 'Earliest Debut'),
                ('last', 'Most Recent'),
                ('least', 'Least Recent'), ('setlist', 'Average Setlist')]
  cursor = connection.cursor()
  oq = sorts.get(order, sorts['name'])
  if tour_id:
    tour = get_object_or_404(Tour, pk=int(tour_id))
  else:
    tour = Tour.objects.order_by('id')[0]
  shows = Show.objects.filter(tour=tour).order_by('date').prefetch_related('setlistsong_set')
  show_ids = []
  for show in shows:
    show_ids.append(show.id)
  cursor.execute(
    'SELECT s.id, count(sls.song_id) c, min(show.date) AS mindate, max(show.date) AS maxdate, s.name, avg(sls.pos) as pos FROM setlist_setlistsong sls LEFT JOIN setlist_song s ON s.id = sls.song_id left join setlist_show show on show.id = sls.show_id where sls.show_id in %s GROUP BY s.id ORDER BY ' + oq,
    (tuple(show_ids),))
  songs = []
  for row in cursor.fetchall():
    song = {'name': row[4], 'mindate': row[2], 'maxdate': row[3], 'count': row[1], 'id': row[0], 'shows': []}
    debut = False
    repeat = 0
    for show in shows:
      found = False
      for x in show.setlistsong_set.all():
        if x.song_id == song['id']:
          found = True
          extra = ''

          if repeat == 0 and not debut:
            debut = True
            song['shows'].append('Debut')
            repeat = 1
          elif x.pos == 0.0:
            song['shows'].append('Opener')
            repeat += 1
          elif x.pos == 1.0:
            song['shows'].append('Closer')
            repeat += 1
          else:
            repeat += 1
            song['shows'].append(str(repeat) + 'x')
          break

      if not found:
        repeat = 0
        song['shows'].append('')

    songs.append(song)

  return {'songs': songs, 'shows': shows, 'order': order, 'sorts': sort_names, 'tour': tour}


@render_to("home.jinja")
def home(request):
  shows = Show.objects.exclude(setlist='').order_by('-date')[:25]

  return {'shows': shows}


@render_to("analysis.jinja")
def analysis(request, tour_id):
  tour = get_object_or_404(Tour, pk=int(tour_id))
  albums = Album.objects.all().order_by('-release_date').prefetch_related('song_set')
  cursor = connection.cursor()
  cursor.execute(
    'select sls.song_id, count(*), sum(case when pos = 0.0 then 1 else 0 end) as opener, sum(case when pos = 1.0 then 1 else 0 end) as closer from setlist_setlistsong sls where sls.show_id in %s group by sls.song_id',
    (tuple(Show.objects.filter(tour=tour).values_list('id', flat=True)),))
  song_data = {}
  for x in cursor.fetchall():
    song_data[x[0]] = x[1:]
  s = []
  for a in albums:
    xs = []
    for song in a.song_set.all():
      sd = song_data.get(song.id, [0])
      if sd[0] > 0:
        row = [song.name, sd[0], sd[1], sd[2], song.id]
        xs.append(row)
    if len(xs) > 0:
      s.append([a.name, xs])
  xs = []
  for song in Song.objects.filter(album=None).order_by('name'):
    sd = song_data.get(song.id, [0])

    if sd[0] > 0:
      row = [song.name, sd[0], sd[1], sd[2], song.id]
      xs.append(row)
  if len(xs) > 0:
    s.append(['Non-Album Tracks', xs])
  return {'tour': tour, 'data': s}
