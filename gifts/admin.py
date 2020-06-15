from django.contrib import admin
from .models import Gift, Category

# Register your models here.
class GiftAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )

admin.site.register(Gift, GiftAdmin)
admin.site.register(Category, CategoryAdmin)