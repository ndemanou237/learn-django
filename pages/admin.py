from django.contrib import admin
from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name','email','create_at','is_treated')
    list_filter = ('is_treated','create_at')
    search_fields = ('name','email')

admin.site.register(ContactMessage,ContactMessageAdmin)
