from django.db import models

# Create your models here.
class Post(models.Model):
    newsTitle = models.TextField(blank=True)
    newsContent = models.TextField(blank=True)
    newsLink = models.URLField(blank=True)
    imgLink = models.URLField(blank=True)
    newsNum = models.IntegerField(default=0)

    def __str__(self):
         return self.newsTitle