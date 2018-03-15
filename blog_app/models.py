from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    content = models.CharField(max_length=256)

    def __str__(self):
        return self.title
