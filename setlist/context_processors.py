from setlist.models import Tour, Song, Album
from django.db import connection


def tour_processor(request):
  # tours = Tour.objects.all().order_by('-start_date')
  c = connection.cursor()
  c2 = connection.cursor()
  c.execute(
    'SELECT mt.id, mt.name, count(s.id), min(s.date) mind, max(s.date) maxd FROM setlist_mastertour mt LEFT JOIN setlist_tour t ON t.master_tour_id = mt.id LEFT JOIN setlist_show s ON s.tour_id = t.id  GROUP BY mt.id ORDER BY mind DESC')
  tours = []
  for mt in c.fetchall():
    tour = {'name': mt[1], 'legs': []}
    c2.execute(
      'SELECT t.id, t.name, count(s.id) c,  min(s.date) mind, max(s.date) maxd FROM setlist_tour t LEFT JOIN setlist_show s ON s.tour_id = t.id  WHERE t.master_tour_id = ' + str(
        mt[0]) + '  GROUP BY t.id ORDER BY mind')
    for t in c2.fetchall():
      if t[2] > 0:
        tour['legs'].append(
          {'name': t[1] + ' (' + t[3].isoformat().replace('-', '/') + ' - ' + t[4].isoformat().replace('-', '/') + ')',
           'id': t[0]})
    tours.append(tour)
  albums = [{'name': 'Non-Album Tracks',
             'songs': [{'name': x.name, 'id': x.id} for x in Song.objects.filter(album=None).order_by('name') if
                       x.setlistsong_set.count() > 0]}]
  for album in Album.objects.all().order_by('release_date'):
    albums.append(
      {'name': album.name, 'songs': [{'name': x.name, 'id': x.id} for x in album.song_set.order_by('name')]})
  return {'tours': tours, 'albums': albums}