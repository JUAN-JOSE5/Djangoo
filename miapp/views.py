from django.shortcuts import render
#Importar para mirar una pagina,crear unos datos, actulizar los datos o borrar los datos
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
#
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
#Importar el inicio de sesion en django 
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
#
from .models import Libro
from .models import Ejemplar
from .models import Prestamo
def cargar_inicio(request):
    return render(request, "miapp/index.html")

#Libros
class LibroList(ListView):
    model = Libro
    template_name = 'miapp/lista_libros.html'

class LibroDetalle(DetailView):
    model = Libro
    template_name = 'miapp/detalle_libro.html'
class LibroCreate(CreateView):
    model = Libro
    fields = ['nombre','descripcion','isbn','copias']
    template_name = 'miapp/nuevo_libro.html'
    success_url = reverse_lazy('listar_libros')

class LibroUpdate(UpdateView):
    model = Libro
    fields = ['nombre','descripcion','isbn','copias']
    template_name = 'miapp/actualizar_libro.html'
    success_url = reverse_lazy('listar_libros')

class LibroDelete(DeleteView):
    model = Libro
    template_name = 'miapp/eliminar_libro.html'
    success_url = reverse_lazy('listar_libros')

#Ejemplar

class EjemplarList(ListView):
    model = Ejemplar
    template_name = 'miapp/ejemplar.html'

class EjemplarCreate(CreateView):
    model = Ejemplar
    fields = ['numeroejemplar','fechadecompra','libro']
    template_name = 'miapp/nuevo_ejemplar.html'
    success_url = reverse_lazy('ejemplar')

class EjemplarUpdate(UpdateView):
    model = Ejemplar
    fields = ['numeroejemplar','fechadecompra','libro']
    template_name = 'miapp/editar_ejemplar.html'
    success_url = reverse_lazy('ejemplar')

class EjemplarDelete(DeleteView):
    model = Ejemplar
    template_name = 'miapp/eliminar_ejemplar.html'
    success_url = reverse_lazy('ejemplar')

class EjemplarDetalle(DetailView):
    model = Ejemplar
    template_name = 'miapp/detalle_ejemplar.html'

#Prestamo

class PrestamoList(ListView):
    model = Prestamo
    template_name = 'miapp/prestamo.html'


class PrestamoCreate(CreateView):
    model = Prestamo
    fields = ['fechaprestamo','nombre_cliente','telefono','estado']
    template_name = 'miapp/nuevo_prestamo.html'
    success_url = reverse_lazy('prestamos')

class PrestamoUpdate(UpdateView):
    model = Prestamo
    fields = ['fechaprestamo','nombre_cliente','telefono','estado']
    template_name = 'miapp/editar_prestamo.html'
    success_url = reverse_lazy('prestamos')

class PrestamoDelete(DeleteView):
    model = Prestamo
    template_name = 'miapp/eliminar_prestamo.html'
    success_url = reverse_lazy('prestamos')

class PrestamoDetalle(DetailView):
    model = Prestamo
    template_name = 'miapp/detalle_prestamo.html'