from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
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

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'admin/login.html'
    authentication_form = CustomLoginForm

def tasklist(request):
    通讯= request.user.has_perm('shuwei.edit_通讯')
    书讯= request.user.has_perm('shuwei.edit_书讯')
    书评= request.user.has_perm('shuwei.edit_书评')
    观点= request.user.has_perm('shuwei.edit_观点')
    文艺= request.user.has_perm('shuwei.edit_文艺')
    问答= request.user.has_perm('shuwei.edit_问答')
    译林= request.user.has_perm('shuwei.edit_译林')
    文摘= request.user.has_perm('shuwei.edit_文摘')
    论文= request.user.has_perm('shuwei.edit_论文')
    经训= request.user.has_perm('shuwei.edit_经训')
    古籍= request.user.has_perm('shuwei.edit_古籍')
    书库= request.user.has_perm('shuwei.edit_书库')

    if request.user.has_perm('shuwei.edit_通讯'):
        通讯 = True
        all_通讯 = 通讯.objects.all()
    if request.user.has_perm('shuwei.edit_书讯'):
        书讯= True
        all_书讯 = 书讯.objects.all()
    if request.user.has_perm('shuwei.edit_书评'):
        书评= True
        all_书评 = 书评.objects.all()
    if request.user.has_perm('shuwei.edit_观点'):
        观点= True
        all_观点 = 观点.objects.all()
    if request.user.has_perm('shuwei.edit_文艺'):
        文艺= True
        all_文艺 = 文艺.objects.all()
    if request.user.has_perm('shuwei.edit_问答'):
        问答= True
        all_问答 = 问答.objects.all()
    if request.user.has_perm('shuwei.edit_译林'):
        译林= True
        all_译林 = 译林.objects.all()
    if request.user.has_perm('shuwei.edit_文摘'):
        文摘= True
        all_文摘 = 文摘.objects.all()
    if request.user.has_perm('shuwei.edit_论文'):
        论文= True
        all_论文 = 论文.objects.all()
    if request.user.has_perm('shuwei.edit_经训'):
        经训= True
        all_经训 = 经训.objects.all()
    if request.user.has_perm('shuwei.edit_古籍'):
        古籍= True
        all_古籍 = 古籍.objects.all()
    if request.user.has_perm('shuwei.edit_书库'):
        书库= True
        all_书库 = 书库.objects.all()
    print(request.user.has_perm('shuwei.edit_通讯'))

    return render(request,'admin/main.html', {})
