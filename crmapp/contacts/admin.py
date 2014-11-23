from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'uuid')

admin.site.register(Contact, ContactAdmin)
