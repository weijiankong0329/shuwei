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
    context ={}
    return render(request,'admin/main.html', context)

def tongxun(request):
    context ={
        'all_通讯': 通讯.objects.all(),
        'content':'tongxun-content'
    }
    return render(request,'admin/通讯.html', context)


