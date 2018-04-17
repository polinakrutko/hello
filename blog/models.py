from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
<<<<<<< HEAD
    title = models.CharField(max_lenght=200)
=======
    title = models.CharField(max_length=200)
>>>>>>> a62a6604fb5a485d4c303b7b567b69be3eb0f8a1
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.publis_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title
        