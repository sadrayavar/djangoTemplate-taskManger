from django.shortcuts import redirect
from django.http import HttpResponseForbidden
from .forms import NewspaperForm
from .models import Newspaper


def newspaper(request):
    if request.method == "POST":
        form = NewspaperForm(request.POST)
        emails = Newspaper.objects.filter(email=form.save(commit=False).email)

        # save email if it doesnt exists
        if len(emails) == 0:
            if form.is_valid():
                form.save()

        # trigger existing email's active property
        elif len(emails) == 1:
            email = emails[0]
            email.active = not (email.active)
            email.save()

        return redirect("homePage")
    else:
        return HttpResponseForbidden()


def createForm():
    return NewspaperForm()
