from django.contrib import admin
from .models import Organisations

class OrganisationsAdmin(admin.ModelAdmin):
    list_display=(
        'name',
        'position',
        
    )

admin.site.register(Organisations, OrganisationsAdmin)
