# Generated by Django 4.1.5 on 2023-01-30 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0018_administracao_dia_do_repasse_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administracao',
            name='dia_do_repasse',
        ),
    ]
