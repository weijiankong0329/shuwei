from django import forms
from django.forms import ModelForm
<<<<<<< HEAD
from home.models import 通讯,译林,文摘,论文,经训,古籍,书库
=======
from home.models import 通讯
from home.models import 书讯
>>>>>>> 5e35798edac67f9864d89dc1f29f7f793969771c
from django.contrib.auth.forms import AuthenticationForm, UsernameField

class CustomLoginForm(AuthenticationForm):
    username = UsernameField(label='用户名',widget=forms.TextInput(attrs={'autofocus':True}))
    password = forms.CharField(label='密码',widget = forms.PasswordInput(attrs={}))

class 通讯_add_form(ModelForm):
    class Meta:
        model = 通讯
        fields ="__all__"
        labels={
            '发布状态':'确认发布'
        }
        widgets = {
            '标题': forms.TextInput(attrs={'class': 'form-control'}),
            '内容': forms.Textarea(attrs={'class': 'form-control'}),
            '资源': forms.TextInput(attrs={'class': 'form-control'}),
            '作者': forms.TextInput(attrs={'class': 'form-control'})
        }

class 书讯_add_form(ModelForm):
    class Meta:
        model = 书讯
        fields ="__all__"
        labels={
            '发布状态':'确认发布'
        }
        widgets = {
            '序号': forms.TextInput(attrs={'class': 'form-control'}),
            '标题': forms.TextInput(attrs={'class': 'form-control'}),
            '简介': forms.Textarea(attrs={'class': 'form-control'}),
            '作者': forms.TextInput(attrs={'class': 'form-control'})
        }

class 译林_add_form(ModelForm):
    class Meta:
        model = 译林
        exclude =['发布状态']
        widgets = {
            '译文标题': forms.TextInput(attrs={'class': 'form-control'}),
            '原文内容': forms.Textarea(attrs={'class': 'form-control'}),
            '译文作者': forms.TextInput(attrs={'class': 'form-control'}),
            '原文作者': forms.TextInput(attrs={'class': 'form-control'}),
            '图片': forms.FileInput(attrs={'id':'image'})
        }

class 文摘_add_form(ModelForm):
    class Meta:
        model = 文摘
        exclude =['发布状态']
        widgets = {
            '标题': forms.TextInput(attrs={'class': 'form-control'}),
            '内容': forms.Textarea(attrs={'class': 'form-control'}),
            '作者': forms.TextInput(attrs={'class': 'form-control'}),
            '资源': forms.TextInput(attrs={'class': 'form-control'}),
            '图片': forms.FileInput(attrs={'id':'image'})
        }


class 论文_add_form(ModelForm):
    class Meta:
        model = 论文
        exclude =['发布状态']
        widgets = {
            '标题': forms.TextInput(attrs={'class': 'form-control'}),
            '文档': forms.FileInput(attrs={'id':'file'}),
            '作者': forms.TextInput(attrs={'class': 'form-control'}),
        }

class 论文_edit_form(ModelForm):
    class Meta:
        model = 论文
        exclude =['发布状态']
        widgets = {
            '标题': forms.TextInput(attrs={'class': 'form-control'}),
            '文档': forms.FileInput(attrs={'id':'file'}),
            '作者': forms.TextInput(attrs={'class': 'form-control'}),
        }

class 经训_add_form(ModelForm):
    class Meta:
        model = 经训
        exclude =['发布状态']
        widgets = {
            '标题': forms.TextInput(attrs={'class': 'form-control'}),
            '章节': forms.TextInput(attrs={'class': 'form-control'}),
            '内容': forms.Textarea(attrs={'class': 'form-control'}),
        }

class 古籍_add_form(ModelForm):
    class Meta:
        model = 古籍
        exclude =['发布状态']
        widgets = {
            '标题': forms.TextInput(attrs={'class': 'form-control'}),
            '作者 ': forms.TextInput(attrs={'class': 'form-control'}),
            '文档': forms.FileInput(attrs={'id':'file'}),
        }

class 书库_add_form(ModelForm):
    class Meta:
        model = 书库
        exclude =['发布状态']
        widgets = {
            '标题': forms.TextInput(attrs={'class': 'form-control'}),
            '作者 ': forms.TextInput(attrs={'class': 'form-control'}),
            '文档': forms.FileInput(attrs={'id':'file'}),
            '简介': forms.Textarea(attrs={'class': 'form-control'}),
            '图片': forms.FileInput(attrs={'id':'image'}),
            '序号': forms.TextInput(attrs={'class': 'form-control'}),
        }