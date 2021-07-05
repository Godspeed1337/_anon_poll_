from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('polls/', views.polls),
    #todo: доделать авторизацию
    path('accounts/', include('django.contrib.auth.urls')),
    path('polls/<int:event_id>', views.questions),
]
