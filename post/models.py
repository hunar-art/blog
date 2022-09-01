from django.db import models
from django.conf import settings

# Create your models here.

class Tag(models.Model):
    value = models.CharField(max_length=100)
    def __str__(self):
        return self.value
    
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    summary = models.TextField()
    slug = models.SlugField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True,null=True)
    tags = models.ManyToManyField(Tag,related_name='posts')
    
    def __str__(self):
        return self.slug
    
    
    
        
    