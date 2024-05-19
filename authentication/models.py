from django.db import models
from django.contrib.auth.models import User
import time

# Create your models here.

#model for the password reset token  
class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    timestamp = models.IntegerField()  # Stores timestamp in seconds

    def __str__(self):
        return f"{self.user} - {self.token[:10]}"  # Truncate token for display

    def is_valid(self):
        # Logic to expire the token after 3 minutes 
        expiration_time = 180
        return (int(time.time()) - self.timestamp) < expiration_time



class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=100,null=True)
    phone=models.IntegerField(null=True)
    phone1=models.IntegerField(null=True)


    def __str__(self):

        return self.user.username


class OTP(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    otp=models.CharField(max_length=5)


