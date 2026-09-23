from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    MIN_CONTENT_LENGTH = 50

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

    def clean_content(self):
        content = self.cleaned_data.get('content')

        if content and len(content.strip()) < self.MIN_CONTENT_LENGTH:
            raise forms.ValidationError(
                f'O conteúdo do post precisa ter pelo menos {self.MIN_CONTENT_LENGTH} caracteres.'
            )

        return content