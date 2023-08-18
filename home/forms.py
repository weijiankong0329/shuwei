from django import forms
from django.forms import ModelForm
from .models import 评论_视频

class 视频_comment_form(ModelForm):
    class Meta:
        model = 评论_视频
        exclude =['视频', '发表时间','通过']
        widgets = {
            '评论': forms.Textarea(attrs={'class': 'form-control'})
        }