from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    deadline_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    deadline_time = forms.TimeField(widget=forms.TimeInput(attrs={"type": "time"}))

    class Meta:
        model = Task
        fields = ["title", "priority", "state", "deadline_date", "deadline_time"]
