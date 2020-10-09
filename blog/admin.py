from django.contrib import admin
from .models import Post

# Register given model to make it visible on admin page.
# admin.site.register(ModelName)
admin.site.register(Post)
