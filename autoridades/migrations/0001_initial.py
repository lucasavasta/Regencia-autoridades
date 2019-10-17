
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.PositiveIntegerField(help_text='Ingrese código de la asignatura.', unique=True, validators=[django.core.validators.MaxValueValidator(999999), django.core.validators.MinValueValidator(1)], verbose_name='Código asignatura')),
                ('nombre', models.CharField(help_text='Ingrese el nombre de la asignatura.', max_length=40, verbose_name='Nombre de la asignatura')),
                ('año', models.PositiveIntegerField(help_text='Ingrese el año en el que se cursa la asignatura.', validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(1)], verbose_name='Año de la asignatura')),
            ],
            options={
                'verbose_name_plural': 'asignaturas',
            },
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('dni', models.PositiveSmallIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(1)])),
                ('nombre', models.CharField(help_text='Ingrese el nombre del profesor.', max_length=40)),
                ('apellido', models.CharField(help_text='Ingrese el apellido del profesor.', max_length=40)),
            ],
            options={
                'verbose_name': 'Profesor',
                'verbose_name_plural': 'Profesores',
            },
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turnos', models.CharField(choices=[('M', 'Mañana'), ('T', 'Tarde'), ('N', 'Noche')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(help_text='Ingrese la fecha actual', verbose_name='Fecha actual')),
                ('curso', models.PositiveIntegerField(help_text='Ingrese el curso correspondiente.', validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(1)], verbose_name='Curso perteneciente')),
                ('division', models.PositiveIntegerField(help_text='Ingrese la division del curso correspondiente.', validators=[django.core.validators.MaxValueValidator(7), django.core.validators.MinValueValidator(1)], verbose_name='Division del curso')),
                ('ausente', models.BooleanField(blank=True, null=True)),
                ('tarde', models.BooleanField(blank=True, null=True)),
                ('asignatura', models.ForeignKey(help_text='Elegir una asignatura', on_delete=django.db.models.deletion.CASCADE, to='autoridades.Asignatura')),
                ('profesor', models.ForeignKey(help_text='Elegir un profesor', on_delete=django.db.models.deletion.CASCADE, to='autoridades.Profesor')),
                ('turno', models.ForeignKey(help_text='Elegir un turno', on_delete=django.db.models.deletion.CASCADE, to='autoridades.Turno')),
            ],
            options={
                'verbose_name_plural': 'Seguimiento',
            },
        ),
    ]
