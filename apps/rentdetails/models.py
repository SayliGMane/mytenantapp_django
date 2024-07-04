from django.db import models

# Create your models here.
#from django.contrib.auth.models import AbstractUser   

   
class RentDetails(models.Model):
    flatno = models.ForeignKey('flatdetails.FlatDetails', on_delete=models.CASCADE)
    tenantid = models.CharField(max_length=5, primary_key=True)
    contractstartdate = models.DateField(null=True, blank=True)
    contractenddate = models.DateField(null=True, blank=True)
    rent = models.IntegerField()

    class Meta:
        db_table = 'private_data.rent_details'
        constraints = [
            models.CheckConstraint(check=models.Q(contractstartdate__lt=models.F('contractenddate')), name='rent_details_check')
        ]

    def __str__(self):
        return f"Tenant ID: {self.tenantid}, Flat No: {self.flatno}"
