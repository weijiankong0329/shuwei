from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('login',views.CustomLoginView.as_view(),name="login"),
    path('logout',auth_view.LogoutView.as_view(),name="logout"),
    path('main',views.tasklist,name='main'),

    path('main/通讯/add',views.TongXunAddView.as_view(),name='通讯_add'),
    path('main/通讯/edit/<int:pk>',views.TongXunEditView.as_view(),name='通讯_edit'),

    path('main/书讯/add', views.ShuXunAddView.as_view(), name='书讯_add'),
    path('main/书讯/edit/<int:pk>', views.ShuXunEditView.as_view(), name='书讯_edit'),

    path('main/书评/add',views.ShuPingAddView.as_view(),name='书评_add'),
    path('main/书评/edit/<int:pk>', views.ShuPingEditView.as_view(), name='书评_edit'),

    path('main/观点/add',views.GuanDianAddView.as_view(),name='观点_add'),
    path('main/观点/edit/<int:pk>', views.GuanDianEditView.as_view(), name='观点_edit'),

    path('main/文艺/add',views.WenYiAddView.as_view(),name='文艺_add'),
    path('main/文艺/edit/<int:pk>', views.WenYiEditView.as_view(), name='文艺_edit'),

    path('main/译林/add', views.YiLingAddView.as_view(), name='译林_add'),
    path('main/译林/edit/<int:pk>', views.YiLingEditView.as_view(), name='译林_edit'),

    path('main/文摘/add', views.WenZhaiAddView.as_view(), name='文摘_add'),
    path('main/文摘/edit/<int:pk>', views.WenZhaiEditView.as_view(), name='文摘_edit'),

    path('main/论文/add', views.LunWenAddView.as_view(), name='论文_add'),
    path('main/论文/edit/<int:pk>/', views.LunWenEditView.as_view(), name='论文_edit'),

    path('main/经训/add', views.JingXunAddView.as_view(), name='经训_add'),

    path('main/古籍/add', views.GuJiAddView.as_view(), name='古籍_add'),
    path('main/古籍/edit/<int:pk>/', views.GuJiEditView.as_view(), name='古籍_edit'),

    path('main/书库/add', views.ShuKuAddView.as_view(), name='书库_add'),
    path('main/书库/edit/<int:pk>/', views.ShuKuEditView.as_view(), name='书库_edit'),

    path('main/<str:content>/<str:task>', views.ContentItemList, name='content-item'),
    path('main/<str:content>/delete/<int:id>', views.ContentItemDeleteView, name='content-item-delete'),
    path('main/<str:content>/detail/<int:id>',views.ContentItemDetailView,name='content-item-detail'),
    path('main/<str:content>-<int:content_id>/comment-detail/<int:id>',views.ContentItemCommentDetailView,name='content-item-comment-detail'),
    path('main/<str:content>-<int:content_id>/<str:type>/<int:id>/approval',views.CommentApprovalView,name='comment-approval')
]