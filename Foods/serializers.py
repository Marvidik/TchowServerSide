from rest_framework.serializers import ModelSerializer
from .models import Foods,Restaurant,Order

from rest_framework import serializers



class RestaurantSerializer(ModelSerializer):

    class Meta:
        model=Restaurant
        fields="__all__"



class FoodsSerializer(ModelSerializer):


    class Meta:
        model=Foods
        fields="__all__"




class OrderSerializer(ModelSerializer):

    class Meta:
        model=Order
        fields="__all__"

