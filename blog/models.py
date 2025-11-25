# blog/models.py

from django.conf import settings
from django.db import models


class Post(models.Model):
    # link to the user who wrote the post
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name="posts",
    )

    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)  
    modified_at = models.DateTimeField(auto_now=True)     
    published_at = models.DateTimeField(null=True, blank=True) 

    # main content fields
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)   
    summary = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title


