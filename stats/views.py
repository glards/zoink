from zoink.torrent.models import Torrent
from zoink.stats.models import Click
from django.http import HttpResponse
from django.shortcuts import render_to_response

def click(request, torrent_id):
    try:
        clicked_torrent = Torrent.objects.get(id=torrent_id)
        stat = Click()
        stat.torrent = clicked_torrent
        stat.ip_address = request.META['REMOTE_ADDR']
        stat.save()
        return HttpResponse("Ok")
    except Torrent.DoesNotExist:
        return HttpResponse("Not Found")

def index(request):
    stats = Click.objects.order_by('-date')[:100]
    return render_to_response('stats.html', {'stats': stats})