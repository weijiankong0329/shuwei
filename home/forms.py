from django import forms
from django.forms import ModelForm
from .models import 评论_视频,评论_问答,评论_书评,评论_观点,评论_文艺
class 视频_comment_form(ModelForm):
    class Meta:
        model = 评论_视频
        exclude =['视频', '发表时间','通过']
        widgets = {
            '评论': forms.Textarea(attrs={'class': 'form-control'})
        }

class 问答_comment_form(ModelForm):
    class Meta:
        model = 评论_问答
        exclude =['问答', '发表时间','通过']
        widgets = {
            '评论': forms.Textarea(attrs={'class': 'form-control'})
        }

class 书评_comment_form(ModelForm):
    class Meta:
        model = 评论_书评
        exclude =['书评', '发表时间','通过']
        widgets = {
            '评论': forms.Textarea(attrs={'class': 'form-control'})
        }

class 观点_comment_form(ModelForm):
    class Meta:
        model = 评论_观点
        exclude =['观点', '发表时间','通过']
        widgets = {
            '评论': forms.Textarea(attrs={'class': 'form-control'})
        }

class 文艺_comment_form(ModelForm):
    class Meta:
        model = 评论_文艺
        exclude =['文艺', '发表时间','通过']
        widgets = {
            '评论': forms.Textarea(attrs={'class': 'form-control'})
        }