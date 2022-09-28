from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=99)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f'{self.name} - {self.quantity}'
