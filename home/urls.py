from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.MainView,name="test"),
    path('经训/', views.jingxun, name='jingxun'),
    path('show_all_chapters/<int:经训_id>/', views.show_all_chapters, name='show_all_chapters'),
    path('经训/章节/<int:章节_id>/', views.content, name='content'), 
    path('search/', views.search, name='search'),


]