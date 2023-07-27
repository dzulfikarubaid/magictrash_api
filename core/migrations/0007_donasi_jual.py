# Generated by Django 4.2.3 on 2023-07-27 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_aicammodel_aichatmodel_detailsmodel_messagemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_barang', models.CharField(max_length=30)),
                ('nomor_wa', models.CharField(max_length=30)),
                ('alamat', models.TextField()),
                ('alasan', models.TextField()),
                ('foto_barang', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Jual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_barang', models.CharField(max_length=30)),
                ('nomor_wa', models.CharField(max_length=30)),
                ('alamat', models.TextField()),
                ('harga', models.IntegerField()),
                ('alasan', models.TextField()),
                ('foto_barang', models.TextField()),
            ],
        ),
    ]
