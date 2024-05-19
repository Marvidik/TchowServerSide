from django.contrib import admin
from .models import PasswordResetToken,OTP,Profile

# Register your models here.
admin.site.register(PasswordResetToken)
admin.site.register(OTP)
admin.site.register(Profile)