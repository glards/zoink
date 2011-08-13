from django.conf.urls.defaults import *

urlpatterns = patterns('zoink.stats.views',
    url(r'click/(?P<torrent_id>\d*)$', 'click', name = "click"),
    url(r'list$', 'index'),
)