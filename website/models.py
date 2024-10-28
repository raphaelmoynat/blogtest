from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles', null=True)
    created_at = models.DateTimeField(auto_now=True, null=True)




class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(verbose_name='Contenu du commentaire')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=True)
    created_at = models.DateTimeField(auto_now=True, null=True)
