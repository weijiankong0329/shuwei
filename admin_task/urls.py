from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('login',views.CustomLoginView.as_view(),name="login"),
    path('logout',auth_view.LogoutView.as_view(),name="logout"),
    path('main',views.tasklist,name='main'),
    path('main/通讯',views.tongxun,name='通讯')
]