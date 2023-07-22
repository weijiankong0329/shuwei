from django.shortcuts import render
from django.utils import timezone

# Create your views here.

def test(request):
    return render(request,'index.html',{'time': timezone.now})
