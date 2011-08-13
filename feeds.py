from django.contrib.syndication.feeds import Feed
from zoink.torrent.models import Torrent

class TorrentsFeed(Feed):
    title = "Latest TV torrents"
    link = "/"
    description = ""

    def items(self):
        return Torrent.objects.order_by('-added')[:15]
