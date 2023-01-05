from django.db import models

class Kategori(models.Model):
    nama = models.CharField(max_length=20)

class Postingan(models.Model):
    judul = models.CharField(max_length=255)
    isi   = models.TextField()
    tgl_buat = models.DateTimeField(auto_now_add=True)
    akhir_buat = models.DateTimeField(auto_now=True) 
    kategori = models.ManyToManyField('Kategori', related_name='posting')

class Komentar(models.Model):
    penulis = models.CharField(max_length=60)
    isi = models.TextField()
    tgl_buat = models.DateTimeField(auto_now_add=True)
    postingan = models.ForeignKey('Postingan', on_delete=models.CASCADE)