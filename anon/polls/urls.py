from django.urls import path
from django.contrib.auth import views as views2

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('polls/', views.polls),
    #todo: доделать авторизацию
    path('login/', views2.TemplateView, name='login'),
    path('polls/<int:event_id>', views.questions),
]