from setlist.models import *
from django.contrib import admin
from django.contrib.admin import site
import adminactions.actions as actions

# register all adminactions
actions.add_to_site(site)
# Register your models here.

class SongAdmin(admin.ModelAdmin):
  ordering = ('name',)
  list_filter = ('author', 'album')


class ShowAdmin(admin.ModelAdmin):
  ordering = ('date',)
  date_hierarchy = 'date'
  list_filter = ('tour__master_tour', 'venue__state')
  # fields = ('date', 'venue')


class TourAdmin(admin.ModelAdmin):
  ordering = ('name',)
  list_filter = ('master_tour',)


admin.site.register(Show, ShowAdmin)

admin.site.register(Album)
admin.site.register(Song, SongAdmin)
admin.site.register(Venue)
admin.site.register(Tour, TourAdmin)
admin.site.register(MasterTour)
admin.site.register(Person)

