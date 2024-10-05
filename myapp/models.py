from django.db import models

# Create your models here.
class model(models.Model):

   
       
    address=models.CharField(max_length=1000,null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    

    