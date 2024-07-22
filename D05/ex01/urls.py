from django.urls import path
from . import views

urlpatterns = [
    path('django/', views._django, name="_django"),
    path('display/', views._display, name ="_display"),
    path('templates/', views._templates, name ="_templates"),
]