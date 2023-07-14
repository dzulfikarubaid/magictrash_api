from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    harga_asli = models.IntegerField()
    harga_diskon = models.IntegerField()
    image1 = models.TextField(blank=True, default='')
    image2 = models.TextField(blank=True, default='')
    image3 = models.TextField(blank=True, default='')
    image4 = models.TextField(blank=True, default='')
    image5 = models.TextField(blank=True, default='')

    def __str__(self):
        return self.title