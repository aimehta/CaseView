from django.db import models

# Create your models here.

class imageupload(models.Model):

    title = models.CharField(max_length=50)
    images = models.ImageField('images')
