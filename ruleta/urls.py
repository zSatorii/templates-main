from django.urls import path
from . import views

urlpatterns = [
    path('', views.ruleta_page, name='ruleta_page'),
    path('girar/', views.ruleta_casino, name='girar_ruleta'),
]
