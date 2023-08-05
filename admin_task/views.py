from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
from .forms import 通讯_add_form,书讯_add_form,书评_add_form,译林_add_form,文摘_add_form,论文_add_form,古籍_add_form,经训_add_form,书库_add_form
from home.models import 通讯,书讯,书评,观点,文艺,问答,译林,文摘,论文,经训,古籍,书库
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.apps import apps


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'admin/login.html'
    authentication_form = CustomLoginForm


def tasklist(request):
    context = {}
    return render(request, 'admin/main.html', context)

def ContentItemList(request, content, task):
    model_name = apps.get_model('home', content)
    content_all_list = model_name.objects.all().order_by('id')
    page = request.GET.get('page', 1)
    paginator = Paginator(content_all_list, 20)
    try:
        all_content = paginator.page(page)
    except PageNotAnInteger:
        all_content = paginator.page(1)
    except EmptyPage:
        all_content = paginator.page(paginator.num_pages)

    context ={
        'all_content':all_content,
        'content_title': content,
        'task': task
    }

    return render(request, 'admin/content-item-list.html', context)

def ContentItemDeleteView(request, content, id):
    model_name = apps.get_model('home', content)
    delete_item = model_name.objects.get(id=id)
    delete_item.delete()
    msg='选中'+ content + '项目已被删除'
    messages.success(request, msg )
    return HttpResponseRedirect(reverse('admin_task:content-item',kwargs={'content':content,'task':'content'}))

def ContentItemDetailView(request, content, id):
    model_name = apps.get_model('home', content)
    content_item = model_name.objects.get(id=id)
    template_name = 'admin/'+content+'/'+content+'_detail.html'
    context={
        'content_item':content_item,
        'content_title' : content,
        'task':'content'
    }
    return render(request, template_name, context)

class TongXunAddView(generic.TemplateView):
    template_name = 'admin/通讯/通讯_add.html'

    def get(self, request):
        form = 通讯_add_form()
        通讯_all = 通讯.objects.all()
        args = {
            'form': form,
            '通讯_all': 通讯_all,
            'content_title': '通讯',
            'task': 'content'
        }
        return render(request, self.template_name, args)

    def post(self, request):
        action = request.POST.get('submit-type')
        form = 通讯_add_form(request.POST, request.FILES)
        if form.is_valid():
            tongxunForm = form.save(commit=False)
            if action == 'save':
                tongxunForm.发布状态 = False
            else:
                tongxunForm.发布状态 = True
            form.save()
            标题 = form.cleaned_data['标题']
            内容 = form.cleaned_data['内容']
            作者 = form.cleaned_data['作者']
            资源 = form.cleaned_data['资源']
            图片 = form.cleaned_data['图片']
            args = {
                'form': form,
                '标题': 标题,
                '内容': 内容,
                '作者': 作者,
                '资源': 资源,
                '图片': 图片
            }
            messages.success(request, '通讯添加成功！')
            return HttpResponseRedirect(reverse('admin_task:content-item',kwargs={'content' : '通讯','task' : 'content'}))
        else:
            messages.error(request, '通讯添加失败请检查填表！')
            return render(request, 'admin/通讯_add.html', {'form': form, 'content_title': '通讯', 'task': 'content'})

class TongXunEditView(generic.TemplateView):
    template_name = "admin/通讯/通讯_edit.html"

    def get(self, request, pk):
        tongxun = 通讯.objects.get(id=pk)
        form = 通讯_add_form(instance=tongxun)
        args = {
            'form': form,
            '通讯': tongxun,
            'content_title': '通讯',
            'task': 'content'
        }
        return render(request, self.template_name, args)

    def post(self, request, pk):
        tongxun = 通讯.objects.get(id=pk)
        form = 通讯_add_form(request.POST, request.FILES, instance=tongxun)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, '通讯内容修改成功')
            return HttpResponseRedirect(reverse('admin_task:content-item-detail', kwargs={'content':'通讯','id': pk}))
        else:
            messages.error(request, '通讯内容修改错误，请更正错误后提交更改内容')
            return HttpResponseRedirect(reverse('admin_task:通讯_edit', kwargs={'pk': pk}))

class ShuXunAddView(generic.TemplateView):
    template_name = 'admin/书讯/书讯_add.html'

    def get(self, request):
        form = 书讯_add_form()
        书讯_all = 书讯.objects.all()
        args = {
            'form': form,
            '书讯_all': 书讯_all,
            'content_title': '书讯',
            'task': 'content'
        }
        return render(request, self.template_name, args)

    def post(self, request):
        action = request.POST.get('submit-type')
        form = 书讯_add_form(request.POST, request.FILES)
        if form.is_valid():
            shuxunForm = form.save(commit=False)
            if action == 'save':
                shuxunForm.发布状态 = False
            else:
                shuxunForm.发布状态 = True
            form.save()
            标题 = form.cleaned_data['标题']
            简介 = form.cleaned_data['简介']
            作者 = form.cleaned_data['作者']
            序号 = form.cleaned_data['序号']
            图片 = form.cleaned_data['图片']
            args = {
                'form': form,
                '标题': 标题,
                '简介': 简介,
                '作者': 作者,
                '序号': 序号,
                '图片': 图片
            }
            messages.success(request, '书讯添加成功！')
            return HttpResponseRedirect(reverse('admin_task:content-item',kwargs={'content' : '书讯','task' : 'content'}))
        else:
            messages.error(request, '书讯添加失败请检查填表！')
            return render(request, self.template_name, {'form': form, 'content_title': '书讯', 'task': 'content'})

class ShuXunEditView(generic.TemplateView):
    template_name = "admin/书讯/书讯_edit.html"

    def get(self, request, pk):
        shuxun = 书讯.objects.get(id=pk)
        form = 书讯_add_form(instance=shuxun)
        args = {
            'form': form,
            '书讯': shuxun,
            'content_title': 'shuxun',
            'task': 'content'
        }
        return render(request, self.template_name, args)

    def post(self, request, pk):
        shuxun = 书讯.objects.get(id=pk)
        form = 书讯_add_form(request.POST, request.FILES, instance=shuxun)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, '书讯内容修改成功')
            return HttpResponseRedirect(reverse('admin_task:content-item-detail', kwargs={'content':'书讯','id': pk}))
        else:
            context = {
                'pk': pk,
                'form': form
            }
            messages.error(request, '书讯内容修改错误，请更正错误后提交更改内容')
            return render(request, self.template_name, context)

class ShuPingAddView(generic.TemplateView):
    template_name = 'admin/书评/书评_add.html'

    def get(self, request):
        form = 书评_add_form()
        书评_all = 书评.objects.all()
        args = {
            'form': form,
            '书评_all': 书评_all,
            'content_title': '书评',
            'task': 'content'
        }
        return render(request, self.template_name, args)

    def post(self, request):
        action = request.POST.get('submit-type')
        form = 书评_add_form(request.POST, request.FILES)
        if form.is_valid():
            shupingForm = form.save(commit=False)
            if action == 'save':
                shupingForm.发布状态 = False
            else:
                shupingForm.发布状态 = True
            form.save()
            标题 = form.cleaned_data['标题']
            书籍作者 = form.cleaned_data['书籍作者']
            书籍出版日期 = form.cleaned_data['书籍出版日期']
            书评内容 = form.cleaned_data['书评内容']
            书评作者 = form.cleaned_data['书评作者']
            图片 = form.cleaned_data['图片']
            args = {
                'form': form,
                '标题': 标题,
                '书籍作者': 书籍作者,
                '书籍出版日期': 书籍出版日期,
                '书评内容': 书评内容,
                '书评作者': 书评作者,
                '图片': 图片,
            }
            messages.success(request, '书评添加成功！')
            return HttpResponseRedirect(reverse('admin_task:content-item',kwargs={'content' : '书评','task' : 'content'}))
        else:
            messages.error(request, '书评添加失败请检查填表！')
            return render(request, 'admin/书评_add.html', {'form': form, 'content_title': '书评', 'task': 'content'})

class ShuPingEditView(generic.TemplateView):
    template_name = "admin/书评/书评_edit.html"

    def get(self, request, pk):
        shuping = 书评.objects.get(id=pk)
        form = 书评_add_form(instance=shuping)
        args = {
            'form': form,
            '书评': shuping,
            'content_title': '书评',
            'task': 'content'
        }
        return render(request, self.template_name, args)

    def post(self, request, pk):
        shuping = 书评.objects.get(id=pk)
        form = 书评_add_form(request.POST, request.FILES, instance=shuping)
        if form.is_valid():
            form.save()
            messages.success(request, '书评内容修改成功')
            return HttpResponseRedirect(reverse('admin_task:content-item-detail', kwargs={'content':'书评','id': pk}))
        else:
            context = {
                'pk': pk,
                'form': form
            }
            messages.error(request, '书评内容修改错误，请更正错误后提交更改内容')
            return render(request, self.template_name, context)

class YiLingAddView(generic.TemplateView):
    template_name = 'admin/译林/译林_add.html'

    def get(self, request):
        form = 译林_add_form()
        print(form)
        译林_all = 译林.objects.all()
        args = {
            'form': form,
            '译林_all': 译林_all,
            'content_title': '译林',
            'task': 'content'
        }
        return render(request, self.template_name, args)

    def post(self, request):
        action = request.POST.get('submit-type')
        form = 译林_add_form(request.POST, request.FILES)
        if form.is_valid():
            yilingForm = form.save(commit=False)
            if action == 'save':
                yilingForm.发布状态 = False
            else:
                yilingForm.发布状态 = True
            form.save()
            标题 = form.cleaned_data['标题']
            译文内容 = form.cleaned_data['译文内容']
            译文作者 = form.cleaned_data['译文作者']
            原文作者 = form.cleaned_data['原文作者']
            图片 = form.cleaned_data['图片']
            args = {
                'form': form,
                '标题': 标题,
                '译文内容': 译文内容,
                '译文作者': 译文作者,
                '原文作者': 原文作者,
                '图片': 图片
            }
            messages.success(request, '译林添加成功！')
            return HttpResponseRedirect(reverse('admin_task:content-item',kwargs={'content' : '译林','task' : 'content'}))
        else:
            messages.error(request, '译林添加失败请检查填表！')
            return render(request, self.template_name, {'form': form, 'content_title': '译林', 'task': 'content'})

class WenZhaiAddView(generic.TemplateView):
    template_name = 'admin/文摘/文摘_add.html'

    def get(self, request):
        form = 文摘_add_form()
        文摘_all = 文摘.objects.all()
        args = {
            'form': form,
            '文摘_all': 文摘_all,
            'content_title': '文摘',
            'task': 'content'
        }
        return render(request, self.template_name, args)

    def post(self, request):
        action = request.POST.get('submit-type')
        form = 文摘_add_form(request.POST, request.FILES)
        if form.is_valid():
            wenzhaiForm = form.save(commit=False)
            if action == 'save':
                wenzhaiForm.发布状态 = False
            else:
                wenzhaiForm.发布状态 = True
            form.save()
            标题 = form.cleaned_data['标题']
            内容 = form.cleaned_data['内容']
            作者 = form.cleaned_data['作者']
            资源 = form.cleaned_data['资源']
            图片 = form.cleaned_data['图片']
            args = {
                'form': form,
                '标题': 标题,
                '内容': 内容,
                '作者': 作者,
                '资源': 资源,
                '图片': 图片
            }
            messages.success(request, '文摘添加成功！')
            return HttpResponseRedirect(reverse('admin_task:content-item',kwargs={'content' : '文摘','task' : 'content'}))
        else:
            messages.error(request, '文摘添加失败请检查填表！')
            return render(request, self.template_name, {'form': form, 'content_title': '文摘', 'task': 'content'})

class LunWenAddView(generic.TemplateView):
    template_name = 'admin/论文/论文_add.html'

    def get(self, request):
        form = 论文_add_form()
        论文_all = 论文.objects.all()
        args = {
            'form': form,
            '论文_all': 论文_all,
            'content_title': '论文',
            'task': 'content'
        }
        return render(request, self.template_name, args)

    def post(self, request):
        action = request.POST.get('submit-type')
        form = 论文_add_form(request.POST, request.FILES)
        if form.is_valid():
            lunwenForm = form.save(commit=False)
            if action == 'save':
                lunwenForm.发布状态 = False
            else:
                lunwenForm.发布状态 = True
            form.save()
            标题 = form.cleaned_data['标题']
            文档 = form.cleaned_data['文档']
            作者 = form.cleaned_data['作者']
            args = {
                'form': form,
                '标题': 标题,
                '文档': 文档,
                '作者': 作者,
            }
            messages.success(request, '论文添加成功！')
            return HttpResponseRedirect(reverse('admin_task:content-item',kwargs={'content' : '论文','task' : 'content'}))
        else:
            messages.error(request, '论文添加失败请检查填表！')
            return render(request, 'admin/论文_add.html', {'form': form, 'content_title': '论文', 'task': 'content'})

def LunWenEditView(request, pk):
    lunwen = get_object_or_404(论文, id=pk)

    if request.method == 'POST':
        form = 论文_add_form(request.POST, request.FILES, instance=lunwen)
        if form.is_valid():
            # 如果表单有效，保存编辑后的论文
            form.save()
            return HttpResponseRedirect(reverse('admin_task:content-item',kwargs={'content' : '论文','task' : 'content'}))
          # 重定向到论文列表页面
    else:
        form = 论文_add_form(instance=lunwen)  # 使用现有的论文对象填充表单

    context = {
        'form': form,
        'content_title': '论文',
        'task': 'content',
    }
    return render(request, 'admin/论文/论文_edit.html', context)

class JingXunAddView(generic.TemplateView):
    template_name = 'admin/经训/经训_add.html'

    def get(self, request):
        form = 经训_add_form()
        经训_all = 经训.objects.all()
        args = {
            'form': form,
            '经训_all': 经训_all,
            'content_title': '经训',
            'task': 'content'
        }
        return render(request, self.template_name, args)

    def post(self, request):
        action = request.POST.get('submit-type')
        form = 经训_add_form(request.POST, request.FILES)
        if form.is_valid():
            jingxunForm = form.save(commit=False)
            if action == 'save':
                jingxunForm.发布状态 = False
            else:
                jingxunForm.发布状态 = True
            form.save()
            标题 = form.cleaned_data['标题']
            章节 = form.cleaned_data['章节']
            内容 = form.cleaned_data['内容']
            args = {
                'form': form,
                '标题': 标题,
                '章节': 章节,
                '内容': 内容,
            }
            messages.success(request, '经训添加成功！')
            return HttpResponseRedirect(reverse('admin_task:content-item',kwargs={'content' : '经训','task' : 'content'}))
        else:
            messages.error(request, '经训添加失败请检查填表！')
            return render(request, self.template_name, {'form': form, 'content_title': '经训', 'task': 'content'})

class GuJiAddView(generic.TemplateView):
    template_name = 'admin/古籍/古籍_add.html'

    def get(self, request):
        form = 古籍_add_form()
        古籍_all = 古籍.objects.all()
        args = {
            'form': form,
            '古籍_all': 古籍_all,
            'content_title': '古籍',
            'task': 'content'
        }
        return render(request, self.template_name, args)

    def post(self, request):
        action = request.POST.get('submit-type')
        form = 古籍_add_form(request.POST, request.FILES)
        if form.is_valid():
            gujiForm = form.save(commit=False)
            if action == 'save':
                gujiForm.发布状态 = False
            else:
                gujiForm.发布状态 = True
            form.save()
            标题 = form.cleaned_data['标题']
            文档 = form.cleaned_data['文档']
            作者 = form.cleaned_data['作者']
            args = {
                'form': form,
                '标题': 标题,
                '文档': 文档,
                '作者': 作者,

            }
            messages.success(request, '古籍添加成功！')
            return HttpResponseRedirect(reverse('admin_task:content-item',kwargs={'content' : '古籍','task' : 'content'}))

        else:
            messages.error(request, '古籍添加失败请检查填表！')
            return render(request, self.template_name, {'form': form, 'content_title': '古籍', 'task': 'content'})
class ShuKuAddView(generic.TemplateView):
    template_name = 'admin/书库/书库_add.html'

    def get(self, request):
        form = 书库_add_form()
        书库_all = 书库.objects.all()
        args = {
            'form': form,
            '书库_all': 书库_all,
            'content_title': '书库',
            'task': 'content'
        }
        return render(request, self.template_name, args)

    def post(self, request):
        action = request.POST.get('submit-type')
        form = 书库_add_form(request.POST, request.FILES)
        if form.is_valid():
            shukuForm = form.save(commit=False)
            if action == 'save':
                shukuForm.发布状态 = False
            else:
                shukuForm.发布状态 = True
            form.save()
            标题 = form.cleaned_data['标题']
            文档 = form.cleaned_data['文档']
            作者 = form.cleaned_data['作者']
            args = {
                'form': form,
                '标题': 标题,
                '文档': 文档,
                '作者': 作者,

            }
            messages.success(request, '书库添加成功！')
            return HttpResponseRedirect(reverse('admin_task:content-item',kwargs={'content' : '书库','task' : 'content'}))

        else:
            messages.error(request, '书库添加失败请检查填表！')
            return render(request, self.template_name, {'form': form, 'content_title': '书库', 'task': 'content'})














