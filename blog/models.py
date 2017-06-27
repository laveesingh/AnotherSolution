from django.db import models
from django.utils.timezone import now

from tagging.fields import TagField
from tagging.models import Tag
from froala_editor.fields import FroalaField

class Post(models.Model):
    title = models.CharField(default='', max_length=300)
    author = models.CharField(default='', max_length=50)
    # body = models.TextField()
    body = FroalaField()
    date = models.DateTimeField(blank=True)
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