from django.contrib import admin
from core.models import Post, User, Comment

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
# Register your models here.
