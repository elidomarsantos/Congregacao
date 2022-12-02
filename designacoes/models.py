
from cProfile import label
from django.db import models
from django.contrib.auth import get_user_model

ANCIÃOS = (
    ('Jeferson', 'Jeferson' ),
    ('Elidomar', 'Elidomar'),
    ('Abel', 'Abel'),
    ('Geraldo', 'Geraldo'),
)

ANCIÃOS_SERVOS = (
    ('Jeferson', 'Jeferson' ),
    ('Elidomar', 'Elidomar'),
    ('Abel', 'Abel'),
    ('Geraldo', 'Geraldo'),
    ('José', 'José'),
    ('Douglas', 'Douglas'),
    ('Nelito', 'Nelito'),
    ('Isac', 'Isac'),
    ('Vanoel', 'Vanoel'),
    ('Samuel', 'Samuel'),
    ('Arnaldo', 'Arnaldo'),
)

INDICADORES = (

    ('Isaías', 'Isaías'),
    ('Joselito','Joselito'),
    ('Vanoel', 'Vanoel'),
    ('Ronaldo', 'Ronaldo'),
    ('Isac', 'Isac'),
    ('Arnaldo', 'Arnaldo'),
    ('José', 'José'),
    ('Paulo Copque', 'Paulo Copque'),
    ('Gilson', 'Gilson'),
    ('Vanoel', 'Vanoel'),
    ('Samuel', 'Samuel'),
    ('David', 'David'),
    ('Pierre', 'Pierre'),
    ('Samuel', 'Samuel'),
    ('Jardas', 'Jardas'),
    ('Ueliton', 'Ueliton'),
    ('Renan','Renan'),
    ('Romenil','Romenil'),
    ('Marcio','Marcio'),
)

LEITORES_ESTUDO = (
    ('Douglas', 'Douglas'),
    ('Arnaldo', 'Arnaldo'),
    ('David', 'David'),
    ('Isaías', 'Isaías'),
    ('Joselito','Joselito'),
    ('Renan','Renan'),
    ('Romenil','Romenil'),
    
    
)

LEITORES_SENTINELA = (
    ('Pierre', 'Pierre'),
    ('Vanoel', 'Vanoel'),
    ('Paulo Moura', 'Paulo Moura'),
    ('Paulo Copque', 'Paulo Copque'),
    ('Samuel', 'Samuel'),
)

ORAÇÃO = (
   
    ('José', 'José'),
    ('Douglas', 'Douglas'),
    ('Vanoel', 'Vanoel'),
    ('Joselito','Joselito'),
    ('Arnaldo', 'Arnaldo'),
    ('Isac', 'Isac'),
    ('Samuel', 'Samuel'),
    ('Paulo Copque', 'Paulo Copque'),
    ('Pierre', 'Pierre'),
    ('Paulo Moura', 'Paulo Moura'),


)


class DesigQuarta(models.Model):
    data = models.DateField(blank=True, null=True,)
    presidente = models.CharField(max_length=30, blank=True, null=True, choices=ANCIÃOS)
    oração_Inicial = models.CharField(max_length=30, blank=True, null=True, choices=ANCIÃOS)
    tesouros = models.CharField(max_length=30, blank=True, null=True, choices=ANCIÃOS_SERVOS)
    joias_Espirituais = models.CharField(max_length=30, blank=True, null=True, choices=ANCIÃOS_SERVOS)
    leitura_da_Bíblia = models.CharField(max_length=30, blank=True, null=True)
    designação_01 = models.CharField(max_length=30, blank=True, null=True)
    ajudante_01 = models.CharField(max_length=30, blank=True, null=True)
    designação_02 = models.CharField(max_length=30, blank=True, null=True)
    ajudante_02 = models.CharField(max_length=30, blank=True, null=True)
    designação_03 = models.CharField(max_length=30, blank=True, null=True)
    ajudante_03 = models.CharField(max_length=30, blank=True, null=True)
    designação_04 = models.CharField(max_length=30, blank=True, null=True)
    ajudante_04 = models.CharField(max_length=30, blank=True, null=True)
    nossa_Vida_01 = models.CharField(max_length=30, blank=True, null=True, choices=ANCIÃOS_SERVOS)
    nossa_Vida_02 = models.CharField(max_length=30, blank=True, null=True, choices=ANCIÃOS_SERVOS)
    dirigente_Estudo = models.CharField(max_length=30, blank=True, null=True, choices=ANCIÃOS)
    leitor_Estudo = models.CharField(max_length=30, blank=True, null=True, choices=LEITORES_ESTUDO)
    oração_Final = models.CharField(max_length=30, blank=True, null=True, choices=ORAÇÃO)
    indicador_Principal = models.CharField(max_length=30, blank=True, null=True, choices=INDICADORES)
    indicador_Recepção = models.CharField(max_length=30, blank=True, null=True, choices=INDICADORES)
    volante_01 = models.CharField(max_length=30, blank=True, null=True, choices=INDICADORES)
    volante_02 = models.CharField(max_length=30, blank=True, null=True, choices=INDICADORES)

    class Meta:
        ordering = ['data']    

class DesigSabado(models.Model):
    data = models.DateField(blank=True, null=True)
    presidente = models.CharField(max_length=30, blank=True, null=True, choices=ANCIÃOS_SERVOS)
    orador = models.CharField(max_length=30, blank=True, null=True)
    congregação = models.CharField(max_length=30, blank=True, null=True)
    tema = models.CharField(max_length=60, blank=True, null=True)
    leitor_da_Sentinela = models.CharField(max_length=30, blank=True, null=True, choices=LEITORES_SENTINELA)
    indicador_Principal = models.CharField(max_length=30, blank=True, null=True, choices=INDICADORES)
    indicador_Recepção = models.CharField(max_length=30, blank=True, null=True, choices=INDICADORES)
    volante_01 = models.CharField(max_length=30, blank=True, null=True, choices=INDICADORES)
    volante_02 = models.CharField(max_length=30, blank=True, null=True, choices=INDICADORES)    

    class Meta:
        ordering = ['data']    