# Generated by Django 4.0.5 on 2022-09-06 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designacoes', '0017_alter_desigsabado_tema'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desigquarta',
            name='indicador_Principal',
            field=models.CharField(blank=True, choices=[('Isaías', 'Isaías'), ('Joselito', 'Joselito'), ('Vanoel', 'Vanoel'), ('Ronaldo', 'Ronaldo'), ('Isac', 'Isac'), ('Arnaldo', 'Arnaldo'), ('José', 'José'), ('Paulo Copque', 'Paulo Copque'), ('Gilson', 'Gilson'), ('Vanoel', 'Vanoel'), ('Samuel', 'Samuel'), ('David', 'David'), ('Pierre', 'Pierre'), ('Samuel', 'Samuel'), ('Jardas', 'Jardas'), ('Ueliton', 'Ueliton'), ('Renan', 'Renan')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='desigquarta',
            name='indicador_Recepção',
            field=models.CharField(blank=True, choices=[('Isaías', 'Isaías'), ('Joselito', 'Joselito'), ('Vanoel', 'Vanoel'), ('Ronaldo', 'Ronaldo'), ('Isac', 'Isac'), ('Arnaldo', 'Arnaldo'), ('José', 'José'), ('Paulo Copque', 'Paulo Copque'), ('Gilson', 'Gilson'), ('Vanoel', 'Vanoel'), ('Samuel', 'Samuel'), ('David', 'David'), ('Pierre', 'Pierre'), ('Samuel', 'Samuel'), ('Jardas', 'Jardas'), ('Ueliton', 'Ueliton'), ('Renan', 'Renan')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='desigquarta',
            name='leitor_Estudo',
            field=models.CharField(blank=True, choices=[('Douglas', 'Douglas'), ('Arnaldo', 'Arnaldo'), ('David', 'David'), ('Isaías', 'Isaías'), ('Joselito', 'Joselito'), ('Renan', 'Renan')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='desigquarta',
            name='volante_01',
            field=models.CharField(blank=True, choices=[('Isaías', 'Isaías'), ('Joselito', 'Joselito'), ('Vanoel', 'Vanoel'), ('Ronaldo', 'Ronaldo'), ('Isac', 'Isac'), ('Arnaldo', 'Arnaldo'), ('José', 'José'), ('Paulo Copque', 'Paulo Copque'), ('Gilson', 'Gilson'), ('Vanoel', 'Vanoel'), ('Samuel', 'Samuel'), ('David', 'David'), ('Pierre', 'Pierre'), ('Samuel', 'Samuel'), ('Jardas', 'Jardas'), ('Ueliton', 'Ueliton'), ('Renan', 'Renan')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='desigquarta',
            name='volante_02',
            field=models.CharField(blank=True, choices=[('Isaías', 'Isaías'), ('Joselito', 'Joselito'), ('Vanoel', 'Vanoel'), ('Ronaldo', 'Ronaldo'), ('Isac', 'Isac'), ('Arnaldo', 'Arnaldo'), ('José', 'José'), ('Paulo Copque', 'Paulo Copque'), ('Gilson', 'Gilson'), ('Vanoel', 'Vanoel'), ('Samuel', 'Samuel'), ('David', 'David'), ('Pierre', 'Pierre'), ('Samuel', 'Samuel'), ('Jardas', 'Jardas'), ('Ueliton', 'Ueliton'), ('Renan', 'Renan')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='desigsabado',
            name='indicador_Principal',
            field=models.CharField(blank=True, choices=[('Isaías', 'Isaías'), ('Joselito', 'Joselito'), ('Vanoel', 'Vanoel'), ('Ronaldo', 'Ronaldo'), ('Isac', 'Isac'), ('Arnaldo', 'Arnaldo'), ('José', 'José'), ('Paulo Copque', 'Paulo Copque'), ('Gilson', 'Gilson'), ('Vanoel', 'Vanoel'), ('Samuel', 'Samuel'), ('David', 'David'), ('Pierre', 'Pierre'), ('Samuel', 'Samuel'), ('Jardas', 'Jardas'), ('Ueliton', 'Ueliton'), ('Renan', 'Renan')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='desigsabado',
            name='indicador_Recepção',
            field=models.CharField(blank=True, choices=[('Isaías', 'Isaías'), ('Joselito', 'Joselito'), ('Vanoel', 'Vanoel'), ('Ronaldo', 'Ronaldo'), ('Isac', 'Isac'), ('Arnaldo', 'Arnaldo'), ('José', 'José'), ('Paulo Copque', 'Paulo Copque'), ('Gilson', 'Gilson'), ('Vanoel', 'Vanoel'), ('Samuel', 'Samuel'), ('David', 'David'), ('Pierre', 'Pierre'), ('Samuel', 'Samuel'), ('Jardas', 'Jardas'), ('Ueliton', 'Ueliton'), ('Renan', 'Renan')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='desigsabado',
            name='volante_01',
            field=models.CharField(blank=True, choices=[('Isaías', 'Isaías'), ('Joselito', 'Joselito'), ('Vanoel', 'Vanoel'), ('Ronaldo', 'Ronaldo'), ('Isac', 'Isac'), ('Arnaldo', 'Arnaldo'), ('José', 'José'), ('Paulo Copque', 'Paulo Copque'), ('Gilson', 'Gilson'), ('Vanoel', 'Vanoel'), ('Samuel', 'Samuel'), ('David', 'David'), ('Pierre', 'Pierre'), ('Samuel', 'Samuel'), ('Jardas', 'Jardas'), ('Ueliton', 'Ueliton'), ('Renan', 'Renan')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='desigsabado',
            name='volante_02',
            field=models.CharField(blank=True, choices=[('Isaías', 'Isaías'), ('Joselito', 'Joselito'), ('Vanoel', 'Vanoel'), ('Ronaldo', 'Ronaldo'), ('Isac', 'Isac'), ('Arnaldo', 'Arnaldo'), ('José', 'José'), ('Paulo Copque', 'Paulo Copque'), ('Gilson', 'Gilson'), ('Vanoel', 'Vanoel'), ('Samuel', 'Samuel'), ('David', 'David'), ('Pierre', 'Pierre'), ('Samuel', 'Samuel'), ('Jardas', 'Jardas'), ('Ueliton', 'Ueliton'), ('Renan', 'Renan')], max_length=30, null=True),
        ),
    ]
