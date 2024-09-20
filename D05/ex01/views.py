from django.shortcuts import render

# Create your views here.
def django(request):
    return render(request, "django.html")

def display(request):
    return render(request, "display.html")

def templates(request):
    return render(request, "templates.html")