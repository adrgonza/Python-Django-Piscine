from django import forms

class InputForm(forms.Form):
    user_input = forms.CharField(label='Input', max_length=100)
