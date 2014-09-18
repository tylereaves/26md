from django.core.management.base import BaseCommand, CommandError
from setlist.models import *
import csv, datetime


class Command(BaseCommand):
  args = ''
  help = ''


  def handle(self, *args, **options):
    f = args[0].lower()
    r = args[1]
    for s in Show.objects.raw("SELECT * FROM setlist_show WHERE lower(setlist) LIKE '%%" + args[0] + "%%'"):
      sl = s.setlist.split('\n')
      print s
      i = 0
      save = False
      for l in sl:
        if l.lower().strip() == f:
          sl[i] = r
          save = True
          print "Match found: " + str(s)
        i += 1
      if save:
        s.setlist = '\n'.join(sl)
      s.save()
