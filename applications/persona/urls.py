from django.contrib import admin
from django.urls import path
from . import views

app_name = 'persona_app'

urlpatterns = [
    path(
        '', 
        views.InicioView.as_view(),
        name='inicio'
    ),
    path(
        'listar-todo-empleados/', 
        views.ListAllEMpleados.as_view(),
        name='empleados_all'
    ),
    path(
        'lista-empleados-admin', 
        views.ListaEmpleadosAdmin.as_view(),
        name='empleados_admin'
    ),
    path(
        'list-by-area/<shorname>/', 
        views.ListByAreaEmpleado.as_view(),
        name = 'empleados_area'
        ),
    path('list-by-trabajo/<shorname>/', views.ListByTrabajoEmpleado.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
    path('lista-habilidades/', views.ListaHabilidadesEmpleado.as_view()),
    path(
        'ver-empleado/<pk>/', 
        views.EmpleadoDetailView.as_view(),
        name='empleado_detalle'
    ),
    path(
        'agregar-empleado/', 
        views.EmpleadoCreateView.as_view(),
        name='agregar'
    ),
    path('success/', views.SuccessView.as_view(),name='correcto'),
    path('udate-empleado/<pk>/', 
    views.EmpleadoUpdateView.as_view(),
    name='modificar_empleado'
    ),
    path('delete-empleado/<pk>/', 
    views.EmpleadoDeleteView.as_view(),
    name='eliminar_empleado'
    ),

]
