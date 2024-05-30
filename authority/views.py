from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response


from Drivers.models import Drivers,DriversOrder
from Drivers.serializers import DriversSerializer,DriversOrderSerializer
from Foods.models import Order
from Foods.serializers import OrderSerializer
# Create your views here.


@api_view(['GET'])
def company_drivers(request):
    data=Drivers.objects.all()

    serializer=DriversSerializer(instance=data,many=True)

    return Response({'drivers': serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def sent_orders(request):
    data=DriversOrder.objects.all()

    serializer=DriversOrderSerializer(instance=data,many=True)

    return Response({'orders': serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def user_orders(request):
    data=Order.objects.all()

    serializer=OrderSerializer(instance=data,many=True)

    return Response({'orders': serializer.data}, status=status.HTTP_200_OK)


@api_view(["POST"])
def add_to_drivers_order(request):
    serializer= DriversOrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({'Orders':" Drivers Orders Successfuly Added"}, status=status.HTTP_200_OK)
    else:
        return Response({'Order':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)