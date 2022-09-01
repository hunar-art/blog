from django.contrib import admin
from .models import Tag,Post

class PostAdmin(admin.ModelAdmin):
    exclude = ['slug']
    list_display = ['title','published_at']
    
admin.site.register(Tag)
    