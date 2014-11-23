from django.contrib import admin
from .models import Communication

class CommunicationAdmin(admin.ModelAdmin):
    list_display = ('subject', 'uuid')

admin.site.register(Communication, CommunicationAdmin)
