from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Post(models.Model):
	title = models.CharField(max_length=120) #title & max length of title
	
	content = models.TextField(max_length=2000) #actual post & their max length
	
	updated = models.DateTimeField(auto_now=True, auto_now_add=False) #update timestamp
	
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True) #initial post timestamp

	def __unicode__(self):
		return self.title
	
	def __str__(self):
		return self.title