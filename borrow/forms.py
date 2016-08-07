from django import forms
from .models import Comment
from lend.models import Machine, Tag

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['content']
        labels={'content':'내용'}

class SearchForm(forms.Form):
    MACHINE_NAME=(
        ('', '전체'),
        ('1', '세그웨이'),
        ('2', '전동 퀵보드'),
        )
    TAG_CHOICES=(
        ('', '전체'),
        ('1', '서울대입구'),
        ('2', '서울대'),
        ('3', '녹두'),
        ('4', '낙성대'),
        )
    machine=forms.ChoiceField(choices=MACHINE_NAME, required=False)
    location=forms.ChoiceField(choices=TAG_CHOICES, required=False)
    price=forms.CharField(max_length=20, required=False)
    date=forms.IntegerField(required=False)

