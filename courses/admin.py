from django.contrib import admin
from .models import Course, Category

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category','weekday_datetime','weekends_datetime', 'is_published', 'is_next_event')

    ordering = ('weekday_datetime',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )

admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)