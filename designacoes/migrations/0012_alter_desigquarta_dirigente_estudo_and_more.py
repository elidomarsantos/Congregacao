# Generated by Django 4.0.5 on 2022-07-07 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designacoes', '0011_alter_desigquarta_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desigquarta',
            name='dirigente_Estudo',
            field=models.CharField(blank=True, choices=[('Jeferson', 'Jeferson'), ('Elidomar', 'Elidomar'), ('Abel', 'Abel'), ('Geraldo', 'Geraldo')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='desigquarta',
            name='indicador_Principal',
            field=models.CharField(blank=True, choices=[('José', 'José'), ('Douglas', 'Douglas'), ('Isac', 'Isac'), ('Vanoel', 'Vanoel'), ('Samuel', 'Samuel'), ('Arnaldo', 'Arnaldo'), ('David', 'David'), ('Isaías', 'Isaías'), ('Joselito', 'Joselito'), ('Pierre', 'Pierre'), ('Vanoel', 'Vanoel'), ('Paulo Moura', 'Paulo Moura'), ('Paulo Copque', 'Paulo Copque'), ('Samuel', 'Samuel'), ('Ronaldo', 'Ronaldo'), ('Gilson', 'Gilson'), ('Jardas', 'Jardas'), ('Wesley', 'Wesley')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='desigquarta',
            name='indicador_Recepção',
            field=models.CharField(blank=True, choices=[('José', 'José'), ('Douglas', 'Douglas'), ('Isac', 'Isac'), ('Vanoel', 'Vanoel'), ('Samuel', 'Samuel'), ('Arnaldo', 'Arnaldo'), ('David', 'David'), ('Isaías', 'Isaías'), ('Joselito', 'Joselito'), ('Pierre', 'Pierre'), ('Vanoel', 'Vanoel'), ('Paulo Moura', 'Paulo Moura'), ('Paulo Copque', 'Paulo Copque'), ('Samuel', 'Samuel'), ('Ronaldo', 'Ronaldo'), ('Gilson', 'Gilson'), ('Jardas', 'Jardas'), ('Wesley', 'Wesley')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='desigquarta',
            name='joias_Espirituais',
            field=models.CharField(blank=True, choices=[('Jeferson', 'Jeferson'), ('Elidomar', 'Elidomar'), ('Abel', 'Abel'), ('Geraldo', 'Geraldo'), ('José', 'José'), ('Douglas', 'Douglas'), ('Nelito', 'Nelito'), ('Isac', 'Isac'), ('Vanoel', 'Vanoel'), ('Samuel', 'Samuel'), ('Arnaldo', 'Arnaldo')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='desigquarta',
            name='leitor_Estudo',
            field=models.CharField(blank=True, choices=[('Douglas', 'Douglas'), ('Arnaldo', 'Arnaldo'), ('David', 'David'), ('Isaías', 'Isaías'), ('Joselito', 'Joselito')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='desigquarta',
            name='nossa_Vida_01',
            field=models.CharField(blank=True, choices=[('Jeferson', 'Jeferson'), ('Elidomar', 'Elidomar'), ('Abel', 'Abel'), ('Geraldo', 'Geraldo'), ('José', 'José'), ('Douglas', 'Douglas'), ('Nelito', 'Nelito'), ('Isac', 'Isac'), ('Vanoel', 'Vanoel'), ('Samuel', 'Samuel'), ('Arnaldo', 'Arnaldo')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='desigquarta',
            name='nossa_Vida_02',
            field=models.CharField(blank=True, choices=[('Jeferson', 'Jeferson'), ('Elidomar', 'Elidomar'), ('Abel', 'Abel'), ('Geraldo', 'Geraldo'), ('José', 'José'), ('Douglas', 'Douglas'), ('Nelito', 'Nelito'), ('Isac', 'Isac'), ('Vanoel', 'Vanoel'), ('Samuel', 'Samuel'), ('Arnaldo', 'Arnaldo')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='desigquarta',
            name='oração_Final',
            field=models.CharField(blank=True, choices=[('José', 'José'), ('Douglas', 'Douglas'), ('Isac', 'Isac'), ('Vanoel', 'Vanoel'), ('Samuel', 'Samuel'), ('Arnaldo', 'Arnaldo'), ('Joselito', 'Joselito'), ('Vanoel', 'Vanoel'), ('Paulo Copque', 'Paulo Copque')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='desigquarta',
            name='oração_Inicial',
            field=models.CharField(blank=True, choices=[('Jeferson', 'Jeferson'), ('Elidomar', 'Elidomar'), ('Abel', 'Abel'), ('Geraldo', 'Geraldo')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='desigquarta',
            name='presidente',
            field=models.CharField(blank=True, choices=[('Jeferson', 'Jeferson'), ('Elidomar', 'Elidomar'), ('Abel', 'Abel'), ('Geraldo', 'Geraldo')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='desigquarta',
            name='tesouros',
            field=models.CharField(blank=True, choices=[('Jeferson', 'Jeferson'), ('Elidomar', 'Elidomar'), ('Abel', 'Abel'), ('Geraldo', 'Geraldo'), ('José', 'José'), ('Douglas', 'Douglas'), ('Nelito', 'Nelito'), ('Isac', 'Isac'), ('Vanoel', 'Vanoel'), ('Samuel', 'Samuel'), ('Arnaldo', 'Arnaldo')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='desigquarta',
            name='volante_01',
            field=models.CharField(blank=True, choices=[('José', 'José'), ('Douglas', 'Douglas'), ('Isac', 'Isac'), ('Vanoel', 'Vanoel'), ('Samuel', 'Samuel'), ('Arnaldo', 'Arnaldo'), ('David', 'David'), ('Isaías', 'Isaías'), ('Joselito', 'Joselito'), ('Pierre', 'Pierre'), ('Vanoel', 'Vanoel'), ('Paulo Moura', 'Paulo Moura'), ('Paulo Copque', 'Paulo Copque'), ('Samuel', 'Samuel'), ('Ronaldo', 'Ronaldo'), ('Gilson', 'Gilson'), ('Jardas', 'Jardas'), ('Wesley', 'Wesley')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='desigquarta',
            name='volante_02',
            field=models.CharField(blank=True, choices=[('José', 'José'), ('Douglas', 'Douglas'), ('Isac', 'Isac'), ('Vanoel', 'Vanoel'), ('Samuel', 'Samuel'), ('Arnaldo', 'Arnaldo'), ('David', 'David'), ('Isaías', 'Isaías'), ('Joselito', 'Joselito'), ('Pierre', 'Pierre'), ('Vanoel', 'Vanoel'), ('Paulo Moura', 'Paulo Moura'), ('Paulo Copque', 'Paulo Copque'), ('Samuel', 'Samuel'), ('Ronaldo', 'Ronaldo'), ('Gilson', 'Gilson'), ('Jardas', 'Jardas'), ('Wesley', 'Wesley')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='desigsabado',
            name='indicador_Principal',
            field=models.CharField(blank=True, choices=[('José', 'José'), ('Douglas', 'Douglas'), ('Isac', 'Isac'), ('Vanoel', 'Vanoel'), ('Samuel', 'Samuel'), ('Arnaldo', 'Arnaldo'), ('David', 'David'), ('Isaías', 'Isaías'), ('Joselito', 'Joselito'), ('Pierre', 'Pierre'), ('Vanoel', 'Vanoel'), ('Paulo Moura', 'Paulo Moura'), ('Paulo Copque', 'Paulo Copque'), ('Samuel', 'Samuel'), ('Ronaldo', 'Ronaldo'), ('Gilson', 'Gilson'), ('Jardas', 'Jardas'), ('Wesley', 'Wesley')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='desigsabado',
            name='indicador_Recepção',
            field=models.CharField(blank=True, choices=[('José', 'José'), ('Douglas', 'Douglas'), ('Isac', 'Isac'), ('Vanoel', 'Vanoel'), ('Samuel', 'Samuel'), ('Arnaldo', 'Arnaldo'), ('David', 'David'), ('Isaías', 'Isaías'), ('Joselito', 'Joselito'), ('Pierre', 'Pierre'), ('Vanoel', 'Vanoel'), ('Paulo Moura', 'Paulo Moura'), ('Paulo Copque', 'Paulo Copque'), ('Samuel', 'Samuel'), ('Ronaldo', 'Ronaldo'), ('Gilson', 'Gilson'), ('Jardas', 'Jardas'), ('Wesley', 'Wesley')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='desigsabado',
            name='leitor_da_Sentinela',
            field=models.CharField(blank=True, choices=[('Pierre', 'Pierre'), ('Vanoel', 'Vanoel'), ('Paulo Moura', 'Paulo Moura'), ('Paulo Copque', 'Paulo Copque'), ('Samuel', 'Samuel')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='desigsabado',
            name='presidente',
            field=models.CharField(blank=True, choices=[('Jeferson', 'Jeferson'), ('Elidomar', 'Elidomar'), ('Abel', 'Abel'), ('Geraldo', 'Geraldo'), ('José', 'José'), ('Douglas', 'Douglas'), ('Nelito', 'Nelito'), ('Isac', 'Isac'), ('Vanoel', 'Vanoel'), ('Samuel', 'Samuel'), ('Arnaldo', 'Arnaldo')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='desigsabado',
            name='volante_01',
            field=models.CharField(blank=True, choices=[('José', 'José'), ('Douglas', 'Douglas'), ('Isac', 'Isac'), ('Vanoel', 'Vanoel'), ('Samuel', 'Samuel'), ('Arnaldo', 'Arnaldo'), ('David', 'David'), ('Isaías', 'Isaías'), ('Joselito', 'Joselito'), ('Pierre', 'Pierre'), ('Vanoel', 'Vanoel'), ('Paulo Moura', 'Paulo Moura'), ('Paulo Copque', 'Paulo Copque'), ('Samuel', 'Samuel'), ('Ronaldo', 'Ronaldo'), ('Gilson', 'Gilson'), ('Jardas', 'Jardas'), ('Wesley', 'Wesley')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='desigsabado',
            name='volante_02',
            field=models.CharField(blank=True, choices=[('José', 'José'), ('Douglas', 'Douglas'), ('Isac', 'Isac'), ('Vanoel', 'Vanoel'), ('Samuel', 'Samuel'), ('Arnaldo', 'Arnaldo'), ('David', 'David'), ('Isaías', 'Isaías'), ('Joselito', 'Joselito'), ('Pierre', 'Pierre'), ('Vanoel', 'Vanoel'), ('Paulo Moura', 'Paulo Moura'), ('Paulo Copque', 'Paulo Copque'), ('Samuel', 'Samuel'), ('Ronaldo', 'Ronaldo'), ('Gilson', 'Gilson'), ('Jardas', 'Jardas'), ('Wesley', 'Wesley')], max_length=30, null=True),
        ),
    ]
