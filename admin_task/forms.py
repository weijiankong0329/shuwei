from django import forms
from django.forms import ModelForm
from home.models import 通讯,书讯,书评,译林,文摘,论文,经训,古籍,书库,观点,文艺,视频,问答,章节_经训

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

class 书评_add_form(ModelForm):
    class Meta:
        model = 书评
        fields ="__all__"
        labels={
            '发布状态':'确认发布'
        }
        widgets = {
            '书籍标题': forms.TextInput(attrs={'class': 'form-control'}),
            '书籍作者': forms.TextInput(attrs={'class': 'form-control'}),
            '书籍出版日期': forms.TextInput(attrs={'class': 'form-control','type':'date'}),
            '书评内容':forms.Textarea(attrs={'class': 'form-control'}),
            '书评作者': forms.TextInput(attrs={'class': 'form-control'})
        }

class 观点_add_form(ModelForm):
    class Meta:
        model = 观点
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

class 文艺_add_form(ModelForm):
    class Meta:
        model = 文艺
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

class 问答_add_form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(问答_add_form, self).__init__(*args, **kwargs)
        self.fields['参考问答项目'].queryset = self.fields['参考问答项目'].queryset.exclude(参考问答=True)

    class Meta:
        model = 问答
        fields ="__all__"
        labels ={
            '发布状态': '确认发布'
        }
        widgets = {
            '标题': forms.TextInput(attrs={'class': 'form-control'}),
            '答案': forms.Textarea(attrs={'class': 'form-control'}),
            '参考问答项目': forms.Select(attrs={'class': 'form-control'})
        }

class 视频_add_form(ModelForm):
    class Meta:
        model = 视频
        fields = "__all__"

        labels = {
            '发布状态': '确认发布'
        }
        widgets = {
            '标题': forms.TextInput(attrs={'class': 'form-control'}),
            '内容': forms.Textarea(attrs={'class': 'form-control'}),
            '资源': forms.TextInput(attrs={'class': 'form-control'}),
            '作者': forms.TextInput(attrs={'class': 'form-control'})
        }


class 译林_add_form(ModelForm):
    class Meta:
        model = 译林
        fields ="__all__"
        labels={
            '发布状态':'确认发布'
        }
        widgets = {
            '标题': forms.TextInput(attrs={'class': 'form-control'}),
            '原文标题':forms.TextInput(attrs={'class': 'form-control'}),
            '原文作者': forms.TextInput(attrs={'class': 'form-control'}),
            '原文出版日期': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            '译文内容': forms.Textarea(attrs={'class': 'form-control'}),
            '译文作者': forms.TextInput(attrs={'class': 'form-control'}),
           
        }

class 文摘_add_form(ModelForm):
    class Meta:
        model = 文摘
        fields ="__all__"
        labels={
            '发布状态':'确认发布'
        }
        widgets = {
            '标题': forms.TextInput(attrs={'class': 'form-control'}),
            '内容': forms.Textarea(attrs={'class': 'form-control'}),
            '作者': forms.TextInput(attrs={'class': 'form-control'}),
            '资源': forms.TextInput(attrs={'class': 'form-control'})
        }

class 论文_add_form(ModelForm):
    class Meta:
        model = 论文
        fields ="__all__"
        labels={
            '发布状态':'确认发布'
        }
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
        fields ="__all__"
        labels={
            '发布状态':'确认发布'
        }
        widgets = {
            '标题': forms.TextInput(attrs={'class': 'form-control'}),
            '更新时间': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class 章节_经训_Form(ModelForm):
    class Meta:
        model = 章节_经训
        exclude = ['经训']
        widgets = {
            '章节': forms.TextInput(attrs={'class': 'form-control'}),
            '内容': forms.Textarea(attrs={'class': 'form-control'}),
        }

class 古籍_add_form(ModelForm):
    class Meta:
        model = 古籍
        fields ="__all__"
        labels={
            '发布状态':'确认发布'
        }
        widgets = {
            '标题': forms.TextInput(attrs={'class': 'form-control'}),
            '作者 ': forms.TextInput(attrs={'class': 'form-control'}),
            '文档': forms.FileInput(attrs={'id':'file'}),
        }

class 书库_add_form(ModelForm):
    class Meta:
        model = 书库
        fields ="__all__"
        labels={
            '发布状态':'确认发布'
        }
        widgets = {
            '标题': forms.TextInput(attrs={'class': 'form-control'}),
            '作者 ': forms.TextInput(attrs={'class': 'form-control'}),
            '文档': forms.FileInput(attrs={'id':'file'}),
            '简介': forms.Textarea(attrs={'class': 'form-control'}),
            '图片': forms.FileInput(attrs={'id':'image'}),
            '序号': forms.TextInput(attrs={'class': 'form-control'}),
        }