from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Signup(models.Model):
    Name=models.CharField(max_length=15,default='')
    Age=models.IntegerField(default='')
    Place=models.CharField(max_length=15,default='')
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)
    Email=models.EmailField(default='')
    Password=models.CharField(max_length=12,default='')
class Pictures(models.Model):
    Car=models.CharField(max_length=50,default='')
    Image=models.ImageField(upload_to='images/')
    Brand=models.CharField(max_length=20,default='')
    Details=models.CharField(max_length=50,default='')
    