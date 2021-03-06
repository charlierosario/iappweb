# Generated by Django 2.0.2 on 2019-11-06 17:47

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headerimg', models.ImageField(blank=True, help_text='ATENCION!! ASEGURARSE QUE LA IMAGEN NO SUPERA LOS 710px DE ALTURA PARA GUARDAR LA PROPORCIONALIDAD.', null=True, upload_to='projects', verbose_name='Imagen')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('codigo', models.CharField(max_length=8, verbose_name='Código')),
                ('fechacurso', models.DateField(verbose_name='Fecha')),
                ('horacurso', models.CharField(max_length=200, verbose_name='Horario')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Organizan')),
                ('disertantescurso', ckeditor.fields.RichTextField(verbose_name='Disertantes')),
                ('temario', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Temario')),
                ('arancelcurso', models.TextField(verbose_name='Arancel')),
                ('auspicia', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Auspician')),
                ('localizacioncurso', models.CharField(help_text='Cómo obtener las coordenadas de un lugar <br> 1. ir a www.latlong.net <br> 2. Introducir la direccion: ej. Rioja 2045, Rosario, Santa Fe<br>3.Dar al boton Find <br> 4. Aparecera una marca azul en el mapa si ve que no esta exactamente haga doble click en la localizacion exacta<br>5. Listo copie la latitud y longitud tal cual.<br><br>En el campo de localizacion debe introducir de esta forma esos datos incluidos las llaves:<br>{lat: -32.952881, lng: -60.655832}', max_length=400, verbose_name='Localizacion (Coordenadas)')),
                ('order', models.SmallIntegerField(default=0, verbose_name='Orden')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'ordering': ['-fechacurso'],
                'verbose_name_plural': 'cursos',
                'verbose_name': 'curso',
            },
        ),
    ]
