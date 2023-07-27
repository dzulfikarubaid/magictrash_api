from django.contrib.admin import site
from .models import Post, Donasi, Jual

site.register([Post, Donasi, Jual])