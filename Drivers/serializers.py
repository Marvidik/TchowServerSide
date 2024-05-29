from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Drivers,DriversOrder


#  user serializer
class DriversSerializer(serializers.ModelSerializer):
    
    class Meta(object):
        model = Drivers
        fields = '__all__'


class DriversOrderSerializer(serializers.ModelSerializer):
    
    class Meta(object):
        model=DriversOrder
        fields='__all__'



