# Generated by Django 4.1.5 on 2023-02-09 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0033_remove_administracao_dia_do_repasse_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administracao',
            name='dias_para_repasse',
            field=models.IntegerField(blank=True, default=5, null=True, verbose_name='Dia para repasse'),
        ),
    ]
