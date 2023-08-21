from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from home.models import 通讯, 书讯, 书评, 观点, 文艺, 问答, 视频, 译林, 文摘, 论文, 经训, 古籍, 书库, 章节_经训, 提问_问答
from .forms import 视频_comment_form,问答_comment_form,书评_comment_form,观点_comment_form,文艺_comment_form,文摘_comment_form
from django.contrib import messages
from django.db.models import Count,Q

# Create your views here.


def MainView(request):
    context ={
        'all_通讯':通讯.objects.all().filter(发布状态=True).order_by("-更新时间")[:10],
        'all_书讯': 书讯.objects.all().filter(发布状态=True).order_by("-更新时间")[:4],
        'all_书评': 书评.objects.all().filter(发布状态=True).order_by("-更新时间")[:4],
        'all_观点': 观点.objects.all().filter(发布状态=True).order_by("-更新时间")[:4],
        'all_文艺': 文艺.objects.all().filter(发布状态=True).order_by("-更新时间")[:4],
        'all_问答': 问答.objects.all().filter(发布状态=True).order_by("-更新时间")[:5],
        'all_视频': 视频.objects.all().filter(发布状态=True).order_by("-更新时间")[:4],
        'all_论文': 论文.objects.all().filter(发布状态=True).order_by("-更新时间")[:3],
        'all_古籍': 古籍.objects.all().filter(发布状态=True).order_by("-更新时间")[:3],
        'all_书库': 书库.objects.all().filter(发布状态=True).order_by("-更新时间")[:3],
        'all_译林': 译林.objects.all().filter(发布状态=True).order_by("-更新时间")[:4],
        'all_文摘': 文摘.objects.all().filter(发布状态=True).order_by("-更新时间")[:4],
        'all_经训': 经训.objects.all().filter(发布状态=True).order_by("-更新时间")[:4],
    }
    return render(request,'frontend/首页/index.html',context)

def TongXun(request):
    all_通讯 = 通讯.objects.all().filter(发布状态=True)
    context = {
        'all_通讯': all_通讯,
    }
    return render(request, 'frontend/通讯/main.html', context)

def TongXunDetail(request,tongxun_id):
    tongxun = 通讯.objects.all().get(id=tongxun_id)
    all_通讯 = 通讯.objects.all().filter(发布状态=True).exclude(id=tongxun_id)[:5]
    context = {
        'all_通讯': all_通讯,
        'tongxun': tongxun
    }
    return render(request, 'frontend/通讯/detail.html', context)

def ShuXun(request):
    all_书讯 = 书讯.objects.all().filter(发布状态=True)
    context = {
        'all_书讯': all_书讯,
    }
    return render(request, 'frontend/书讯/main.html', context)

def ShuXunDetail(request,shuxun_id):
    shuxun = 书讯.objects.all().get(id=shuxun_id)
    all_书讯 = 书讯.objects.all().filter(发布状态=True).exclude(id=shuxun_id)[:5]
    context = {
        'all_书讯': all_书讯,
        'shuxun': shuxun
    }
    return render(request, 'frontend/书讯/detail.html', context)

def ShuPing(request):
    all_书评 = 书评.objects.all().filter(发布状态=True)
    context = {
        'all_书评': all_书评,
    }
    return render(request, 'frontend/书评/main.html', context)

class ShuPingDetail(generic.TemplateView):
    template_name = "frontend/书评/detail.html"
    def get(self,request,shuping_id):
        shuping = 书评.objects.all().get(id=shuping_id)
        all_书评 = 书评.objects.all().filter(发布状态=True).exclude(id=shuping_id)[:5]
        form = 书评_comment_form
        comments = shuping.评论_书评_set.filter(通过='已通过')
        context = {
            'all_书评': all_书评,
            'shuping': shuping,
            'form':form,
            'comments':comments
        }
        return render(request, self.template_name, context)

    def post(self,request,shuping_id):
        form = 书评_comment_form(request.POST)
        if form.is_valid():
            commentForm = form.save(commit=False)
            commentForm.书评 = 书评.objects.get(id=shuping_id)
            commentForm.save()
            comment = form.cleaned_data['评论']
            args = {
                'form': form,
                'comment': comment
            }
            msg = '评论已提交，待审核'
            messages.success(request, msg)
            return HttpResponseRedirect(reverse('home:shupingdetail', kwargs={'shuping_id': shuping_id}))

def GuanDian(request):
    all_观点 = 观点.objects.all().filter(发布状态=True)
    context = {
        'all_观点': all_观点,
    }
    return render(request, 'frontend/观点/main.html', context)

class GuanDianDetail(generic.TemplateView):
    template_name = "frontend/观点/detail.html"

    def get(self, request, guandian_id):
        form = 观点_comment_form
        all_观点 = 观点.objects.all().filter(发布状态=True).exclude(id=guandian_id).annotate(comment_no=Count("评论_观点", filter=Q(评论_观点__通过='已通过')))[:5]
        guandian = 观点.objects.get(id=guandian_id)
        comments = guandian.评论_观点_set.filter(通过='已通过')
        context = {
            'all_观点': all_观点,
            'guandian':guandian,
            'form':form,
            'comments':comments
        }
        return render(request, self.template_name, context)

    def post(self,request,guandian_id):
        form = 观点_comment_form(request.POST)
        if form.is_valid():
            commentForm = form.save(commit=False)
            commentForm.观点 = 观点.objects.get(id=guandian_id)
            commentForm.save()
            comment = form.cleaned_data['评论']
            args = {
                'form': form,
                'comment': comment
            }
            msg = '评论已提交，待审核'
            messages.success(request, msg)
            return HttpResponseRedirect(reverse('home:guandiandetail', kwargs={'guandian_id': guandian_id}))
def WenYi(request):
    all_文艺 = 文艺.objects.all().filter(发布状态=True)
    context = {
        'all_文艺': all_文艺,
    }
    return render(request, 'frontend/文艺/main.html', context)



class WenYiDetail(generic.TemplateView):
    template_name = "frontend/文艺/detail.html"

    def get(self, request, wenyi_id):
        form = 文艺_comment_form
        all_文艺 = 文艺.objects.all().filter(发布状态=True).exclude(id=wenyi_id).annotate(comment_no=Count("评论_文艺",filter=Q(评论_文艺__通过='已通过')))[:5]
        wenyi = 文艺.objects.get(id=wenyi_id)
        comments = wenyi.评论_文艺_set.filter(通过='已通过')
        context = {
            'all_文艺': all_文艺,
            'wenyi':wenyi,
            'form':form,
            'comments':comments
        }
        return render(request, self.template_name, context)

    def post(self,request,wenyi_id):
        form = 文艺_comment_form(request.POST)
        if form.is_valid():
            commentForm = form.save(commit=False)
            commentForm.文艺 = 文艺.objects.get(id=wenyi_id)
            commentForm.save()
            comment = form.cleaned_data['评论']
            args = {
                'form': form,
                'comment': comment
            }
            msg = '评论已提交，待审核'
            messages.success(request, msg)
            return HttpResponseRedirect(reverse('home:wenyidetail', kwargs={'wenyi_id': wenyi_id}))

def ShiPing(request):
    all_视频 = 视频.objects.all().filter(发布状态=True).annotate(comment_no=Count("评论_视频",filter=Q(评论_视频__通过='已通过')))
    context = {
        'all_视频': all_视频,
    }
    return render(request, 'frontend/视频/main.html', context)

class ShiPingDetail(generic.TemplateView):
    template_name = "frontend/视频/detail.html"

    def get(self, request, shiping_id):
        form = 视频_comment_form
        all_视频 = 视频.objects.all().filter(发布状态=True).annotate(comment_no=Count("评论_视频",filter=Q(评论_视频__通过='已通过')))
        shiping = 视频.objects.get(id=shiping_id)
        comments = shiping.评论_视频_set.filter(通过='已通过')
        context = {
            'all_视频': all_视频,
            'shiping':shiping,
            'form':form,
            'comments':comments
        }
        return render(request, self.template_name, context)

    def post(self,request,shiping_id):
        form = 视频_comment_form(request.POST)
        if form.is_valid():
            commentForm = form.save(commit=False)
            commentForm.视频 = 视频.objects.get(id=shiping_id)
            commentForm.save()
            comment = form.cleaned_data['评论']
            args = {
                'form': form,
                'comment': comment
            }
            msg = '评论已提交，待审核'
            messages.success(request, msg)
            return HttpResponseRedirect(reverse('home:shipingdetail', kwargs={'shiping_id': shiping_id}))

def WenDa(request):
    all_问答 = 问答.objects.all().filter(发布状态=True).annotate(comment_no=Count("评论_问答",filter=Q(评论_问答__通过='已通过')))
    context = {
        'all_问答': all_问答,
    }
    return render(request, 'frontend/问答/main.html', context)

def WenDaSearch(request):
    keyword=request.GET.get('keyword')
    all_问答 = 问答.objects.all().filter(标题__icontains=keyword).filter(发布状态=True).annotate(comment_no=Count("评论_问答",filter=Q(评论_问答__通过='已通过')))
    context = {
        'all_问答': all_问答,
        'keyword':keyword
    }
    return render(request, 'frontend/问答/main.html', context)

def WenDaAddQuestion(request):
    if request.method=='POST':
        new_question = 提问_问答(标题=request.POST.get('question'))
        new_question.save()
        msg = '新提问已提交，待审核'
        messages.success(request, msg)
        return HttpResponseRedirect(reverse('home:wenda'))

class WenDaDetail(generic.TemplateView):
    template_name = "frontend/问答/detail.html"

    def get(self, request, wenda_id):
        form = 问答_comment_form
        all_问答 = 问答.objects.all().exclude(id=wenda_id).filter(发布状态=True).annotate(comment_no=Count("评论_问答",filter=Q(评论_问答__通过='已通过')))[:5]
        wenda = 问答.objects.get(id=wenda_id)
        comments = wenda.评论_问答_set.filter(通过='已通过')
        context = {
            'all_问答': all_问答,
            'wenda': wenda,
            'form': form,
            'comments': comments
        }
        return render(request, self.template_name, context)

    def post(self, request, wenda_id):
        form = 问答_comment_form(request.POST)
        if form.is_valid():
            commentForm = form.save(commit=False)
            commentForm.问答 = 问答.objects.get(id=wenda_id)
            commentForm.save()
            comment = form.cleaned_data['评论']
            args = {
                'form': form,
                'comment': comment
            }
            msg = '评论已提交，待审核'
            messages.success(request, msg)
            return HttpResponseRedirect(reverse('home:wendadetail', kwargs={'wenda_id': wenda_id}))

def JingXun(request):
    all_经训 = 经训.objects.all().filter(发布状态=True)
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
    all_书库 = 书库.objects.all().filter(发布状态=True)
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
    all_古籍 = 古籍.objects.all().filter(发布状态=True)
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
    all_论文 = 论文.objects.all().filter(发布状态=True)
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
    all_译林 = 译林.objects.all().filter(发布状态=True)
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


def WenZhai(request):
    all_文摘 = 文摘.objects.all().filter(发布状态=True)
    context = {
        'all_文摘': all_文摘,
    }
    return render(request, 'frontend/文摘/main.html', context)

class WenZhaiDetail(generic.TemplateView):
    template_name = "frontend/文摘/detail.html"

    def get(self, request, wenzhai_id):
        form = 文摘_comment_form
        all_文摘 = 文摘.objects.all().filter(发布状态=True).exclude(id=wenzhai_id).annotate(comment_no=Count("评论_文摘",filter=Q(评论_文摘__通过='已通过')))[:5]
        wenzhai = 文摘.objects.get(id=wenzhai_id)
        comments = wenzhai.评论_文摘_set.filter(通过='已通过')
        context = {
            'all_文艺': all_文摘,
            'wenzhai':wenzhai,
            'form':form,
            'comments':comments
        }
        return render(request, self.template_name, context)

    def post(self,request,wenzhai_id):
        form = 文摘_comment_form(request.POST)
        if form.is_valid():
            commentForm = form.save(commit=False)
            commentForm.文摘 = 文摘.objects.get(id=wenzhai_id)
            commentForm.save()
            comment = form.cleaned_data['评论']
            args = {
                'form': form,
                'comment': comment
            }
            msg = '评论已提交，待审核'
            messages.success(request, msg)
            return HttpResponseRedirect(reverse('home:wenzhaidetail', kwargs={'wenzhai_id': wenzhai_id}))