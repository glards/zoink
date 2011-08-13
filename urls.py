from django.conf.urls.defaults import *
from zoink.feeds import TorrentsFeed

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

feeds = {
    'torrents': TorrentsFeed,
}


urlpatterns = patterns('',
    # Example:
    (r'^', include('zoink.torrent.urls')),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
    (r'^stats/', include('zoink.stats.urls')),
    (r'^search$','zoink.search.views.search'),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
