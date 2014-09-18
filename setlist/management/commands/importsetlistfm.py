from django.core.management.base import BaseCommand, CommandError
from setlist.models import *
import csv, datetime, urllib, json, pprint

# select Year, Month,Date,City,State,Venue, Track_order, s_Title from Performance p left join Perf_Lookup pl on pl.Perf_ID =p.Perf_ID left join Song s on s.Song_ID = pl.Song_ID

tour = Tour.objects.get(pk=9)

url = 'http://api.setlist.fm/rest/0.1/artist/8eae1e0a-1696-4532-9e3c-0a072217ef4c/setlists.json?p='


class Command(BaseCommand):
  def handle(self, *args, **options):
    for page in range(1, 50):
      p = urllib.urlopen(url + str(page))
      j = json.loads(p.read())

      for s in j['setlists']['setlist']:
        dp = s['@eventDate'].split('-')

        date = datetime.date(int(dp[2]), int(dp[1]), int(dp[0]))

        if Show.objects.filter(date=date).exclude(source='OOTD').exists():
          print 'Show exists for ' + str(date)
        else:
          try:
            Show.objects.filter(date=date).delete()
            ok = False
            city = s['venue']['city']['@name']
            name = s['venue']['@name']
            if s['venue']['city']['country']['@code'] in ['CA', 'US']:
              state = s['venue']['city']['@stateCode']
            else:
              state = s['venue']['city']['@state']
            setlists = []

            if type(s['sets']['set']) == type({}):
              s['sets']['set'] = [s['sets']['set']]
            for set in s['sets']['set']:

              theset = []

              for song in set['song']:
                theset.append(song['@name'])
                ok = True
              setlists.append('\n'.join(theset))
            if ok:
              venue, created = Venue.objects.get_or_create(city=city, state=state, name=name)
              show, created = Show.objects.get_or_create(date=date, venue=venue, tour=tour)

              show.source = 'S.FM'
              show.setlist = '\n'.join(setlists)
              show.save()
              pprint.pprint(show)
          except:
            import traceback

            traceback.print_exc()
            pprint.pprint(s['sets'])
