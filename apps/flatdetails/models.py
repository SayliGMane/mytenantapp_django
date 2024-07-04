from django.db import models
from django.contrib.auth.models import AbstractUser   


class FlatDetails(AbstractUser):
    
    FLAT_TYPES = [
        ('2BHK', '2BHK'),
        ('1BHK', '1BHK'),
        ('Shop', 'Shop'),
    ]
    
    FURNISHED_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    flatno = models.AutoField(primary_key=True)
    floorno = models.IntegerField(null=True, blank=True)
    furnished = models.CharField(max_length=3, choices=FURNISHED_CHOICES)
    facilities = models.JSONField(null=True, blank=True)
    propertytype = models.CharField(max_length=5, choices=FLAT_TYPES)
    area_in_m2 = models.IntegerField(null=True, blank=True)
    price_range = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    available_from = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Flat {self.flatno} ({self.propertytype})"