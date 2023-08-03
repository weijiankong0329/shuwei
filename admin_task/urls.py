from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('login',views.CustomLoginView.as_view(),name="login"),
    path('logout',auth_view.LogoutView.as_view(),name="logout"),
    path('main',views.tasklist,name='main'),
    path('main/通讯',views.tongxun,name='通讯'),
    path('main/通讯/add',views.addTongXunView.as_view(),name='通讯_add'),
    path('main/通讯/detail/<int:pk>',views.TongxunDetailView,name='通讯_detail'),
    path('main/通讯/edit/<int:pk>',views.TongXunEditView.as_view(),name='通讯_edit'),
    path('main/通讯/delete/<int:pk>',views.TongXunDelete,name='通讯_delete'),
    path('main/书讯',views.shuxun,name='书讯'),
    path('main/书评/<str:task>',views.shuping,name='书评')
]