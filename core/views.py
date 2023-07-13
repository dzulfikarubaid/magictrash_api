from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import viewsets

@api_view(['GET'])
def post_list(request, id):
    posts = Post.objects.filter(id=id)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def rec_list(request):
    posts = Post.objects.all()[0:4]
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer

