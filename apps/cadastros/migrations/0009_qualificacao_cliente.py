# Generated by Django 4.1.5 on 2023-01-27 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0008_remove_imoveis_prop_alter_clientes_tipo_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qualificacao_Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualificacao', models.CharField(max_length=100, verbose_name='Qualificação')),
            ],
            options={
                'verbose_name': 'Qualificão',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
