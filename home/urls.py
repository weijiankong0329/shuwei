from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.MainView,name="test"),
    path('经训/', views.JingXun, name='jingxun'),
    path('经训/所有章节/<int:经训_id>/', views.show_all_chapters, name='show_all_chapters'),
    path('经训/内容/<int:章节_id>/', views.JingXuncontent, name='content'), 
    path('经训/搜索结果/', views.search, name='search'),
    path('书库/', views.ShuKu, name='shuku'),
    path('书库/<int:shuku_id>/', views.ShuKucontent, name='detail'),

]


