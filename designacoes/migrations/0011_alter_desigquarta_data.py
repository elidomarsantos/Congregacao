# Generated by Django 4.0.4 on 2022-06-16 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designacoes', '0010_alter_desigquarta_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desigquarta',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
    ]
