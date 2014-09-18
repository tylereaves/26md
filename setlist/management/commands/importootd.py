from django.core.management.base import BaseCommand, CommandError
from setlist.models import *
import csv, datetime

# select Year, Month,Date,City,State,Venue, Track_order, s_Title from Performance p left join Perf_Lookup pl on pl.Perf_ID =p.Perf_ID left join Song s on s.Song_ID = pl.Song_ID

import MySQLdb as mysql

tour = Tour.objects.get(pk=8)


class Command(BaseCommand):
  def handle(self, *args, **options):
    db = mysql.connect(user='root', passwd='mysql', db='dbt')
    c = db.cursor()
    c2 = db.cursor()
    c.execute("SELECT * FROM Performance ORDER BY Year,Month,Date")
    for r in c.fetchall():
      r = list(r)
      if len(r[3]) > 2:
        r[3] = r[3][:2]

      date = datetime.date(int(r[1]), int(r[2]), int(r[3]))
      if Show.objects.filter(date=date, venue__name=r[6]).exclude(source='OOTD').exists():
        print 'Show exists for ' + str(r)
      else:
        setlist = []
        ok = False
        c2.execute(
          "SELECT s_Title FROM Perf_Lookup p LEFT JOIN Song s ON s.Song_ID = p.Song_ID WHERE p.Perf_ID = " + str(
            r[0]) + " ORDER BY p.Track_order")
        for s in c2.fetchall():
          if s[0] != None:
            setlist.append(s[0])
            ok = True
        sl = '\n'.join(setlist)
        if sl == None:
          sl = ''
        if ok:
          print sl

          venue, created = Venue.objects.get_or_create(city=r[4], state=r[5], name=r[6])
          show, created = Show.objects.get_or_create(tour=tour, venue=venue,
                                                     date=date, source="OOTD")
          print show
          show.setlist = sl
          show.save()
