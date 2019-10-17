from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Turno(models.Model):
    TURNOS_CHOICES = (
    	('M', 'Mañana'),
        ('T', 'Tarde'),
        ('N', 'Noche'),
    )
    turnos = models.CharField(
        max_length=1,
        choices=TURNOS_CHOICES
    )

    def __str__(self):
    	return '%s' % (self.turnos)


class Profesor(models.Model):
	dni = models.PositiveSmallIntegerField(
		primary_key=True,
		validators=[
			MaxValueValidator(9999),
			MinValueValidator(1)
		]
	)
	nombre = models.CharField(max_length=40, help_text='Ingrese el nombre del profesor.')
	apellido = models.CharField(max_length=40, help_text='Ingrese el apellido del profesor.')

	class Meta:
		verbose_name='Profesor'
		verbose_name_plural = "Profesores"

	def __str__(self):
		return '%s' % (self.nombre)


class Asignatura(models.Model):
	codigo = models.PositiveIntegerField('Código asignatura', 
		unique=True,
		validators=[
			MaxValueValidator(999999),
			MinValueValidator(1)
		],
		help_text='Ingrese código de la asignatura.'
	)
	nombre = models.CharField('Nombre de la asignatura', max_length=40, help_text='Ingrese el nombre de la asignatura.')
	año = models.PositiveIntegerField('Año de la asignatura',
		validators=[
			MaxValueValidator(6),
			MinValueValidator(1)
		],
		help_text='Ingrese el año en el que se cursa la asignatura.'
	)

	def __str__(self):
		return '%s %s' % (self.nombre, self.año)

	class Meta:
		verbose_name_plural = 'asignaturas'


class Seguimiento(models.Model):
	fecha = models.DateField('Fecha actual', help_text='Ingrese la fecha actual')
	profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, help_text = 'Elegir un profesor')
	turno = models.ForeignKey(Turno, on_delete=models.CASCADE, help_text = 'Elegir un turno')
	curso = models.PositiveIntegerField('Curso perteneciente',
		validators=[
			MaxValueValidator(6),
			MinValueValidator(1)
		],
		help_text='Ingrese el curso correspondiente.'
	)
	division = models.PositiveIntegerField('Division del curso',
		validators=[
			MaxValueValidator(7),
			MinValueValidator(1)
		],
		help_text='Ingrese la division del curso correspondiente.'
	)
	asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, help_text = 'Elegir una asignatura')
	ausente = models.BooleanField(blank=True, null=True)
	tarde = models.BooleanField(blank=True, null=True)


	def __str__(self):
		return '%s %s %s %s %s %s' % (self.fecha, self.profesor, self.turno, self.curso, self.division, self.asignatura)

	class Meta:
		verbose_name_plural = 'asignaturas'