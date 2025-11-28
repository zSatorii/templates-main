from django.urls import path
from . import views

urlpatterns = [
    path('', views.summit_home, name='summit_home'),
]
