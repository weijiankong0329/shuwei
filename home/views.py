from django.shortcuts import render
from django.utils import timezone
from home.models import 通讯,书讯,书评,观点,文艺,问答,视频,译林,文摘,论文,经训,古籍,书库

# Create your views here.

def MainView(request):
    context ={
        'all_通讯':通讯.objects.all().order_by("-更新时间")[:10],
        'all_通讯': 书讯.objects.all().order_by("-更新时间")[:3],
        'all_通讯': 书评.objects.all().order_by("-更新时间")[:3],
        'all_通讯': 观点.objects.all().order_by("-更新时间")[:3],
        'all_通讯': 文艺.objects.all().order_by("-更新时间")[:3],
        'all_通讯': 问答.objects.all().order_by("-更新时间")[:3],
        'all_通讯': 视频.objects.all().order_by("-更新时间")[:4]
    }
    return render(request,'index.html',{'time': timezone.now})

def lunwen(request):
    context ={
        'all_论文': 论文.objects.all(),
        'content_title':'lunwen',
        'task':'content'
    }
    return render(request,'test.html', context)