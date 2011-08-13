from django.db import models

class Torrent(models.Model):
	name = models.CharField(max_length=256)
	added = models.DateTimeField()
	url = models.CharField(max_length=512)
	
	def __unicode__(self):
		return self.name
