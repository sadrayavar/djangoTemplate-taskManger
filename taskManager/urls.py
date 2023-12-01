from django.contrib import admin
from django.urls import path, include
from comment.views import myComments
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("task.urls")),
    path("account/", include("user.urls")),
    path("comments/", myComments, name="myCommentsPage"),
    path("search/", views.search, name="searchPage"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
