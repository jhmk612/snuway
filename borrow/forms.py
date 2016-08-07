from django import forms
from .models import Comment
from lend.models import Machine, Tag

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['content']
        labels={'content':'내용'}

class SearchForm(forms.Form):
    machine=forms.ChoiceField(choices=Machine.names)
    location=forms.ChoiceField(choices=Tag_tag)
    price=forms.CharField(max_length=20, required=False)
    date=forms.IntegerField(required=False)

