from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name='Главная страница'),
    path('about_me/', views.about_me, name='О себе'),

]
