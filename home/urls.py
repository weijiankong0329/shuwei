from django.urls import path,include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('关于我们/', TemplateView.as_view(template_name='about_us.html'), name='about_us'),
    path('联系我们/', TemplateView.as_view(template_name='contact_us.html'), name='contact_us'),
    path('',views.MainView,name="homepage"),
    path('视频/',views.ShiPing,name="shiping"),
    path('经训/', views.JingXun, name='jingxun'),
    path('经训/所有章节/<int:经训_id>/', views.show_all_chapters, name='show_all_chapters'),
    path('经训/内容/<int:章节_id>/', views.JingXuncontent, name='content'), 
    path('经训/搜索结果/', views.search, name='search'),
    path('书库/', views.ShuKu, name='shuku'),
    path('书库/<int:shuku_id>/', views.ShuKucontent, name='detail'),
    path('古籍/', views.GuJi, name='guji'),
    path('古籍/<int:guji_id>/', views.GuJicontent, name='gujidetail'),
    path('论文/', views.LunWen, name='lunwen'),
    path('论文/<int:lunwen_id>/', views.LunWencontent, name='lunwendetail'),
    path('译林/', views.YiLing, name='yiling'),
    path('译林/<int:yiling_id>/', views.YiLingcontent, name='yilingdetail'),
]


