from django import forms
from .models import *


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['description', 'image']


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone', 'bio']
