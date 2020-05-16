from django.db import models

class Gallery(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    raiting = models.IntegerField(default = 0)
    title = models.CharField(max_length = 250)
