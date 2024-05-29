from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Drivers,DriversOrder
from .serializers import DriversSerializer,DriversOrderSerializer
# Create your views here.


@api_view(['GET'])
def driver(request,id):
    data=Drivers.objects.filter(user=id)

    serializer=DriversSerializer(instance=data,many=True)

    return Response({'driver': serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def drivers_order(request,id):
    data=DriversOrder.objects.filter(driver=id)

    serializer=DriversOrderSerializer(instance=data,many=True)

    return Response({'orders': serializer.data}, status=status.HTTP_200_OK)

@api_view(["PATCH"])
def delivered(request, pk):
    try:
        order = DriversOrder.objects.get(pk=pk)
    except DriversOrder.DoesNotExist:
        return Response({"message": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PATCH":
        serializer = DriversOrderSerializer(order, data={'status': "Delivered"}, partial=True)
        if serializer.is_valid():
            serializer.save()  # Commit changes to the database
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["PATCH"])
def accepted(request, pk):
    try:
        order = DriversOrder.objects.get(pk=pk)
    except DriversOrder.DoesNotExist:
        return Response({"message": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PATCH":
        serializer = DriversOrderSerializer(order, data={'status': "Accepted"}, partial=True)
        if serializer.is_valid():
            serializer.save()  # Commit changes to the database
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["PATCH"])
def moving(request, pk):
    try:
        order = DriversOrder.objects.get(pk=pk)
    except DriversOrder.DoesNotExist:
        return Response({"message": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PATCH":
        serializer = DriversOrderSerializer(order, data={'status': "En Route"}, partial=True)
        if serializer.is_valid():
            serializer.save()  # Commit changes to the database
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


