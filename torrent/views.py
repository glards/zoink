from zoink.torrent.models import Torrent
from django.shortcuts import render_to_response
from django.conf import settings

def index(request):
    dates = list(Torrent.objects.dates('added','day','DESC')[:settings.MAX_DAYS])
    last_date = dates[-1]
    torrents = Torrent.objects.filter(added__gt=last_date.date).order_by('-added')
    return render_to_response('zoink.html', {'torrents': torrents})