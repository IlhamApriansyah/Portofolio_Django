from django.db import models

# Create your models here.
class Project(models.Model):

    judul = models.CharField(max_length=100)
    deskripsi = models.TextField()
    teknologi = models.CharField(max_length=20)
    image = models.FilePathField("/img")