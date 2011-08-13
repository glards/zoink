from django.db import models
from zoink.torrent.models import Torrent

class Click(models.Model):
    torrent = models.ForeignKey(Torrent)
    date = models.DateTimeField(auto_now_add=True)
    ip_address = models.IPAddressField()
