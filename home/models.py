from django.db import models

# Create your models here.
# 通讯
class 通讯(models.Model):
    标题 = models.CharField(max_length=150)
    内容 = models.TextField()
    更新时间 = models.DateTimeField(auto_now=True)
    发布状态 = models.BooleanField(default=False)
    资源 = models.CharField(max_length=200,null=True,blank=True)
    作者 = models.CharField(max_length=200,null=True,blank=True)
    图片 = models.ImageField(upload_to='images/tongxun/',blank=True,null=True)

    def __str__(self):
        return self.标题

class 书讯(models.Model):
    标题 = models.CharField(max_length=150)
    简介 = models.TextField()
    更新时间 = models.DateTimeField(auto_now=True)
    发布状态 = models.BooleanField(default=False)
    序号 = models.IntegerField(null=True,blank=True)
    作者 = models.CharField(max_length=200,null=True,blank=True)
    图片 = models.ImageField(upload_to='images/shuxun/',blank=True,null=True)
    def __str__(self):
        return self.标题

class 书评(models.Model):
    标题 = models.CharField(max_length=150)
    书籍作者 =models.CharField(max_length=200,null=True,blank=True)
    书籍出版日期 = models.DateField(null=True,blank=True)
    书评内容 = models.TextField()
    更新时间 = models.DateTimeField(auto_now=True)
    书评作者 = models.CharField(max_length=200,null=True,blank=True)
    图片 = models.ImageField(upload_to='images/shuping/',blank=True,null=True)
    发布状态 = models.BooleanField(default=False)

    def __str__(self):
        return self.标题

class 评论_书评(models.Model):
    书评 = models.ForeignKey(书评,on_delete=models.CASCADE)
    评论 = models.CharField(max_length=200)
    通过 = models.BooleanField(default=False)
    发布时间 = models.DateTimeField(auto_now=True)

class 观点(models.Model):
    标题 = models.CharField(max_length=150)
    内容 = models.TextField()
    更新时间 = models.DateTimeField(auto_now=True)
    作者 = models.CharField(max_length=200, null=True, default='null')
    图片 = models.ImageField(upload_to='', default='null', null=True)
    发布状态 = models.BooleanField(default=False)

class 评论_观点(models.Model):
    观点 = models.ForeignKey(观点,on_delete=models.CASCADE)
    评论 = models.CharField(max_length=200)
    通过 = models.BooleanField(default=False)
    发布时间 = models.DateTimeField(auto_now=True)

class 文艺(models.Model):
    标题 = models.CharField(max_length=150)
    内容 = models.TextField()
    更新时间 = models.DateTimeField(auto_now=True)
    作者 = models.CharField(max_length=200, null=True, default='null')
    图片 = models.ImageField(upload_to='', default='null', null=True)
    发布状态 = models.BooleanField(default=False)

class 评论_文艺(models.Model):
    文艺 = models.ForeignKey(文艺,on_delete=models.CASCADE)
    评论 = models.CharField(max_length=200)
    通过 = models.BooleanField(default=False)
    发布时间 = models.DateTimeField(auto_now=True)

class 问答(models.Model):
    标题 = models.CharField(max_length=150)
    答案 = models.TextField()
    序号 = models.IntegerField()
    更新时间 = models.DateTimeField(auto_now=True)
    发布状态 = models.BooleanField(default=False)

class 评论_问答(models.Model):
    问答 = models.ForeignKey(问答,on_delete=models.CASCADE)
    评论 = models.CharField(max_length=200)
    通过 = models.BooleanField(default=False)
    发布时间 = models.DateTimeField(auto_now=True)

class 译林(models.Model):
    标题 = models.CharField(max_length=150)
    译文作者 = models.CharField(max_length=100, null=True, blank=True)
    更新时间 = models.DateTimeField(auto_now=True)
    原文标题 = models.CharField(max_length=150)
    译文内容 = models.TextField()
    原文作者 = models.CharField(max_length=100, null=True, blank=True)
    原文出版日期 = models.DateField(null=True,blank=True)
    图片 = models.ImageField(upload_to='images/yiling/', blank=True, null=True)
    发布状态 = models.BooleanField(default=False)

class 文摘(models.Model):
    标题 = models.CharField(max_length=150)
    内容 = models.TextField()
    更新时间 = models.DateTimeField(auto_now=True)
    作者 = models.CharField(max_length=200, null=True, blank=True)
    图片 = models.ImageField(upload_to='images/wenzhai/', blank=True, null=True)
    资源 = models.CharField(max_length=200, null=True, blank=True)
    发布状态 = models.BooleanField(default=False)

class 评论_文摘(models.Model):
    文摘 = models.ForeignKey(文摘, on_delete=models.CASCADE)
    评论 = models.CharField(max_length=200)
    通过 = models.BooleanField(default=False)
    发布时间 = models.DateTimeField(auto_now=True)


class 论文(models.Model):
    标题 = models.CharField(max_length=150)
    作者 = models.CharField(max_length=200, null=True, blank=True)
    更新时间 = models.DateTimeField(auto_now=True)
    文档 = models.FileField(upload_to='pdf/lunwen/', default='null', null=True)
    发布状态 = models.BooleanField(default=False)

class 经训(models.Model):
    章节 = models.CharField(max_length=150)
    原文作者 = models.CharField(max_length=150)
    译文作者 = models.CharField(max_length=150)
    标题 = models.CharField(max_length=150)
    内容 = models.TextField()
    更新时间 = models.DateTimeField(auto_now=True)
    发布状态 = models.BooleanField(default=False)

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
    简介 = models.TextField()
    图片 = models.ImageField(upload_to='images/shuku/', default='null', null=True)
    序号 = models.IntegerField()
    发布状态 = models.BooleanField(default=False)