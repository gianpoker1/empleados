from django import forms
from .models import Prueba

class PruebaForm(forms.Form):
    class Meta:
        model = Prueba
        fields=(
            'titulo',
            'subtitulo',
            'cantidad',
        )
        widgets = {
            'titulo':forms.TextInput(
                attrs={
                    'placeholder':'Ingrese Texto',
                    
                }
            )
        }


    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese numero mayor a 10')

        return cantidad
        
