from django import forms
from .models import Comment

Class CommentForm(forms.ModelForm):
    class Meta:
        model=Commentfields=('author', 'text')