from django.shortcuts import render
from django.utils import timezone

from home.models import 通讯,书讯,书评,观点,文艺,问答,视频,译林,文摘,论文,经训,古籍,书库,章节_经训

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

def jingxun(request):
    all_经训 = 经训.objects.all()
    context = {
        'all_经训': all_经训,
        'content_title': 'jingxun',
        'task': 'content'
    }

    return render(request, 'frontend/经训/经训.html', context)

def show_all_chapters(request, 经训_id):
    经训_instance = 经训.objects.get(pk=经训_id)
    章节_list = 章节_经训.objects.filter(经训=经训_instance)
    
    context = {
        '经训': 经训_instance,
        '章节_list': 章节_list,
    }
    
    return render(request, 'frontend/经训/all_chapter.html', context)



def content(request, 章节_id):
    章节 = 章节_经训.objects.get(id=章节_id)
    return render(request, 'frontend/经训/content.html', {'章节': 章节})




def search(request):
    keyword = request.GET.get('keyword')
    经训_results = []
    章节_results = []
    
    if keyword:
        经训_results = 经训.objects.filter(标题__icontains=keyword)
        章节_results = 章节_经训.objects.filter(内容__icontains=keyword)
    
    return render(request, 'frontend/经训/search_results.html', {'经训_results': 经训_results, '章节_results': 章节_results, 'keyword': keyword})

