from django.contrib import admin

from .models import Team

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    display_links = ('name',)

admin.site.register(Team, TeamAdmin)
