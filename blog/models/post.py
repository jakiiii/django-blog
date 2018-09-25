from django.db import models
from django.db.models.signals import pre_save
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import settings
from django.urls import reverse

from .category import Category
from blog.utils import unique_slug_generator

fs = FileSystemStorage(location='media')
User = settings.AUTH_USER_MODEL


# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, null=False)
    image = models.ImageField(storage=fs, null=True, blank=True)
    link = models.URLField(max_length=300, null=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=False, null=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('details', kwargs={'slug': self.slug})


def blog_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(blog_pre_save_receiver, sender=Post)
