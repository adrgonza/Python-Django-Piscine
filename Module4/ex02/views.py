from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import InputForm
from django.conf import settings
import os

def ex02_view(request):
    form = InputForm()
    history = []

    # Check if logs file exists and read its content
    if os.path.exists(settings.LOG_FILE):
        with open(settings.LOG_FILE, 'r') as f:
            history = f.readlines()

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            timestamp = timezone.now()
            log_entry = f'{timestamp}: {text}\n'
            
            # Write to log file
            with open(settings.LOG_FILE, 'a') as f:
                f.write(log_entry)
            
            # Redirect to the same page to display updated history
            return redirect('ex02_view')

    context = {
        'form': form,
        'history': history,
    }
    return render(request, 'ex02/index.html', context)
