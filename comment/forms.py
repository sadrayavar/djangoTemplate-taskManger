from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)

        widgets = {
            "text": forms.TextInput(attrs={"autofocus": True}),
        }
    text = forms.CharField(label='Your Comment')