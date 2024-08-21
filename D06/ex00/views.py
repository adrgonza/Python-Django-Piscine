from django.shortcuts import render

# Create your views here.

def ex00_view(request):
    return render(request, 'index.html')