from django.contrib import admin
from .models import Course, Category, SubCategory

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category','day','course_datetime', 'is_published', 'is_next_event')
    list_display_links = ('id', 'title')
    list_filter = ('subcategory',)
    list_editable = ('is_published', 'is_next_event')
    list_per_page = 15
    search_fields = ('title', 'description1','description2', 'learn_list1', 
                    'learn_list2','learn_list3','completion_list1',
                    'completion_list2','course_datetime', 'day')

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