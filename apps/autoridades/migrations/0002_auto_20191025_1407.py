# Generated by Django 2.1.1 on 2019-10-25 17:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoridades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='dni',
            field=models.PositiveSmallIntegerField(help_text='Ingrese el DNI del profesor.', primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(999999999), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='seguimiento',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha actual'),
        ),
        migrations.AlterField(
            model_name='seguimiento',
            name='turno',
            field=models.CharField(choices=[('mañana', 'Mañana'), ('tarde', 'Tarde'), ('noche', 'Noche')], max_length=6),
        ),
        migrations.DeleteModel(
            name='Turno',
        ),
    ]