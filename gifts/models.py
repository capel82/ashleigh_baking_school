from django.db import models

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    title = models.CharField(max_length=254)

    def __str__(self):
        return self.title

class Gift(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length =50)
    image = models.ImageField(upload_to='media/photos/', null=True, blank=True)
    price = models.IntegerField()
    def __str__(self):
        return self.title

