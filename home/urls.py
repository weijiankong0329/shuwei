from django.urls import path,include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('关于我们/', TemplateView.as_view(template_name='about_us.html'), name='about_us'),
    path('联系我们/', TemplateView.as_view(template_name='contact_us.html'), name='contact_us'),

    path('',views.MainView,name="homepage"),

    path('通讯/',views.TongXun,name="tongxun"),
    path('通讯/<int:tongxun_id>',views.TongXunDetail,name="tongxundetail"),

    path('书讯/',views.ShuXun,name="shuxun"),
    path('书讯/<int:shuxun_id>',views.ShuXunDetail,name="shuxundetail"),

    path('书评/',views.ShuPing,name="shuping"),
    path('书评/<int:shuping_id>',views.ShuPingDetail.as_view(),name="shupingdetail"),

    path('观点/',views.GuanDian,name="guandian"),
    path('观点/<int:guandian_id>',views.GuanDianDetail.as_view(),name="guandiandetail"),

    path('文艺/',views.WenYi,name="wenyi"),
    path('文艺/<int:wenyi_id>',views.WenYiDetail.as_view(),name="wenyidetail"),

    path('视频/',views.ShiPing,name="shiping"),
    path('视频/<int:shiping_id>',views.ShiPingDetail.as_view(),name="shipingdetail"),

    path('问答/',views.WenDa,name="wenda"),
    path('问答/搜索结果/',views.WenDaSearch,name="wendasearch"),
    path('问答/提交问题/',views.WenDaAddQuestion,name="wendaaddquestion"),
    path('问答/<int:wenda_id>',views.WenDaDetail.as_view(),name="wendadetail"),

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

    path('文摘/',views.WenZhai,name="wenzhai"),
    path('文摘/<int:wenzhai_id>',views.WenZhaiDetail.as_view(),name="wenzhaidetail"),
]


