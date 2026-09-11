from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'cover_image',
            'category',
            'tags',
        ]
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 12,
            }),
            'tags': forms.CheckboxSelectMultiple,
        }