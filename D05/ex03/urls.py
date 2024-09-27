from django.urls import path
from . import views

urlpatterns = [
    path('', views.colortable, name='ex03'),
]
