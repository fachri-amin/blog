from django.contrib import admin

# Register your models here.
from .models import ArtikelModel

class ArtikelModelAdmin(admin.ModelAdmin):
    readonly_fields=[
        'slug',
        'published',
        'updated',
    ]

admin.site.register(ArtikelModel, ArtikelModelAdmin)