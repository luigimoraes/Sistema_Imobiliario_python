# Generated by Django 4.1.5 on 2023-01-29 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0011_alter_imoveis_proprietario'),
        ('contratos', '0004_remove_administracao_imovel'),
    ]

    operations = [
        migrations.AddField(
            model_name='administracao',
            name='imovel',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='Imoveis.endereco +', to='cadastros.imoveis', verbose_name='Imóvel'),
        ),
        migrations.AlterField(
            model_name='administracao',
            name='proprietario',
            field=models.ForeignKey(default=None, limit_choices_to={'qualificacao': 2}, on_delete=django.db.models.deletion.PROTECT, related_name='Clientes.proprietario +', to='cadastros.clientes', verbose_name='Proprietário'),
        ),
    ]