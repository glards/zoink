from torrent.models import Torrent

class ZoinkscraperPipeline(object):
    def process_item(self, domain, item):
        try:
            Torrent.objects.get(name=item['name'])
        except Torrent.DoesNotExist:
            t = Torrent()
            t.name = item['name']
            t.url = item['url']
            t.added = item['date']
            t.save()
        return item
