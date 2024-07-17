from django import forms

class InputForm(forms.Form):
    text = forms.CharField(label='Your input', max_length=100)
