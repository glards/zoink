from zoink.torrent.models import Torrent
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

def search(request):
    if request.method == 'GET':
        q = request.GET.get('q')
        if q:
            torrents = Torrent.objects
            for word in q.split(' '):
                torrents = torrents.filter(name__icontains=word)
            torrents = torrents.order_by('-added')
            return render_to_response('search.html', {'torrents': torrents})
    return HttpResponseRedirect('/')
