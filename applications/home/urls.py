from django.contrib import admin
from django.urls import path
from . import views

def DesdeApps(self):
    print('*******************************************home')



urlpatterns = [
    path('prueba/', views.PruebaView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('lista_prueba/', views.ListaPrueba.as_view()),
    path('add/', views.PruebaCreateView.as_view(),name='prueba_add'),
    path(
        'resumen-foundation/', 
        views.ResumenFoundationView.as_view(),
        name='resumen'
    ),

]
