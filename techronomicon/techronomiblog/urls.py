from django.urls import path
from .views import home, about

urlpatterns = [
    path('', home, name='techronomiblog-home'),
    path('about/', about, name='about')
]
