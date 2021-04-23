from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    TemplateView, 
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Empleado
from .forms import EmpleadoForm

# Create your views here.

class InicioView(TemplateView):
    #vista que carga la pagina de inicio
    template_name='templates/inicio.html'
 
class ListAllEMpleados(ListView):
    template_name = "templates/persona/list_all.html"
    paginate_by=4
    context_object_name='empleados'
    

    def get_queryset(self):
        print('**************************************')
        palabra_clave=self.request.GET.get('kword','')
        print(palabra_clave)
        lista= Empleado.objects.filter(
            #
            first_name__icontains=palabra_clave
        )
        return lista

class ListaEmpleadosAdmin(ListView):
    template_name = "templates/persona/lista_empleados.html"
    paginate_by=4
    context_object_name='empleados'
    model = Empleado


class ListByAreaEmpleado(ListView):   
    template_name = "templates/persona/list-by-area.html"
    context_object_name='empleados'
    def get_queryset(self):
        area = self.kwargs['shorname']
        queryset = Empleado.objects.filter(
        departamento__name = area
        )
        return queryset

class ListByTrabajoEmpleado(ListView):   
    template_name = "templates/persona/list-by-trabajo.html"
    def get_queryset(self):
        area = self.kwargs['shorname']
        queryset = Empleado.objects.filter(
        job = area
        
    )
        return queryset

class ListEmpleadosByKword(ListView):
    template_name='templates/persona/bykword.html'
    context_object_name='empleados'
    def get_queryset(self):
        print('**************************************')
        palabra_clave=self.request.GET.get('kword','')
        lista= Empleado.objects.filter(
            first_name = palabra_clave
        )
        return lista

class ListaHabilidadesEmpleado(ListView):
    template_name = 'templates/persona/habilidades.html'
    context_object_name='habilidades'

    def get_queryset(self):
        palabra_clave=self.request.GET.get('kword','')        
        empleado=Empleado.objects.get(first_name=palabra_clave)
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "templates/persona/detalle_empleado.html"

    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo']='Empleado del mes'
        return context


class SuccessView(TemplateView):
    template_name = "templates/persona/success.html"
    success_url= reverse_lazy('persona_app:agregar')


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "templates/persona/add.html"
    form_class = EmpleadoForm
    success_url= reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' '+empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "templates/persona/update.html"
    fields=[
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url= reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
        
    def form_valid(self, form):
        
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "templates/persona/delete.html"
    context_object_name='empleado'
    success_url= reverse_lazy('persona_app:empleados_admin')
