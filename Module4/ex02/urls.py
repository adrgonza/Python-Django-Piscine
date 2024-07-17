from django.urls import path
from . import views

urlpatterns = [
    path('ex02/', views.index, name='ex02_view'),
]