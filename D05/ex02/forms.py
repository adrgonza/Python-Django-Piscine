from django import forms

class InputForm(forms.Form):
    user_input = forms.CharField(label='Your Input', max_length=100)
