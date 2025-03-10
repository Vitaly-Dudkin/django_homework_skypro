from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='description')
    image = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name='image')
    purchase_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='date_of_creation')
    last_modified_date = models.DateTimeField(auto_now=True, verbose_name='last_modified_date')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
