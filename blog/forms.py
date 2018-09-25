from django import forms

from .models import Post


# Create your form here.
class DateInput(forms.DateInput):
    input_type = 'date'


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'image',
            'link',
            'description',
            'category',
            'date',
            'slug'
        ]
        widgets = {
            'date': DateInput(),
        }

        labels = {
            'title': 'Title',
            'image': 'Image',
            'link': 'Youtube Link',
            'description': 'Description',
            'category': 'Category',
            'date': 'Date',
            'slug': 'Slug'
        }
