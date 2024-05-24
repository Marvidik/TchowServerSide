from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Junks,Foods,Restaurant,Order
from .serializers import FoodsSerializer,RestaurantSerializer,OrderSerializer
# Create your views here.


@api_view(['GET'])
def restaurants(request):
    data=Restaurant.objects.all()

    serializer=RestaurantSerializer(instance=data,many=True)

    return Response({'restaurants': serializer.data}, status=status.HTTP_200_OK)

@api_view(["GET"])
def restaurant_food(request,id):

    data=Foods.objects.filter(restaurant=id)
    serializer=FoodsSerializer(instance=data, many=True)

    return Response({'Foods': serializer.data}, status=status.HTTP_200_OK)

    

@api_view(['GET'])
def view_orders(request, id):
    orders = Order.objects.filter(user=id)
    order_data = []
    
    for order in orders:
        order_details = OrderSerializer(order).data
        food_details = None
        junk_details = None
        
        # Fetch food details if available
        if order.real_food:
            food_details = {
                'name': order.real_food.name,
                'image': order.real_food.image.url,
                'rating': order.real_food.rating,
                'deliveryfee': order.real_food.deliveryfee,
                'category': order.real_food.category,
                'availability': order.real_food.availability,
                'price': order.real_food.price
            }
 
        order_details['food_details'] = food_details
        order_data.append(order_details)

    return Response({'Orders': order_data}, status=status.HTTP_200_OK)

@api_view(["POST"])
def add_to_order(request):

    serializer= OrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({'Orders':"Orders Successfuly Added"}, status=status.HTTP_200_OK)
    else:
        return Response({'Order':"error"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["PATCH"])
def received(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({"message": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PATCH":
        serializer = OrderSerializer(order, data={'delivered': True}, partial=True)
        if serializer.is_valid():
            serializer.save()  # Commit changes to the database
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def search(request, query):
    restaurants = Restaurant.objects.filter(name__icontains=query)
    foods = Foods.objects.filter(name__icontains=query)

    restaurant_results = []
    food_results = []

    for restaurant in restaurants:
        foods_of_restaurant = Foods.objects.filter(restaurant=restaurant)
        serializer = FoodsSerializer(foods_of_restaurant, many=True)
        restaurant_data = {
            "restaurant": restaurant.name,
            "foods": serializer.data
        }
        restaurant_results.append(restaurant_data)

    for food in foods:
        serializer = FoodsSerializer(food)
        food_results.append(serializer.data)

    results = {
        "restaurants": restaurant_results,
        "foods": food_results
    }

    return Response(results)


@api_view(['GET'])
def search_food(request, query,id):
    restaurants = Restaurant.objects.get(id=id)
    foods = Foods.objects.filter(name__icontains=query,restaurant=restaurants)

    
    food_results = []

    for food in foods:
        serializer = FoodsSerializer(food)
        food_results.append(serializer.data)

    results = {
       
        "foods": food_results
    }

    return Response(results)