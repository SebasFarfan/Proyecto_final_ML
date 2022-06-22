from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('buscar-producto', views.buscar_producto, name='Buscar'),
    path('buscar-producto-ml/',views.busqueda_producto),
    path('buscar-varios-productos/',views.busqueda_varios_productos),
    path('envio-alerta/',views.envio_correo),
    path('enviar/',views.contacto),
    path('listado-productos-buscar', views.listado_productos_buscar, name='Listado'),
    path('agregar-lista/',views.agregar_nombre_producto),
    path('buscar-productos-lista/', views.buscar_varios_productos),
]