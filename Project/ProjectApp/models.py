from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name =models.CharField(max_length=20)
    last_name =models.CharField(max_length=20)
    mobile_number =models.CharField(max_length=20)
    email =models.EmailField(max_length=20)
    
    def __str__(self):
        return self.first_name
    
class Contact_us(models.Model):
    name=models.CharField(max_length=20)
    email =models.EmailField(max_length=20)
    mobile_number =models.CharField(max_length=10)
    message=models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name