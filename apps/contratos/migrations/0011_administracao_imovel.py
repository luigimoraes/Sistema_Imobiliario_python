# Generated by Django 4.1.5 on 2023-01-29 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0013_alter_imoveis_endereco'),
        ('contratos', '0010_remove_administracao_nome_administracao_proprietario'),
    ]

    operations = [
        migrations.AddField(
            model_name='administracao',
            name='imovel',
            field=models.ForeignKey(default=None, limit_choices_to={'tipo': 'CASA'}, on_delete=django.db.models.deletion.PROTECT, to='cadastros.imoveis', verbose_name='Imóvel'),
        ),
    ]
