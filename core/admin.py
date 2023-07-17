from django.contrib.admin import site
from .models import Post, AIcamModel, AIchatModel, MessageModel

site.register(Post)
site.register(AIcamModel)
site.register(AIchatModel)
site.register(MessageModel)