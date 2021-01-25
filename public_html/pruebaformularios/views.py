from django.views.generic import View, ListView
from django.shortcuts import render, redirect
#from django.core.mail import EmailMessage
from django.core.mail import send_mail
from .models import Persona
from .models import PersonaForm
from pages.models import Page
from .filters import SnippetFilter
from datetime import datetime
from django.utils import formats


class PersonaList(ListView):
    template_name = "pruebaformularios/personas_list.html"
    model = Persona

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['filter'] = SnippetFilter(self.request.GET, queryset=self.get_queryset())
        return context


def add_persona(request):
    
    form_class = PersonaForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            datos = form.cleaned_data['email']
            nombre_f = form.cleaned_data['nombre']
            apellido_f = form.cleaned_data['apellidos']
            dni_f = form.cleaned_data['dni']
            nombreyapellido_f = nombre_f + " " + apellido_f
            nombrecurso_f = form.cleaned_data['nombrecurso']
            codigocurso_f = form.cleaned_data['codigocurso']
            nombre_f = nombre_f.upper()
            apellido_f = apellido_f.upper()
            date_joined = datetime.now()
            formatted_datetime = formats.date_format(date_joined, "d/m/Y H:m:s")
            
            per_existe = Persona.objects.filter(dni=dni_f, codigocurso=codigocurso_f).exists()
            if per_existe:
                return render(request, 'pruebaformularios/fail.html')
            else:
                #print('NO')
                html_message = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
                <html xmlns="http://www.w3.org/1999/xhtml">
                <head>
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
                </head>
                <body style="margin: 0; padding:0;">
                <table border="0"  cellpadding="0" cellspacing="0" width="100%">
                <tr bgcolor="white">
                <td>
                <table align="center" border="0" cellpadding="0" cellspacing="0" width="600" style="border-bottom: 2px solid #eaeaea;">
                <tr>
                <td bgcolor="white" style="padding: 0px 0px 10px 0px">
                <center>
                <img src="https://iapprosario.com/media/TITMAIL3.png" alt="Smiley face" />
                </center>
                </td>
                </tr>
                </table>
                </td>
                </tr>
                <tr bgcolor="white">
                <td>
                <table bgcolor="#ffffff" align="center" border="0" cellpadding="0" cellspacing="0" width="600" style="border-collapse: collapse;">
                <tr>
                <td style="padding: 20px">
                <table  bgcolor="#ffffff" style="border-bottom: 2px solid #eaeaea;" border="0" cellpadding="0" cellspacing="0" width="100%"><br>
                Gracias """ + nombreyapellido_f + """&nbsp; por preinscribirse.
			    Por favor imprima el comprobante y recorte por las lineas punteadas o por el simbolo igual,
                deberá entregar y abonar el comprobante de preinscripción en el colegio de procuradores, en la fecha prevista. <br>
    
                <b><u>Por favor tome nota de la siguiente información</u></b><br>

                <br>Recuerde acudir con DNI al momento de abonar el arancel.<br>
                Si es procurador debera acreditar la condición de tal al momento del pago.<br>
                Podrá abonar la inscripción en efectivo en el Colegio de Procuradores de 8.30 a 12.30<br>
                (Balcarce 1651, Planta Baja Tribunales Rosario).<br>

                <br>También puede abonar por transferencia o depósito bancario:<br>
                <b><u>Datos Bancarios:</u></b><br>
                CUIT: 30-68547215-1<br>
                Banco: Nuevo Banco de Santa Fe<br>
                Sucursal: AG Tribunales Rosario<br>
                Cuenta: 00803027166/06<br>
                Cbu: 3300008220080027166068<br>
                Una vez realizado el pago deberá enviar al correo electrónico colprocuradores@arnetbiz.com.ar<br>
                desde el email que ud registro en el formulario, los siguientes datos:<br>
                – Nombre y apellido<br>
                – Dni<br>
                – Foto del comprobante de preinscripcion.<br>
			    – Foto del comprobante de deposito o transferencia.<br>
                <tr>
                <td style="color: #53545e;font-weight: bold;font-family: Arial, Verdana, sans-serif;padding: 25px 0px 25px 0px;"><br>
                <img src="https://iapprosario.com/media/tijera.png" alt="Smiley face"  WIDTH=30 HEIGHT=30 />
                ------------------------------------------------------------------------------------<br>
                =================================================================<br>
                <br>Comprobante de preinscripción<br>
                _________________________________________________________________<br>
                <br><b>Nombre de la jornada/curso:</b> """+ nombrecurso_f +""" <br>
                <br><b>Código del curso: </b> """ + codigocurso_f + """ <br>
                _________________________________________________________________<br>
                <br><b>Nombre y Apellido:</b> """ + nombreyapellido_f + """ <br>
                <b>Dni:</b> """ + dni_f + """ <br>
                <b>Fecha / Hora de inscripción: </b>""" + formatted_datetime + """<br>
                <br>
                =================================================================<br>
                --------------------------------------------------------------------------------------<br>
                </td>
                </tr>
                </table>
                </td>
                </tr>                       
                </table>
                </td>
                </tr>   
                <tr>
                <td style="padding: 35px 0px 50px 0px">
                <center>
                Para mas  información visite nuestro sitio web<br>
                <a href="https://www.iapprosario.com" style="background-color: #53545e;padding: 5px 10px;color: #ffffff;text-decoration: none;font-family: Arial, Verdana, sans-serif;"><br>Visitar web</a> 
                </center>
                </td>
                </tr>    
                </table>
                </body>
                </html>"""
       
                email_body="Gracias por preinscribirse, recuerde abonar el arancel dentro de la fecha prevista."
                #email = EmailMessage('Gracias por inscribirse a la Jornada.', email_body,
                #'IAPP Rosario <noresponder@iapprosario.com>', to=[datos], faili)
                #email.content_subtype = "html"  # Main content is now text/html
                #email.send()
                send_mail(
                'Gracias por inscribirse a la Jornada.',
                email_body,
                'IAPP Rosario <noresponder@iapprosario.com>',
                [datos],
                fail_silently=False, html_message=html_message
                )
                new_persona = form.save()
                form = PersonaForm()
                return render(request, 'pruebaformularios/gracias.html')
    return render(request, 'pruebaformularios/persona_form.html', {'form': form})

