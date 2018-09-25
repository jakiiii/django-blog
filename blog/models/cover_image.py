from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='media')


# Create your models here.
class CoverImage(models.Model):
    title = models.CharField(max_length=255)
    cover_image = models.ImageField(storage=fs, null=False)

    def __str__(self):
        return self.title
