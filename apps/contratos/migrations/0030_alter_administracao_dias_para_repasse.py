# Generated by Django 4.1.5 on 2023-02-09 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0029_alter_administracao_dias_para_repasse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administracao',
            name='dias_para_repasse',
            field=models.CharField(blank=True, default=1, max_length=100, null=True, verbose_name='Dia para repasse'),
        ),
    ]
