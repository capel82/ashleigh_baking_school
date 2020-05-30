from django.db import models
from datetime import datetime

# Create your models here.
class Course(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length =50)
    learn_list1 = models.CharField(max_length=250)
    learn_list2 = models.CharField(max_length=250)
    learn_list3 = models.CharField(max_length=250, blank=True)
    completion_list1 = models.CharField(max_length=250)
    completion_list2 = models.CharField(max_length=250, blank=True)
    weekday_datetime = models.DateTimeField()
    weekends_datetime = models.DateTimeField()
    photo_course = models.ImageField(upload_to='media/photos/%Y/%m/%d/')
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

