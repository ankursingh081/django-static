from django.urls import path
from . import views
from .views import ClubChartView

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('user-home/', views.user_home, name='user-home'),
    path('about/', views.about, name='blog-about'),
    path('add-detail/', views.add_detail, name='add-detail'),
    path('chart/', ClubChartView.as_view(), name='task-chart'),
]