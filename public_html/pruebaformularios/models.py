from django.forms import ModelForm, TextInput, Textarea
from django.db import models
from django import forms


class Persona(models.Model):

    GENDER_CHOICES = (
        ('NO', 'NO'),
        ('SI', 'SI'),
    )
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=60, verbose_name="Apellido")
    dni = models.CharField(help_text="Dni válido ej. 22222222", max_length=8)
    direccion = models.CharField(max_length=100, verbose_name="Localidad", help_text="Ej. Rosario 2000")
    telefono = models.CharField(max_length=18)
    email = models.EmailField()
    procurador = models.CharField(max_length=2, choices=GENDER_CHOICES)
    codigocurso = models.CharField(max_length=7, blank=True)
    nombrecurso = models.CharField(max_length=60, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'

    def __str__(self):
        return self.dni

    def save(self, force_insert=False, force_update=False):
        self.nombre = self.nombre.upper()
        self.apellidos = self.apellidos.upper()
        self.direccion = self.direccion.upper()
        super(Persona, self).save(force_insert, force_update)


class PersonaForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = ''
        self.fields['apellidos'].label = ''
        self.fields['dni'].label = ''
        self.fields['direccion'].label = ''
        self.fields['telefono'].label = ''
        self.fields['email'].label = ''
        self.initial['procurador'] = 'NO'

        #self.fields['house'].widget.attrs['size'] = '1'
        #self.fields['house'].style = 'font-size:13px;width:60px;'

    class Meta:

        model = Persona
        fields = ('nombre', 'apellidos', 'dni', 'direccion', 'telefono', 'email', 'procurador', 'codigocurso', 'nombrecurso')
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre', 'onkeyup' : 'this.value = this.value.toUpperCase();'}),
            'apellidos': forms.TextInput(attrs={'placeholder': 'Apellido', 'onkeyup' : 'this.value = this.value.toUpperCase();'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Localidad', 'onkeyup' : 'this.value = this.value.toUpperCase();'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Telefono', 'onKeypress': 'if (event.keyCode < 45 || event.keyCode > 57) event.returnValue = false;'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'procurador': forms.Select(attrs={'style': 'font-size:13px;width:60px;'}),
            'dni': forms.TextInput(attrs={'minlength': '8', 'placeholder': 'Dni', 'onKeypress': 'if (event.keyCode < 45 || event.keyCode > 57) event.returnValue = false;'}),
        }
