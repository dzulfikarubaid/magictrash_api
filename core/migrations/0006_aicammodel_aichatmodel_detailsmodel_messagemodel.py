# Generated by Django 4.2.3 on 2023-07-17 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_post_image1_alter_post_image2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AIcamModel',
            fields=[
                ('id_img', models.AutoField(primary_key=True, serialize=False)),
                ('img', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AIchatModel',
            fields=[
                ('id_chat', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('chat', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DetailsModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=40)),
                ('desc', models.TextField(max_length=250)),
                ('image', models.CharField(max_length=20)),
                ('skill1', models.CharField(max_length=20)),
                ('skill2', models.CharField(max_length=20)),
                ('skill3', models.CharField(max_length=20)),
                ('skill4', models.CharField(max_length=20)),
                ('skill5', models.CharField(max_length=20)),
                ('skill6', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MessageModel',
            fields=[
                ('id_msg', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('msg', models.TextField()),
            ],
        ),
    ]
