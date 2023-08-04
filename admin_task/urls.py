from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('login',views.CustomLoginView.as_view(),name="login"),
    path('logout',auth_view.LogoutView.as_view(),name="logout"),
    path('main',views.tasklist,name='main'),

    path('main/通讯',views.TongXunListView,name='通讯'),
    path('main/通讯/add',views.TongXunAddView.as_view(),name='通讯_add'),
    path('main/通讯/detail/<int:pk>',views.TongXunDetailView,name='通讯_detail'),
    path('main/通讯/edit/<int:pk>',views.TongXunEditView.as_view(),name='通讯_edit'),
    path('main/通讯/delete/<int:pk>',views.TongXunDeleteView,name='通讯_delete'),

    path('main/书讯',views.ShuXunListView,name='书讯'),
    path('main/书讯/add', views.ShuXunAddView.as_view(), name='书讯_add'),
    path('main/书讯/detail/<int:pk>', views.ShuXunDetailView, name='书讯_detail'),
    path('main/书讯/edit/<int:pk>', views.ShuXunEditView.as_view(), name='书讯_edit'),
    path('main/书讯/delete/<int:pk>', views.ShuXunDeleteView, name='书讯_delete'),

    path('main/书评/<str:task>',views.shuping,name='书评')
]