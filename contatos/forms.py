from dataclasses import field, fields

from django import forms

from .models import Contatos


class Form_Contatos(forms.ModelForm):

    class Meta:
        model = Contatos
        fields = '__all__'