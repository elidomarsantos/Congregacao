from dataclasses import field, fields

from django import forms

from .models import DesigQuarta, DesigSabado

class DateInput(forms.DateInput):
    input_type = 'date' 



class Form_Quarta(forms.ModelForm):
   
    class Meta:
        model = DesigQuarta
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select Date','type': 'date'})
          }   


class Form_Sabado(forms.ModelForm):
   
    
    class Meta:
        model = DesigSabado
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select Date','type': 'date'})
          }   


