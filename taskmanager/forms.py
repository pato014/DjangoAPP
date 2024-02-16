from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', }),
            'description': forms.Textarea(attrs={'class': 'form-control,'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
