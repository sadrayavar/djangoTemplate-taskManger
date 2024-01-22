from django import forms
from .models import Newspaper


class NewspaperForm(forms.ModelForm):
    email = forms.EmailField(
        label="Enter your email to add it to the newspaper List. Add again to remove it.",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control form-control-dark text-bg-light",
                "placeholder": "Newspaper ( Add / Remove )",
            },
        ),
    )

    class Meta:
        model = Newspaper
        fields = ["email"]
