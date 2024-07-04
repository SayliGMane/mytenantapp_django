from django.db import models

# Create your models here.
#from django.contrib.auth.models import AbstractUser   

class TenantDetails(models.Model):
   GENDER= {
        "F"  : "F",
        "M" : "M"}
   tenantid = models.CharField(max_length=50,primary_key=True)
   tenantname = models.TextField(unique=True)
   gender = models.CharField(max_length=1, choices=GENDER)
   permanentaddress = models.CharField(max_length=70)
   occupation = models.TextField()
   uid_number = models.CharField(max_length=10)
   contactnumber = models.CharField(max_length=12,default="91")

   class Meta:
      db_table = 'private_data.tenant_details'

   def __str__(self):
      return f"Tenant Name: {self.tenantname}, Tenant ID: {self.tenantid}"