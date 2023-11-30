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


class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "autofocus": True,
                "autocomplete": "username",
                "class": "form-control text-bg-dark",
                "id": "floatingInput",
                "placeholder": "Username",
            }
        ),
        label="Username",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "autocomplete": "current-password",
                "class": "form-control text-bg-dark",
                "id": "floatingPassword",
                "placeholder": "Password",
            }
        ),
        label="Password",
    )
