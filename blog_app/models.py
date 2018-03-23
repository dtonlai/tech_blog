from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username

class BlogPost(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    content = models.CharField(max_length=256)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
