# Generated by Django 4.1.5 on 2023-01-30 14:07

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0013_alter_imoveis_endereco'),
        ('contratos', '0016_alter_administracao_imovel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administracao',
            name='imovel',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='proprietario', chained_model_field='proprietario', default=None, on_delete=django.db.models.deletion.PROTECT, to='cadastros.imoveis'),
        ),
    ]
