from django.contrib import admin
from .models import Post, Comment, User, Major

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Major)