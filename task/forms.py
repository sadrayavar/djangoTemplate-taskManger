from django import forms
from .models import Task

mainAttr = {
    "class": "form-control text-bg-dark",
    "id": "floatingInput",
}


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            "title",
            "priority",
            "state",
            "deadline_date",
            "deadline_time",
            "image",
        )
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "type": "text",
                    "autofocus": True,
                    "placeholder": "Title",
                    **mainAttr,
                },
            ),
            "priority": forms.NumberInput(
                attrs={
                    "placeholder": "Priority",
                    **mainAttr,
                },
            ),
            "state": forms.Select(
                attrs={
                    "class": "form-select form-select-lg text-bg-dark",
                },
            ),
            "deadline_date": forms.DateInput(attrs={"type": "date", **mainAttr}),
            "deadline_time": forms.TextInput(attrs={"type": "time", **mainAttr}),
            "image": forms.FileInput(attrs={"type": "file", **mainAttr}),
        }
