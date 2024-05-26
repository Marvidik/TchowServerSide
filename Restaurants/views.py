from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404


from Foods.models import Restaurant,Foods
from Foods.serializers import RestaurantSerializer,FoodsSerializer
# Create your views here.


@api_view(['GET'])
def vendor(request, id):
    try:
        restaurant = Restaurant.objects.get(id=id)
    except Restaurant.DoesNotExist:
        raise Http404

    serializer = RestaurantSerializer(restaurant)
    return Response({'restaurant': serializer.data}, status=status.HTTP_200_OK)

@api_view(["GET"])
def vendor_food(request,id):

    data=Foods.objects.filter(restaurant=id)
    serializer=FoodsSerializer(instance=data, many=True)

    return Response({'Foods': serializer.data}, status=status.HTTP_200_OK)


@api_view(['PATCH'])
def update_food_availability(request, id):
    food = get_object_or_404(Foods, id=id)
    if 'availability' not in request.data:
        return Response({'error': 'Availability field is required.'}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = FoodsSerializer(food, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'food': serializer.data}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)