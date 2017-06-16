from django.db import models
from django.utils.timezone import now

from tagging.fields import TagField
from tagging.models import Tag

class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    # last_edit = models.CharField(max_length=200)
    date = models.DateTimeField(default=now)
    last_edit_date = models.DateTimeField(default=now)
    tags = TagField()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/blog/%d' % self.id

    def get_tags(self):
        return Tag.objects.get_for_object(self)