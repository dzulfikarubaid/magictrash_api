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
    
class DetailsModel(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=40)
    desc=models.TextField(max_length=250)
    image=models.CharField(max_length=20)
    skill1=models.CharField(max_length=20)
    skill2=models.CharField(max_length=20)
    skill3=models.CharField(max_length=20)
    skill4=models.CharField(max_length=20)
    skill5=models.CharField(max_length=20)
    skill6=models.CharField(max_length=20)
    def __str__(self):
        return self.title or ''

class AIcamModel(models.Model):
    id_img = models.AutoField(primary_key=True)
    img = models.TextField()
   
class AIchatModel(models.Model):
    id_chat = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    chat = models.TextField()

class MessageModel(models.Model):
    id_msg = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    msg = models.TextField()

class Jual(models.Model):
    nama_barang = models.CharField(max_length=30)
    nomor_wa = models.CharField(max_length=30)
    alamat = models.TextField()
    harga = models.TextField()
    alasan = models.TextField()
    foto_barang = models.TextField()

class Donasi(models.Model):
    nama_barang = models.CharField(max_length=30)
    nomor_wa = models.CharField(max_length=30)
    alamat = models.TextField()
    alasan = models.TextField()
    foto_barang = models.TextField()