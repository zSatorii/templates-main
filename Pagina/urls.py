from django.urls import path
from .views import categorialistcreateview, categoriadestroy
from .views import home

urlpatterns = [
    path('inicio', home, name='home'),
    path('categoria/', categorialistcreateview.as_view(), name='Categoria-crear'),
    path('categoria/<int:pk>', categoriadestroy.as_view(), name='Categoria-eliminar')
]