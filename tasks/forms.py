from .models import task
from django import forms

class addTask(forms.ModelForm):
    class Meta:
        model = task
        fields = ("title","user","body")
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'cols': '5', 'rows': '3'}),
        }


class editTask(forms.ModelForm):
    class Meta:
        model = task
        fields = ("title", "body", "complete")
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'cols': '5', 'rows': '3'}),
        }
