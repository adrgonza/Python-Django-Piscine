from django.urls import path
from .views import ex03_view

urlpatterns = [
    path('', ex03_view, name='ex03'),
]
