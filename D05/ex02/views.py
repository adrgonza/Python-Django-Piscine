import os
from django.shortcuts import render
from django.conf import settings
from .forms import InputForm
from datetime import datetime

def form(request):
    form = InputForm()
    history = []

    if os.path.exists(settings.LOGS_FILE_PATH):
        with open(settings.LOGS_FILE_PATH, 'r') as file:
            for line in file:
                timestamp, user_input = line.strip().split(' ', 1)
                history.append((timestamp, user_input))

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            history.append((timestamp, user_input))

            with open(settings.LOGS_FILE_PATH, 'a') as file:
                file.write(f'{timestamp} {user_input}\n')

    return render(request, 'form.html', {'form': form, 'history': history})
