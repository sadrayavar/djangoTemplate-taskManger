from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

mainAttr = {
    "class": "form-control text-bg-dark",
    "id": "floatingInput",
}


class UserRegistratoinForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "autocomplete": "current-password",
                "placeholder": "Password",
                **mainAttr,
            }
        ),
        label="Password",
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "autocomplete": "current-password",
                "placeholder": "Password",
                **mainAttr,
            }
        ),
        label="Password confirmation",
    )
    newspaper = forms.BooleanField(required=False)

    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email", "newspaper")
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "type": "text",
                    "autofocus": True,
                    "autocomplete": "username",
                    "placeholder": "Username",
                    **mainAttr,
                },
            ),
            "first_name": forms.TextInput(
                attrs={
                    "type": "text",
                    "maxLength": 150,
                    "placeholder": "First name",
                    **mainAttr,
                },
            ),
            "last_name": forms.TextInput(
                attrs={
                    "type": "text",
                    "maxLength": 150,
                    "placeholder": "Last name",
                    **mainAttr,
                },
            ),
            "email": forms.TextInput(
                attrs={
                    "type": "email",
                    "placeholder": "Email",
                    **mainAttr,
                },
            ),
        }


class UserEditionForm(UserChangeForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "autocomplete": "current-password",
                "placeholder": "Password",
                **mainAttr,
            }
        ),
        label="Password",
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "autocomplete": "current-password",
                "placeholder": "Password",
                **mainAttr,
            }
        ),
        label="Password confirmation",
    )

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
        )
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "type": "text",
                    "autofocus": True,
                    "autocomplete": "username",
                    "placeholder": "Username",
                    **mainAttr,
                },
            ),
            "first_name": forms.TextInput(
                attrs={
                    "type": "text",
                    "maxLength": 150,
                    "placeholder": "First name",
                    **mainAttr,
                },
            ),
            "last_name": forms.TextInput(
                attrs={
                    "type": "text",
                    "maxLength": 150,
                    "placeholder": "Last name",
                    **mainAttr,
                },
            ),
            "email": forms.TextInput(
                attrs={
                    "type": "email",
                    "placeholder": "Email",
                    **mainAttr,
                },
            ),
        }


class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "autofocus": True,
                "autocomplete": "username",
                "placeholder": "Username",
                **mainAttr,
            }
        ),
        label="Username",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "autocomplete": "current-password",
                "placeholder": "Password",
                **mainAttr,
            }
        ),
        label="Password",
    )
