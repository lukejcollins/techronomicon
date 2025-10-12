from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="techronomiblog-home"),
    path("about/", views.about, name="about"),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
]
