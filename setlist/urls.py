from django.conf.urls import patterns, include, url

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from dbt import settings

urlpatterns = patterns('',
                       url('^dummy', 'setlist.views.dummy'),
                       url(r'^tour/(?P<tour_id>[0-9]+)', 'setlist.views.tour'),
                       url(r'^tour-analysis/(?P<tour_id>[0-9]+)', 'setlist.views.analysis'),
                       url(r'^song/(?P<song_id>[0-9]+)', 'setlist.views.song'),
                       url(r'^show/(?P<show_id>[0-9]+)', 'setlist.views.show'),
                       url(r'^$', 'setlist.views.home', name='home'),


)
