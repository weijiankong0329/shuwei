from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
from .forms import 通讯_add_form
from .forms import 书讯_add_form
from home.models import 通讯
from home.models import 书讯
from home.models import 书评
from home.models import 观点
from home.models import 文艺
from home.models import 问答
from home.models import 译林
from home.models import 文摘
from home.models import 论文
from home.models import 经训
from home.models import 古籍
from home.models import 书库
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'admin/login.html'
    authentication_form = CustomLoginForm

def tasklist(request):
    context ={}
    return render(request,'admin/main.html', context)

def TongXunListView(request):
    通讯_list = 通讯.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(通讯_list,20)
    try:
        all_通讯=paginator.page(page)
    except PageNotAnInteger:
        all_通讯 = paginator.page(1)
    except EmptyPage:
        all_通讯 = paginator.page(paginator.num_pages)

    context ={
        'all_通讯': all_通讯,
        'content_title':'tongxun',
        'task':'content'
    }
    return render(request,'admin/通讯.html', context)

class TongXunAddView(generic.TemplateView):
    template_name='admin/通讯_add.html'

    def get(self,request):
        form = 通讯_add_form()
        通讯_all = 通讯.objects.all()
        args={
            'form':form,
            '通讯_all':通讯_all,
            'content_title': 'tongxun',
            'task': 'content'
        }
        return render(request,self.template_name,args)

    def post(self,request):
        action = request.POST.get('submit-type')
        form=通讯_add_form(request.POST,request.FILES)
        if form.is_valid():
            tongxunForm = form.save(commit=False)
            if action=='save':
                tongxunForm.发布状态 = False
            else:
                tongxunForm.发布状态 = True
            form.save()
            标题 = form.cleaned_data['标题']
            内容 = form.cleaned_data['内容']
            作者 = form.cleaned_data['作者']
            资源 = form.cleaned_data['资源']
            图片 = form.cleaned_data['图片']
            args={
                'form':form,
                '标题':标题,
                '内容' : 内容,
                '作者' : 作者,
                '资源' : 资源,
                '图片' : 图片
            }
            messages.success(request, '通讯添加成功！')
            return HttpResponseRedirect(reverse('admin_task:通讯'))
        else:
            messages.error(request, '通讯添加失败请检查填表！')
            return render(request, 'admin/通讯_add.html', {'form': form,'content_title': 'tongxun','task': 'content'})

def TongXunDetailView(request,pk):
    tongxun = 通讯.objects.get(id=pk)
    context = {
        '通讯': tongxun,
        'content_title': 'tongxun',
        'task': 'content'
    }
    return render(request,'admin/通讯_detail.html',context)

def TongXunDeleteView(request,pk):
    tongxun = 通讯.objects.get(id=pk)
    tongxun.delete()
    messages.success(request, '选中通讯已被删除')
    return HttpResponseRedirect(reverse('admin_task:通讯'))

class TongXunEditView(generic.TemplateView):
    template_name="admin/通讯_edit.html"

    def get(self,request,pk):
        tongxun = 通讯.objects.get(id=pk)
        form = 通讯_add_form(instance=tongxun)
        args={
            'form':form,
            '通讯':tongxun,
            'content_title': 'tongxun',
            'task': 'content'
        }
        return render(request,self.template_name,args)

    def post(self,request,pk):
        tongxun = 通讯.objects.get(id=pk)
        form = 通讯_add_form(request.POST, request.FILES, instance=tongxun)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, '通讯内容修改成功')
            return HttpResponseRedirect(reverse('admin_task:通讯_detail',kwargs={'pk':pk}))
        else:
            messages.error(request, '通讯内容修改错误，请更正错误后提交更改内容')
            return HttpResponseRedirect(reverse('admin_task:通讯_edit', kwargs={'pk':pk}))

def ShuXunListView(request):
    书讯_list = 书讯.objects.all().order_by('id')
    page = request.GET.get('page', 1)
    paginator = Paginator(书讯_list, 20)
    try:
        书讯_list = paginator.page(page)
    except PageNotAnInteger:
        书讯_list = paginator.page(1)
    except EmptyPage:
        书讯_list = paginator.page(paginator.num_pages)

    context = {
        'all_书讯': 书讯_list,
        'content_title': 'shuxun',
        'task': 'content'
    }
    return render(request, 'admin/书讯/书讯.html', context)

class ShuXunAddView(generic.TemplateView):
    template_name='admin/书讯/书讯_add.html'

    def get(self,request):
        form = 书讯_add_form()
        书讯_all = 书讯.objects.all()
        args={
            'form':form,
            '书讯_all':书讯_all,
            'content_title': 'shuxun',
            'task': 'content'
        }
        return render(request,self.template_name,args)

    def post(self,request):
        action = request.POST.get('submit-type')
        form = 书讯_add_form(request.POST,request.FILES)
        if form.is_valid():
            shuxunForm = form.save(commit=False)
            if action=='save':
                shuxunForm.发布状态 = False
            else:
                shuxunForm.发布状态 = True
            form.save()
            标题 = form.cleaned_data['标题']
            简介 = form.cleaned_data['简介']
            作者 = form.cleaned_data['作者']
            序号 = form.cleaned_data['序号']
            图片 = form.cleaned_data['图片']
            args={
                'form':form,
                '标题':标题,
                '简介' : 简介,
                '作者' : 作者,
                '序号' : 序号,
                '图片' : 图片
            }
            messages.success(request, '书讯添加成功！')
            return HttpResponseRedirect(reverse('admin_task:书讯'))
        else:
            messages.error(request, '书讯添加失败请检查填表！')
            return render(request, 'admin/书讯_add.html', {'form': form,'content_title': 'tongxun','task': 'content'})

def ShuXunDetailView(request,pk):
    shuxun = 书讯.objects.get(id=pk)
    context = {
        '书讯': shuxun,
        'content_title': 'shuxun',
        'task': 'content'
    }
    return render(request,'admin/书讯/书讯_detail.html',context)

def ShuXunDeleteView(request,pk):
    shuxun = 书讯.objects.get(id=pk)
    shuxun.delete()
    messages.success(request, '选中书讯已被删除')
    return HttpResponseRedirect(reverse('admin_task:书讯'))

class ShuXunEditView(generic.TemplateView):
    template_name="admin/书讯/书讯_edit.html"

    def get(self,request,pk):
        shuxun = 书讯.objects.get(id=pk)
        form = 书讯_add_form(instance=shuxun)
        args={
            'form':form,
            '书讯':shuxun,
            'content_title': 'shuxun',
            'task': 'content'
        }
        return render(request,self.template_name,args)

    def post(self,request,pk):
        shuxun = 书讯.objects.get(id=pk)
        form = 书讯_add_form(request.POST, request.FILES, instance=shuxun)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, '书讯内容修改成功')
            return HttpResponseRedirect(reverse('admin_task:书讯_detail',kwargs={'pk':pk}))
        else:
            context={
                'pk':pk,
                'form':form
            }
            messages.error(request, '书讯内容修改错误，请更正错误后提交更改内容')
            return render(request,self.template_name,context)

def shuping(request,task):
    content_title='shuping'
    context={
        'all_书评':书评.objects.all(),
        'content_title':content_title,
        'task':task
    }
    return render(request,'admin/书评.html',context)


