from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
<<<<<<< HEAD
from .forms import 通讯_add_form,译林_add_form,文摘_add_form,论文_add_form,经训_add_form,古籍_add_form,书库_add_form
=======
from .forms import 通讯_add_form
from .forms import 书讯_add_form
>>>>>>> 5e35798edac67f9864d89dc1f29f7f793969771c
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

<<<<<<< HEAD
def shuxun(request):
    content_title='shuxun'
    context={
        'all_书讯':书讯.objects.all(),
        'content_title':content_title,
        'task':'content'
    }
    return render(request,'admin/书讯.html',context)

def shuping(request,task):
    content_title='shuping'
    context={
        'all_书评':书评.objects.all(),
        'content_title':content_title,
        'task':task
    }
    return render(request,'admin/书评.html',context)

def yiling(request):
    context ={
        'all_译林': 译林.objects.all(),
        'content_title':'yiling',
        'task':'content'
    }
    return render(request,'admin/译林.html', context)

def wenzhai(request,task):
    content_title='wenzhai'
    context={
        'all_文摘':文摘.objects.all(),
        'content_title':content_title,
        'task':task
    }
    return render(request,'admin/文摘.html',context)

def lunwen(request):
    context ={
        'all_论文': 论文.objects.all(),
        'content_title':'lunwen',
        'task':'content'
    }
    return render(request,'admin/论文.html', context)

def delete_lunwen(request, lunwen_id):
    try:
        lunwen = 论文.objects.get(id=lunwen_id)
        lunwen.delete()
        return redirect('admin_task:论文')
    except 论文.DoesNotExist:
        return redirect('admin_task:论文')

def edit_lunwen(request, lunwen_id):
    lunwen = get_object_or_404(论文, id=lunwen_id)

    if request.method == 'POST':
        form = 论文_add_form(request.POST, request.FILES, instance=lunwen)
        if form.is_valid():
            # 如果表单有效，保存编辑后的论文
            form.save()
            return redirect('admin_task:论文')  # 重定向到论文列表页面
    else:
        form = 论文_add_form(instance=lunwen)  # 使用现有的论文对象填充表单

    context = {
        'form': form,
        'content_title': 'lunwen',
        'task': 'content',
    }
    return render(request, 'admin/论文_edit.html', context)



def jingxun(request):
    context ={
        'all_经训': 经训.objects.all(),
        'content_title':'jingxun',
        'task':'content'
    }
    return render(request,'admin/经训.html', context)

def guji(request):
    context ={
        'all_古籍': 古籍.objects.all(),
        'content_title':'guji',
        'task':'content'
    }
    return render(request,'admin/古籍.html', context)

def shuku(request):
    context ={
        'all_书库': 书库.objects.all(),
        'content_title':'shuku',
        'task':'content'
    }
    return render(request,'admin/书库.html', context)

class addShuKuView(generic.TemplateView):
    template_name='admin/书库_add.html'

    def get(self,request):
        form = 书库_add_form()
        书库_all = 书库.objects.all()
        args={
            'form':form,
            '书库_all':书库_all,
            'content_title': 'shuku',
            'task': 'content'
        }
        return render(request,self.template_name,args)

    def post(self,request):
        action = request.POST.get('submit-type')
        form=书库_add_form(request.POST,request.FILES)
        if form.is_valid():
            shukuForm = form.save(commit=False)
            if action=='save':
                shukuForm.发布状态 = False
            else:
                shukuForm.发布状态 = True
            form.save()
            标题 = form.cleaned_data['标题']
            文档 = form.cleaned_data['文档']
            作者 = form.cleaned_data['作者']
            args={
                'form':form,
                '标题':标题,
                '文档' : 文档,
                '作者' : 作者,
          
            }
            messages.success(request, '书库添加成功！')
            return HttpResponseRedirect(reverse('admin_task:书库'))
        else:
            messages.error(request, '书库添加失败请检查填表！')
            return render(request, 'admin/书库_add.html', {'form': form,'content_title': 'shuku','task': 'content'})


class addGuJiView(generic.TemplateView):
    template_name='admin/古籍_add.html'

    def get(self,request):
        form = 古籍_add_form()
        古籍_all = 古籍.objects.all()
        args={
            'form':form,
            '古籍_all':古籍_all,
            'content_title': 'guji',
            'task': 'content'
        }
        return render(request,self.template_name,args)

    def post(self,request):
        action = request.POST.get('submit-type')
        form=古籍_add_form(request.POST,request.FILES)
        if form.is_valid():
            gujiForm = form.save(commit=False)
            if action=='save':
                gujiForm.发布状态 = False
            else:
                gujiForm.发布状态 = True
            form.save()
            标题 = form.cleaned_data['标题']
            文档 = form.cleaned_data['文档']
            作者 = form.cleaned_data['作者']
            args={
                'form':form,
                '标题':标题,
                '文档' : 文档,
                '作者' : 作者,
          
            }
            messages.success(request, '古籍添加成功！')
            return HttpResponseRedirect(reverse('admin_task:古籍'))
        else:
            messages.error(request, '古籍添加失败请检查填表！')
            return render(request, 'admin/古籍_add.html', {'form': form,'content_title': 'guji','task': 'content'})


class addJingXunView(generic.TemplateView):
    template_name='admin/经训_add.html'

    def get(self,request):
        form = 经训_add_form()
        经训_all = 经训.objects.all()
        args={
            'form':form,
            '经训_all':经训_all,
            'content_title': 'jingxun',
            'task': 'content'
        }
        return render(request,self.template_name,args)

    def post(self,request):
        action = request.POST.get('submit-type')
        form=经训_add_form(request.POST,request.FILES)
        if form.is_valid():
            jingxunForm = form.save(commit=False)
            if action=='save':
                jingxunForm.发布状态 = False
            else:
                jingxunForm.发布状态 = True
            form.save()
            标题 = form.cleaned_data['标题']
            章节 = form.cleaned_data['章节']
            内容 = form.cleaned_data['内容']
            args={
                'form':form,
                '标题':标题,
                '章节' : 章节,
                '内容' : 内容,
            }
            messages.success(request, '经训添加成功！')
            return HttpResponseRedirect(reverse('admin_task:经训'))
        else:
            messages.error(request, '经训添加失败请检查填表！')
            return render(request, 'admin/经训_add.html', {'form': form,'content_title': 'jingxun','task': 'content'})



class addLunWenView(generic.TemplateView):
    template_name='admin/论文_add.html'

    def get(self,request):
        form = 论文_add_form()
        论文_all = 论文.objects.all()
        args={
            'form':form,
            '论文_all':论文_all,
            'content_title': 'lunwen',
            'task': 'content'
        }
        return render(request,self.template_name,args)
    
    def post(self,request):
        action = request.POST.get('submit-type')
        form= 论文_add_form(request.POST,request.FILES)
        if form.is_valid():
            lunwenForm = form.save(commit=False)
            if action=='save':
                lunwenForm.发布状态 = False
            else:
                lunwenForm.发布状态 = True
            form.save()
            标题 = form.cleaned_data['标题']
            文档 = form.cleaned_data['文档']
            作者 = form.cleaned_data['作者']
            args={
                'form':form,
                '标题':标题,
                '文档' : 文档,
                '作者' : 作者,
            }
            messages.success(request, '论文添加成功！')
            return HttpResponseRedirect(reverse('admin_task:论文'))
        else:
            messages.error(request, '论文添加失败请检查填表！')
            return render(request, 'admin/论文_add.html', {'form': form,'content_title': 'lunwen','task': 'content'})

class addWenZhaiView(generic.TemplateView):
    template_name='admin/文摘_add.html'

    def get(self,request):
        form = 文摘_add_form()
        文摘_all = 文摘.objects.all()
        args={
            'form':form,
            '文摘_all':文摘_all,
            'content_title': 'wenzhai',
            'task': 'content'
        }
        return render(request,self.template_name,args)
    
    def post(self,request):
        action = request.POST.get('submit-type')
        form= 文摘_add_form(request.POST,request.FILES)
        if form.is_valid():
            wenzhaiForm = form.save(commit=False)
            if action=='save':
                wenzhaiForm.发布状态 = False
            else:
                wenzhaiForm.发布状态 = True
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
            messages.success(request, '文摘添加成功！')
            return HttpResponseRedirect(reverse('admin_task:文摘'))
        else:
            messages.error(request, '文摘添加失败请检查填表！')
            return render(request, 'admin/文摘_add.html', {'form': form,'content_title': 'yiling','task': 'content'})

class addYiLingView(generic.TemplateView):
    template_name='admin/译林_add.html'

    def get(self,request):
        form = 译林_add_form()
        译林_all = 译林.objects.all()
        args={
            'form':form,
            '译林_all':译林_all,
            'content_title': 'yiling',
            'task': 'content'
        }
        return render(request,self.template_name,args)
    
    def post(self,request):
        action = request.POST.get('submit-type')
        form= 译林_add_form(request.POST,request.FILES)
        if form.is_valid():
            yilingForm = form.save(commit=False)
            if action=='save':
                yilingForm.发布状态 = False
            else:
                yilingForm.发布状态 = True
            form.save()
            译文标题 = form.cleaned_data['译文标题']
            原文内容 = form.cleaned_data['原文内容']
            译文作者 = form.cleaned_data['译文作者']
            原文作者 = form.cleaned_data['原文作者']
            图片 = form.cleaned_data['图片']
            args={
                'form':form,
                '译文标题':译文标题,
                '原文内容' : 原文内容,
                '译文作者' : 译文作者,
                '原文作者' : 原文作者,
                '图片' : 图片
            }
            messages.success(request, '译林添加成功！')
            return HttpResponseRedirect(reverse('admin_task:译林'))
        else:
            messages.error(request, '译林添加失败请检查填表！')
            return render(request, 'admin/译林_add.html', {'form': form,'content_title': 'yiling','task': 'content'})
        
    
class addTongXunView(generic.TemplateView):
=======
class TongXunAddView(generic.TemplateView):
>>>>>>> 5e35798edac67f9864d89dc1f29f7f793969771c
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


