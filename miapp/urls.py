from django.urls import path
from .views import cargar_inicio, LibroList, LibroCreate ,LibroUpdate,LibroDelete,LibroDetalle
from .views import EjemplarList,EjemplarCreate,EjemplarUpdate,EjemplarDelete,EjemplarDetalle
from .views import PrestamoList,PrestamoCreate,PrestamoUpdate,PrestamoDelete,PrestamoDetalle
from .views import LoginView,LogoutView
urlpatterns = [
    #Libros
    path('', cargar_inicio, name = 'inicio'),
    path('libros/', LibroList.as_view(), name = 'listar_libros'),
    path('libros/nuevo/', LibroCreate.as_view(), name = 'nuevo_libro'),
    path('libros/editar/<int:pk>', LibroUpdate.as_view(), name = 'editar_libro'),
    path('libros/eliminar/<int:pk>', LibroDelete.as_view(), name = 'borrar_libro'),
    path('libros/detalle/<int:pk>', LibroDetalle.as_view(), name = 'detalle_libro'),

    #Ejemplar
    path('ejemplar/', EjemplarList.as_view(), name = 'ejemplar'),
    path('ejemplar/nuevo/', EjemplarCreate.as_view(), name = 'nuevo_ejemplar'),
    path('ejemplar/editar/<int:pk>', EjemplarUpdate.as_view(), name = 'editar_ejemplar'),
    path('ejemplar/eliminar/<int:pk>', EjemplarDelete.as_view(), name = 'borrar_ejemplar'),
    path('ejemplar/detalle/<int:pk>', EjemplarDetalle.as_view(), name = 'detalle_ejemplar'),

    #Prestamo
    path('prestamo/', PrestamoList.as_view(), name = 'prestamos'),
    path('prestamo/nuevo/', PrestamoCreate.as_view(), name = 'nuevo_prestamo'),
    path('prestamo/editar/<int:pk>', PrestamoUpdate.as_view(), name = 'editar_prestamo'),
    path('prestamo/eliminar/<int:pk>', PrestamoDelete.as_view(), name = 'borrar_prestamo'),
    path('prestamo/detalle/<int:pk>', PrestamoDetalle.as_view(), name = 'detalle_prestamo'),

    #Iniciar sesion
    path('iniciasesion', LoginView.as_view(template_name='accounts/login.html'), name = 'login'),
    path('logoutsesion', LogoutView.as_view(template_name='accounts/logout.html'), name = 'logout'),
]