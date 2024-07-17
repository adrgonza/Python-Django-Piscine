from django.shortcuts import render

def django_intro(request):
    return render(request, 'django.html')

def display_process(request):
    return render(request, 'display.html')

def template_engine(request):
    return render(request, 'templates.html')
