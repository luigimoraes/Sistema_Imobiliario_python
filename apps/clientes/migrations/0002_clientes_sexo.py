# Generated by Django 4.1.5 on 2023-01-23 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('Indef', 'LGBTSQUEJTRNSD')], default='Indef', max_length=10, verbose_name='Sexo'),
        ),
    ]
