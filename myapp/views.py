from .serializers import PostSerializer, CommentSerializer
from rest_framework import filters
from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Comment

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'
    ordering = ['created_at']
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer