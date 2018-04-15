from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse

from datetime import datetime

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username

class BlogPost(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    content = models.CharField(max_length=256)
    create_date = models.DateTimeField(default=timezone.now, blank=True)
    publish_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tech_blog:detail', kwargs={'pk':self.pk})

class BlogPostComment(models.Model):
    content = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    post = models.ForeignKey(BlogPost, related_name='comment')

    def __str__(self):
        return self.author
