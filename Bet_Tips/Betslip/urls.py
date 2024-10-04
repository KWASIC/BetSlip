# tips/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.match_list, name='match_list1'),
    path('update_result/<int:match_id>/<str:result>/', views.update_result, name='update_result'),
    path('vip-odds/<str:odds_range>/', views.vip_odds, name='vip_odds'),
    path('yesterdays-tips/', views.yesterdays_tips, name='yesterdays_tips'),
]
