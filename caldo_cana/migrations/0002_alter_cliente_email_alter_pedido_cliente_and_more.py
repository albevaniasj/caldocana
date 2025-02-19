# Generated by Django 5.1.4 on 2024-12-07 12:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caldo_cana', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caldo_cana.cliente'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='descricao',
            field=models.CharField(max_length=255),
        ),
    ]
