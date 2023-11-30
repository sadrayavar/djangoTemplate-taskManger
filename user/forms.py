from django import forms
from .models import CustomUser


class UserRegistratoinForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "password",
            "first_name",
            "last_name",
            "last_name",
            "email",
            "avatar",
        )
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "my-class",
                    "autofocus": True,
                }
            ),
            "password": forms.PasswordInput(),
        }
