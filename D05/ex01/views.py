from django.shortcuts import render

# Create your views here.
def _django(request):
    return render(request, "django.html")

def _display(request):
    return render(request, "display.html")

def _templates(request):
    return render(request, "templates.html")