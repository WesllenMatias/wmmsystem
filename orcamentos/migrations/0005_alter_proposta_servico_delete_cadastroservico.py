# Generated by Django 4.1.3 on 2022-12-01 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcamentos', '0004_proposta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposta',
            name='servico',
            field=models.TextField(verbose_name='Serviços'),
        ),
        migrations.DeleteModel(
            name='CadastroServico',
        ),
    ]
