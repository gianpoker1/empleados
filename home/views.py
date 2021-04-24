from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba
from .forms import PruebaForm

# Create your views here.
class PruebaView(TemplateView):
    template_name ='templates/home/prueba.html'

class ResumenFoundationView(TemplateView):
    template_name ='templates/home/resume_foundation.html'



class PruebaListView(ListView):
    template_name = "templates/home/lista.html"
    context_object_name='listaNumeros'
    queryset = ['1','10','20','30']


class ListaPrueba(ListView):
    template_name='templates/home/lista_prueba.html'
    model = Prueba
    context_object_name = 'lista'

class PruebaCreateView(CreateView):
    template_name = 'templates/home/add.html'
    model = Prueba
    form_class = PruebaForm
    success_url ='/'