from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    outhor = models.ForeignKey('auth.User')
    title = models.CharField(max_lenght=200)
    text = models.TextField()
    created_date = models.dateTimeField(default=timezone.now)
    published_date = models.dateTimeField(blank=True, null=True)
    
    def publish(self):
        self.publis_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title
        