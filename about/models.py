from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='media/photos/', null=True, blank=True)
    def __str__(self):
        return self.name