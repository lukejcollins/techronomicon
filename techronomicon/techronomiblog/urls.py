from django.urls import path
from .views import home, about
from . import views

urlpatterns = [
    path('', home, name='techronomiblog-home'),
    path('about/', about, name='about'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail')
]
