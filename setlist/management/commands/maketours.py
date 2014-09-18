from django.core.management.base import BaseCommand, CommandError
from setlist.models import *
import datetime, pprint
from datetime import date

breaks = [
  [date(1990, 1, 1), "Early Tours"],
  [date(1998, 1, 1), "Gangstabilly Tour"],
  [date(1999, 5, 7), "Pizza Deliverance Tour"],
  [date(2001, 8, 2), "Southern Rock Opera Tour"],
  [date(2003, 6, 12), "Decoration Day Tour"],
  [date(2004, 8, 19), "Dirty South Tour"],
  [date(2006, 2, 22), "A Blessing and a Curse Tour"],
  [date(2007, 4, 20), "The Dirt Underneath Tour"],
  [date(2008, 1, 1), "Brighter Than Creations Dark Tour"],
  [date(2008, 10, 26), 'Rock and Roll Means Well'],
  [date(2009, 1, 15), "Brighter Than Creations Dark Tour"],
  [date(2010, 1, 14), "The Big To-Do Tour"],
  [date(2011, 1, 13), "Go Go Boots Tour"],
  [date(2012, 1, 1), "2012 Tour"],
  [date(2013, 1, 1), "2013 Tour"],
  [date(2014, 1, 1), "2014 Tour"],
  [date(2014, 3, 6), "English Oceans Tour"],
  [date(2039, 1, 1), 'Fallthrough']
]


class Command(BaseCommand):
  def handle(self, *args, **options):
    tours = []
    last = datetime.date(1990, 1, 1)
    tour = []
    for s in Show.objects.all().order_by('date'):
      gap = (s.date - last).days
      if gap >= 14 and tour != []:
        tours.append(tour)
        tour = []
      tour.append(s)
      last = s.date
    tours.append(tour)

    for x in tours:
      if len(x) > 1:
        if x[0].date >= breaks[0][0]:
          b = breaks.pop(0)
          mt, created = MasterTour.objects.get_or_create(name=b[1])
          leg = 1
        else:
          leg += 1
        tour, created = Tour.objects.get_or_create(master_tour=mt, name="Leg " + str(leg))

      else:
        mt2, created = MasterTour.objects.get_or_create(name="Festivals / One-offs")
        tour, created = Tour.objects.get_or_create(master_tour=mt2, name=str(x[0].date.year))
        if created:
          tour.save()
      for show in x:
        show.tour = tour
        show.save()




