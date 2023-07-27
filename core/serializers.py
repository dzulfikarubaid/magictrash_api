from rest_framework import serializers
from .models import Donasi, Jual, Post
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

from rest_framework import serializers
from .models import DetailsModel, AIcamModel, AIchatModel, MessageModel

class AIcamSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIcamModel
        fields = '__all__'
    
class AIchatSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIchatModel
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields = '__all__'  

class JualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jual
        fields = '__all__'

class DonasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donasi
        fields = '__all__'