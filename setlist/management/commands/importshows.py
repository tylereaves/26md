from django.core.management.base import BaseCommand, CommandError
from setlist.models import *
import csv, datetime


class Command(BaseCommand):
  args = 'tour_id filename'
  help = 'Import a list of shows in csv format'


  def handle(self, *args, **options):
    tour = Tour.objects.get(pk=args[0])
    inf = csv.reader(open(args[1]))
    for line in inf:
      date = line[0].split('/')
      year = int(date[2])
      if year < 90:
        year = year + 2000
      else:
        year = year + 1900
      date = datetime.date(year, int(date[0]), int(date[1]))
      v = line[1].rsplit(' ', 1)
      venue, created = Venue.objects.get_or_create(name=line[2], city=v[0], state=v[1])
      show, created = Show.objects.get_or_create(tour=tour, venue=venue,
                                                 date=date)  # , notes=line[3].replace('\xa0', ''))


