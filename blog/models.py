from django.db import models
from django.utils.timezone import now
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    last_edit = models.CharField(max_length=200)
    date = models.DateTimeField()
    last_edit_date = models.DateTimeField(default=now)
    tags = models.CharField(max_length=140)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

