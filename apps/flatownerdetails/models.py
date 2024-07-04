from django.db import models
#from django.contrib.postgres.fields import JSONField
# Create your models here.
#from django.contrib.auth.models import AbstractUser   

class FlatOwnerDetails(models.Model):
    flat_owner_id = models.AutoField(primary_key=True)
    flatno = models.ForeignKey('flatdetails.FlatDetails', on_delete=models.CASCADE)
    bank_details = models.CharField(max_length=200)
    owner = models.JSONField()

    class Meta:
        db_table = 'private_data.flat_owner_details'

    def __str__(self):
        return f"Flat Owner ID: {self.flat_owner_id}, Flat No: {self.flatno}"

