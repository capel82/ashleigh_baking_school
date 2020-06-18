from django.contrib import admin
from .models import Course, Category, SubCategory

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category','day','course_datetime', 'is_published', 'is_next_event')

    ordering = ('course_datetime',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)