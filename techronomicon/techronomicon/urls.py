from django.contrib import admin
from django.urls import include, path
from techronomiblog import views as blog_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("techronomiblog.urls")),
    path("markdownx/", include("markdownx.urls")),
    path("healthz", blog_views.health),
]
