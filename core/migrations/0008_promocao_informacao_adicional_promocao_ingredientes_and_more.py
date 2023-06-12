# Generated by Django 4.2.1 on 2023-06-12 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_promocao_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocao',
            name='informacao_adicional',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Informação adicional'),
        ),
        migrations.AddField(
            model_name='promocao',
            name='ingredientes',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ingredientes'),
        ),
        migrations.AddField(
            model_name='promocao',
            name='marca',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Marca'),
        ),
        migrations.AddField(
            model_name='promocao',
            name='valor_energetico',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Valor Energético'),
        ),
    ]
