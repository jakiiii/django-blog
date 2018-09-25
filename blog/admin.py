from django.contrib import admin
from .models import CoverImage, Category, Post


# Register your models here.
admin.site.register(CoverImage)
admin.site.register(Category)
admin.site.register(Post)
