from django.db import models
from django.contrib.auth.models import User



class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    user = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
