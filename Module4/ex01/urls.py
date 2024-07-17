from django.urls import path
from . import views

urlpatterns = [
    path('ex01/django/', views.django_intro, name='django_intro'),
    path('ex01/display/', views.display_process, name='display_process'),
    path('ex01/templates/', views.template_engine, name='template_engine'),
]