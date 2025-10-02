from django.contrib import admin
from .models import Post, Comment  # adjust if Post already registered

admin.site.register(Post)
admin.site.register(Comment)
