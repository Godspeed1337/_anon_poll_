from django.urls import path
from django.contrib.auth import views as views2

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('polls/', views.polls),
    path('login/', views2.LoginView.as_view(), name='login'),
]