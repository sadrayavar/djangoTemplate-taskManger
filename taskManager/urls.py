from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from comment.views import myComments
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("admin_page/", include("adminapp.urls")),
    path("", include("task.urls")),
    path("account/", include("user.urls")),
    path("comments/", myComments, name="myCommentsPage"),
    path("search/", views.search, name="searchPage"),
    path("newspaper/", include("emailpaper.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
