from django.db import models
from ckeditor.fields import RichTextField
from sorl.thumbnail import ImageField
# Create your models here.
# 通讯
class 通讯(models.Model):
    标题 = models.CharField(max_length=150)
    内容 = RichTextField(blank=True,null=True)
    更新时间 = models.DateTimeField(auto_now=True)
    发布状态 = models.BooleanField(default=False)
    资源 = models.CharField(max_length=200,null=True,blank=True,default="无资源信息")
    作者 = models.CharField(max_length=200,null=True,blank=True,default="无作者信息")
    def __str__(self):
        return self.标题


class 书讯(models.Model):
    标题 = models.CharField(max_length=150)
    内容简介 = RichTextField(null=True,blank=True,max_length=300,default="暂无内容简介")
    作者简介 = RichTextField(null=True,blank=True,max_length=300,default="暂无作者简介")
    目录 = RichTextField(null=True,blank=True,default="暂无")
    前言 = RichTextField(null=True,blank=True,default="暂无")
    ISBN = models.CharField(max_length=30,null=True,blank=True,default="暂无")
    作者 = models.CharField(max_length=200,null=True,blank=True,default="暂无")
    出版社 = models.CharField(max_length=200,null=True,blank=True,default="暂无")
    出版年 = models.DateField(null=True,blank=True,default="暂无")
    定价 =  models.CharField(max_length=10,null=True,blank=True,default="暂无")
    页数 =  models.IntegerField(null=True,blank=True)
    装帧 = models.CharField(max_length=20,null=True,blank=True,default="暂无")
    图片 = ImageField(upload_to='images/shuxun/',blank=True,null=True)
    更新时间 = models.DateTimeField(auto_now=True)
    发布状态 = models.BooleanField(default=False)
    def __str__(self):
        return self.标题

class 书评(models.Model):
    标题 = models.CharField(max_length=150)
    书籍作者 =models.CharField(max_length=200,null=True,blank=True)
    书籍出版日期 = models.DateField(null=True,blank=True)
    书评内容 = RichTextField()
    更新时间 = models.DateTimeField(auto_now=True)
    书评作者 = models.CharField(max_length=200,null=True,blank=True)
    图片 = ImageField(upload_to='images/shuping/',blank=True,null=True)
    发布状态 = models.BooleanField(default=False)

    def __str__(self):
        return self.标题

class 评论_书评(models.Model):
    书评 = models.ForeignKey(书评,on_delete=models.CASCADE)
    评论 = models.CharField(max_length=200)
    通过 = models.CharField(max_length=100,default='审查中')
    发布时间 = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.评论

class 观点(models.Model):
    标题 = models.CharField(max_length=150)
    内容 = RichTextField(blank=True,null=True)
    更新时间 = models.DateTimeField(auto_now=True)
    作者 = models.CharField(max_length=200, null=True,blank=True)
    图片 = ImageField(upload_to='images/guandian/',blank=True,null=True)
    发布状态 = models.BooleanField(default=False)

    def __str__(self):
        return self.标题

class 评论_观点(models.Model):
    观点 = models.ForeignKey(观点,on_delete=models.CASCADE)
    评论 = models.CharField(max_length=200)
    通过 = models.CharField(max_length=100,default='审查中')
    发布时间 = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.评论

class 文艺(models.Model):
    标题 = models.CharField(max_length=150)
    内容 = RichTextField(blank=True,null=True)
    更新时间 = models.DateTimeField(auto_now=True)
    作者 = models.CharField(max_length=200,  null=True,blank=True)
    图片 = ImageField(upload_to='images/wenyi/',blank=True,null=True)
    发布状态 = models.BooleanField(default=False)
    def __str__(self):
        return self.标题

class 评论_文艺(models.Model):
    文艺 = models.ForeignKey(文艺,on_delete=models.CASCADE)
    评论 = models.CharField(max_length=200)
    通过 = models.CharField(max_length=100, default='审查中')
    发布时间 = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.评论


class 视频(models.Model):
    标题 = models.CharField(max_length=150)
    视频文件 = models.FileField(upload_to='videos/',blank=True,null=True)
    发布状态 = models.BooleanField(default=False)
    更新时间 = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.标题

class 评论_视频(models.Model):
    视频 = models.ForeignKey(视频,on_delete=models.CASCADE)
    评论 = models.CharField(max_length=200)
    通过 = models.CharField(max_length=100, default='审查中')
    发布时间 = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.评论

class 问答(models.Model):
    标题 = models.CharField(max_length=150)
    答案 = RichTextField(blank=True)
    序号 = models.CharField(max_length=4,blank=True)
    参考问答 = models.BooleanField(default=False)
    参考问答项目= models.ForeignKey('self',null=True,blank=True,default=None,on_delete=models.CASCADE)
    更新时间 = models.DateTimeField(auto_now=True)
    发布状态 = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if(self.参考问答==True):
            self.答案=''
        super().save(*args, **kwargs)
        self.序号='{0:04d}'.format(self.id)
        super().save(*args, **kwargs)

    def __str__(self):
        title = self.序号 +" - "+ self.标题 +"\n" +self.答案
        return title

class 提问_问答(models.Model):
    标题 = models.CharField(max_length=150)
    通过 = models.BooleanField(default=False)
    发布时间 = models.DateTimeField(auto_now=True)

class 评论_问答(models.Model):
    问答 = models.ForeignKey(问答,on_delete=models.CASCADE)
    评论 = models.CharField(max_length=200)
    通过 = models.CharField(max_length=100, default='审查中')
    发布时间 = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.评论

class 译林(models.Model):
    标题 = models.CharField(max_length=150)
    译文作者 = models.CharField(max_length=100, null=True, blank=True)
    更新时间 = models.DateTimeField(auto_now=True)
    原文标题 = models.CharField(max_length=150)
    译文内容 = RichTextField(blank=True,null=True)
    原文作者 = models.CharField(max_length=100, null=True, blank=True)
    原文出版日期 = models.DateField(null=True,blank=True)
    图片 = ImageField(upload_to='images/yiling/', blank=True, null=True)
    发布状态 = models.BooleanField(default=False)

class 文史(models.Model):
    标题 = models.CharField(max_length=150)
    内容 = RichTextField(blank=True, null=True)
    更新时间 = models.DateTimeField(auto_now=True)
    作者 = models.CharField(max_length=200, null=True, blank=True)
    图片 = ImageField(upload_to='images/wenshi/', blank=True, null=True)
    资源 = models.CharField(max_length=200, null=True, blank=True)
    发布状态 = models.BooleanField(default=False)
    def __str__(self):
        return self.标题
    
class 评论_文史(models.Model):
    文史 = models.ForeignKey(文史, on_delete=models.CASCADE)
    评论 = models.CharField(max_length=200)
    通过 = models.CharField(max_length=100, default='审查中')
    发布时间 = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.评论


class 论文(models.Model):
    标题 = models.CharField(max_length=150)
    作者 = models.CharField(max_length=200, null=True, blank=True)
    更新时间 = models.DateTimeField(auto_now=True)
    文档 = models.FileField(upload_to='pdf/lunwen/', default='null', null=True)
    发布状态 = models.BooleanField(default=False)

class 经训(models.Model):
    标题 = models.CharField(max_length=150)
    图片 = ImageField(upload_to='images/jingxun/', blank=True, null=True)

    更新时间 = models.DateTimeField(auto_now=True)
    发布状态 = models.BooleanField(default=False)

class 章节_经训(models.Model):
    经训 = models.ForeignKey(经训, on_delete=models.CASCADE)
    章节 = models.CharField(max_length=150)
    内容 = RichTextField()

class 古籍(models.Model):
    标题 = models.CharField(max_length=150)
    作者 = models.CharField(max_length=200, null=True, blank=True)
    更新时间 = models.DateTimeField(auto_now=True)
    文档 = models.FileField(upload_to='pdf/guji/')
    发布状态 = models.BooleanField(default=False)

class 书库(models.Model):
    标题 = models.CharField(max_length=150)
    作者 = models.CharField(max_length=200, null=True, blank=True)
    更新时间 = models.DateTimeField(auto_now=True)
    文档 = models.FileField(upload_to='pdf/shuku/')
    作者简介 =  RichTextField(null=True,blank=True,default="暂无")
    内容简介 =  RichTextField(null=True,blank=True,default="暂无")
    出版日期 = models.DateField(null=True,blank=True,default="暂无")
    图片 = ImageField(upload_to='images/shuku/', default='null', null=True)
    ISBN = models.CharField(max_length=30)
    发布状态 = models.BooleanField(default=False)


class Contact(models.Model):
    邮箱 = models.EmailField(null=False, blank=False)
    主题 = models.CharField(max_length=255)
    内容 = models.TextField(null=False, blank=False)
    def __str__(self):
        return self.邮箱
