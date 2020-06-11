from django.contrib import admin

from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact_date', 'name', 'phone_number', 'email')
    display_links = ('contact_date', 'name')
    search_fields = ('name', 'email')
    ordering = ('-contact_date',)

admin.site.register(Contact, ContactAdmin)
