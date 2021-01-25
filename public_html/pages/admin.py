from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'codigo',)
    readonly_fields = ('created', 'updated')
    search_fields = ('title','codigo',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    #exclude = ('order',)

    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }

admin.site.register(Page, PageAdmin)
