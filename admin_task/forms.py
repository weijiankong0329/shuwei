from django import forms
from django.forms import ModelForm
from home.models import 通讯
from django.contrib.auth.forms import AuthenticationForm, UsernameField

class CustomLoginForm(AuthenticationForm):
    username = UsernameField(label='用户名',widget=forms.TextInput(attrs={'autofocus':True}))
    password = forms.CharField(label='密码',widget = forms.PasswordInput(attrs={}))

class 通讯_add_form(ModelForm):
    class Meta:
        model = 通讯
        exclude =['发布状态']
        widgets = {
            '标题': forms.TextInput(attrs={'class': 'form-control'}),
            '内容': forms.Textarea(attrs={'class': 'form-control'}),
            '资源': forms.TextInput(attrs={'class': 'form-control'}),
            '作者': forms.TextInput(attrs={'class': 'form-control'}),
            '图片': forms.FileInput(attrs={'id':'image'})
        }
