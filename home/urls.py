from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.test,name="test"),
    path('test1/',views.lunwen,name="test1")
]