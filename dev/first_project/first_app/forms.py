from django import forms

class nameForm(forms.Form):
    name=forms.CharField(max_length=30)
    age=forms.IntegerField()
    location=forms.CharField(max_length=30)
