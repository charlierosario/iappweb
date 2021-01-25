from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import PersonaList, add_persona


prueba_patterns = ([
    path('', add_persona, name='plist'),
    path('listar/', login_required(PersonaList.as_view()), name='padd'),
    ], "inscripcion")
