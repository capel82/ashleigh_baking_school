from django.db import models
from datetime import datetime

from about.models import Team

# Create your models here.
class Course(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    subcategory = models.ForeignKey('Subcategory', null=True, blank=True, on_delete=models.SET_NULL)
    team = models.ForeignKey('about.Team', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length =50)
    description1 = models.CharField(max_length=200, blank=True)
    learn_list1 = models.CharField(max_length=250, blank=True)
    learn_list2 = models.CharField(max_length=250, blank=True)
    learn_list3 = models.CharField(max_length=250, blank=True)
    description2 = models.CharField(max_length=200, blank=True)
    completion_list1 = models.CharField(max_length=250, blank=True)
    completion_list2 = models.CharField(max_length=250, blank=True)
    day = models.CharField(max_length=20, blank=True)
    course_datetime = models.DateTimeField(null=True, blank=True)
    photo_course = models.ImageField(upload_to='media/photos/', null=True, blank=True)
    is_next_event = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    price = models.IntegerField()
    def __str__(self):
        return self.title


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    title = models.CharField(max_length=254)

    def __str__(self):
        return self.title

class SubCategory(models.Model):

    class Meta:
        verbose_name_plural = 'Subcategories'
        
    title = models.CharField(max_length=254)

    def __str__(self):
        return self.title
