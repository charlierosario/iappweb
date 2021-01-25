from django.db import models
from ckeditor.fields import RichTextField
# esto esta modificado , null=True, blank=True
from datetime import date


class Page(models.Model):

    msj = "Cómo obtener las coordenadas de un lugar <br> 1. ir a www.latlong.net <br> 2. Introducir la direccion: ej. Rioja 2045, Rosario, Santa Fe<br>3.Dar al boton Find <br> 4. Aparecera una marca azul en el mapa si ve que no esta exactamente haga doble click en la localizacion exacta<br>5. Listo copie la latitud y longitud tal cual.<br><br>En el campo de localizacion debe introducir de esta forma esos datos incluidos las llaves:<br>{lat: -32.952881, lng: -60.655832}"

    headerimg = models.ImageField(verbose_name="Imagen", upload_to="projects", null=True, blank=True, help_text="ATENCION!! ASEGURARSE QUE LA IMAGEN NO SUPERA LOS 710px DE ALTURA PARA GUARDAR LA PROPORCIONALIDAD.")
    title = models.CharField(verbose_name="Título", max_length=200)
    codigo = models.CharField(verbose_name="Código", max_length=8)
    order = models.SmallIntegerField(verbose_name="Orden de publicación", default=0,
                                     help_text="1 Es el principal, luego a partir del 2 son secundarios<br>Recuerde no repetir nunca valores es decir establezca un orden ordinal<br> ej si son 2 cursos el principal sera 1 y el secundario 2, si son 3 cursos el principal 1, luego 2 y luego 3<br>Si el curso que carga es antiguo es decir ya finalizo puede poner cualquier numero sin seguir un orden<br>este campo sirve para ordenar todos los cursos actuales o futuros a ese efecto<br>debe establecer los nros en cada curso para que se muestren los activos secundarios y el curso principal que desee mostrar.")
    institucion = models.CharField(verbose_name="Institución organizadora", max_length=200, null=True, blank=True, help_text="Solo rellene este campo si el curso no es organizado por el IAPP")
    fechacurso = models.DateField(verbose_name="Fecha")
    horacurso = models.CharField(verbose_name="Horario", max_length=200)
    content = RichTextField(verbose_name="Organizan", null=True, blank=True)
    disertantescurso = RichTextField(verbose_name="Disertantes")
    temario = RichTextField(verbose_name="Temario", null=True, blank=True)
    arancelcurso = models.TextField(verbose_name='Arancel')
    auspicia = RichTextField(verbose_name="Auspician", null=True, blank=True)
    localizacioncurso= models.CharField(verbose_name="Localizacion (Coordenadas)", max_length=400, help_text=msj)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:

        verbose_name = "curso"
        verbose_name_plural = "cursos"
        ordering = ['-fechacurso']

    def __str__(self):
        return self.title

    @property
    def is_past_due(self):
        return date.today() > self.fechacurso
