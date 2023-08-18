from django.shortcuts import render,get_object_or_404
from django.utils import timezone

from home.models import 通讯, 书讯, 书评, 观点, 文艺, 问答, 视频, 译林, 文摘, 论文, 经训, 古籍, 书库, 章节_经训

# Create your views here.


def MainView(request):
    context ={
        'all_通讯':通讯.objects.all().order_by("-更新时间")[:10],
        'all_书讯': 书讯.objects.all().order_by("-更新时间")[:4],
        'all_书评': 书评.objects.all().order_by("-更新时间")[:4],
        'all_观点': 观点.objects.all().order_by("-更新时间")[:4],
        'all_文艺': 文艺.objects.all().order_by("-更新时间")[:4],
        'all_问答': 问答.objects.all().order_by("-更新时间")[:5],
        'all_视频': 视频.objects.all().order_by("-更新时间")[:4],
        'all_论文': 论文.objects.all().order_by("-更新时间")[:3],
        'all_古籍': 古籍.objects.all().order_by("-更新时间")[:3],
        'all_书库': 书库.objects.all().order_by("-更新时间")[:3],
        'all_译林': 译林.objects.all().order_by("-更新时间")[:4],
        'all_文摘': 文摘.objects.all().order_by("-更新时间")[:4],
        'all_经训': 经训.objects.all().order_by("-更新时间")[:4],
    }
    return render(request,'frontend/首页/index.html',context)

def ShiPing(request):
    all_视频 = 视频.objects.all()
    context = {
        'all_视频': all_视频,
    }
    return render(request, 'frontend/视频/main.html', context)

def JingXun(request):
    all_经训 = 经训.objects.all()
    context = {
        'all_经训': all_经训,
        'content_title': 'jingxun',
        'task': 'content'
    }
    return render(request, 'frontend/经训/main.html', context)

def show_all_chapters(request, 经训_id):
    经训_instance = 经训.objects.get(pk=经训_id)
    章节_list = 章节_经训.objects.filter(经训=经训_instance)
    context = {
        '经训': 经训_instance,
        '章节_list': 章节_list,
    }
    return render(request, 'frontend/经训/all_chapter.html', context)

def JingXuncontent(request, 章节_id):
    章节 = 章节_经训.objects.get(id=章节_id)
    all_经训 = 经训.objects.all()
    context = {
        '章节': 章节,
        'all_经训': all_经训,
    }
    return render(request, 'frontend/经训/content.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    经训_results = []
    章节_results = []
    if keyword:
        经训_results = 经训.objects.filter(标题__icontains=keyword)
        章节_results = 章节_经训.objects.filter(内容__icontains=keyword)
        all_经训 = 经训.objects.all()
        context = {
        '经训_results': 经训_results,
        '章节_results': 章节_results,
        'keyword': keyword,
        'all_经训': all_经训,  # 将经训数据传递给模板
    }
    return render(request, 'frontend/经训/search_results.html', context)


def ShuKu(request):
    all_书库 = 书库.objects.all()
    context = {
        'all_书库': all_书库,
        'content_title': 'shuku',
        'task': 'content'
    }
    return render(request, 'frontend/书库/main.html', context)

def ShuKucontent(request, shuku_id):
    shuku = 书库.objects.get(id=shuku_id)
    all_书库 = 书库.objects.all()
    context = {
        'shuku': shuku,
        'all_书库': all_书库,
    }
    return render(request, 'frontend/书库/detail.html', context)


def GuJi(request):
    all_古籍 = 古籍.objects.all()
    context = {
        'all_古籍': all_古籍,
        'content_title': 'guji',
        'task': 'content'
    }
    return render(request, 'frontend/古籍/main.html', context)

def GuJicontent(request, guji_id):
    guji = 古籍.objects.get(id=guji_id)
    all_古籍 = 古籍.objects.all()
    context = {
        'guji': guji,
        'all_古籍': all_古籍,
    }
    return render(request, 'frontend/古籍/detail.html', context)

def LunWen(request):
    all_论文 = 论文.objects.all()
    context = {
        'all_论文': all_论文,
        'content_title': 'lunwen',
        'task': 'content'
    }
    return render(request, 'frontend/论文/main.html', context)

def LunWencontent(request, lunwen_id):
    lunwen = 论文.objects.get(id=lunwen_id)
    all_论文 = 论文.objects.all()
    context = {
        'lunwen': lunwen,
        'all_论文':all_论文
    }
    return render(request, 'frontend/论文/detail.html', context)

def YiLing(request):
    all_译林 = 译林.objects.all()
    context = {
        'all_译林': all_译林,
        'content_title': 'lunwen',
        'task': 'content'
    }
    return render(request, 'frontend/译林/main.html', context)

def YiLingcontent(request, yiling_id):
    yiling = 译林.objects.get(id=yiling_id)
    all_译林 = 译林.objects.all()
    context = {
        'yiling': yiling,
        'all_译林':all_译林
    }
    return render(request, 'frontend/译林/detail.html', context)