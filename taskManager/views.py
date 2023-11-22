from django.http import HttpResponse


# Create your views here.
def homePage(request):
    return HttpResponse("Home page")
