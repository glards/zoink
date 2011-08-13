from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('zoink.torrent.views',
    (r'^$', 'index'),
)