from dataclasses import fields
from pyexpat import model
from django import forms
from .models import TaskList

class TaskForm(forms.ModelForm):
    class Meta:
        model=TaskList
        fields=['task','done']