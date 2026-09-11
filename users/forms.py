from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label='e-mail')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name', 'bio', 'profile_picture', 'main_category', 'profile_tags']
        widgets = {
            'profile_tags': forms.CheckboxSelectMultiple,
        }

    def clean_profile_tags(self):
        tags = self.cleaned_data.get('profile_tags')
        if tags and tags.count() > Profile.MAX_TAGS:
            raise forms.ValidationError(
                f'Você pode escolher no máximo {Profile.MAX_TAGS} tags.'
            )
        return tags