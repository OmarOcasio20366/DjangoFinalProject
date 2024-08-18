from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# Represents Blog Posts
class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    author = models.ForeignKey(User, related_name = 'posts', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
# Represents Comments on posts
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name = 'comments', on_delete = models.CASCADE)
    author = models.ForeignKey(User, related_name = 'comments', on_delete = models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    