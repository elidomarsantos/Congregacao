# Generated by Django 4.0.4 on 2022-06-16 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designacoes', '0009_rename_indicador_recepcao_desigquarta_indicador_recepção_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desigquarta',
            name='data',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
