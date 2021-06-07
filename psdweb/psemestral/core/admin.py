from django.contrib import admin
from .models import user, contacto
# Register your models here.


class useredit(admin.ModelAdmin):
    list_display = ["nom", "snom", "email", "password"]
    list_editable = ["snom"]
    search_fields = ["nom"]



admin.site.register(user, useredit)
admin.site.register(contacto)