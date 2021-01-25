from django.contrib import admin
from .models import Persona


class PageAdmin(admin.ModelAdmin):
    list_display = ('dni','nombre', 'apellidos', 'codigocurso')
    readonly_fields = ('codigocurso','created','updated')
    ordering = ("-dni", "codigocurso",)
    search_fields = ('dni','apellidos','nombre', 'codigocurso')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    exclude = ('nombrecurso',)

    class Media:
        css = {'all': ('pages/css/custom_ckeditor.css',)}


admin.site.register(Persona, PageAdmin)
# Register your models here.
