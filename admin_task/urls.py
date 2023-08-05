from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('login',views.CustomLoginView.as_view(),name="login"),
    path('logout',auth_view.LogoutView.as_view(),name="logout"),
    path('main',views.tasklist,name='main'),
   
    path('main/书讯',views.shuxun,name='书讯'),
    path('main/书评/<str:task>',views.shuping,name='书评'),
    path('main/译林',views.yiling,name='译林'),
    path('main/译林/add',views.addYiLingView.as_view(),name='译林_add'),
    path('main/译林/detail/<int:pk>',views.addYiLingView.as_view(),name='译林_detail'),
    path('main/文摘/<str:task>',views.wenzhai,name='文摘'),
    path('main/文摘/add',views.addWenZhaiView.as_view(),name='文摘_add'),
    path('main/论文',views.lunwen,name='论文'),
    path('main/论文/add',views.addLunWenView.as_view(),name='论文_add'),
    path('delete_lunwen/<int:lunwen_id>/', views.delete_lunwen, name='论文_delete'),
    path('edit_lunwen/<int:lunwen_id>/', views.edit_lunwen, name='论文_edit'),
    path('main/经训',views.jingxun,name='经训'),
    path('main/经训/add',views.addJingXunView.as_view(),name='经训_add'),
    path('main/古籍',views.guji,name='古籍'),
    path('main/古籍/add',views.addGuJiView.as_view(),name='古籍_add'),
    path('main/书库',views.shuku,name='书库'),
    path('main/书库/add',views.addShuKuView.as_view(),name='书库_add'),
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