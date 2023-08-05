from django.shortcuts import render
from django.utils import timezone
from home.models import 论文

# Create your views here.

def test(request):
    return render(request,'index.html',{'time': timezone.now})

def lunwen(request):
    context ={
        'all_论文': 论文.objects.all(),
        'content_title':'lunwen',
        'task':'content'
    }
    return render(request,'test.html', context)