from django import forms
from .models import Task_List

class Task_Form(forms.ModelForm):
    class Meta:
        model=Task_List
        fields=['task','done']