from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from dbt import settings

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'dbt.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'', include('setlist.urls')),
                       url(r'^adminactions/', include('adminactions.urls')),
                       url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                           document_root=settings.STATIC_ROOT)
