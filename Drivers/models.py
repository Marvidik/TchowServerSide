from django.db import models
from django.contrib.auth.models import User

# Create your models here.

choices=(
    ("Available","Available"),
    ("Unavailable","Unavailable")
)


class Drivers(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.IntegerField()
    location=models.CharField(max_length=100)
    balance=models.IntegerField()
    availability=models.CharField(max_length=100, choices=choices  )
    
