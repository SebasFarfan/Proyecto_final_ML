from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('buscar-producto', views.buscar_producto, name='Buscar'),
    path('buscar-producto-ml/',views.busqueda_producto),
    path('buscar-varios-productos/',views.busqueda_varios_productos),
]