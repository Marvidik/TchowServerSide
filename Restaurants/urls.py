from django.urls import path
from .views import *
urlpatterns = [
    path('company/<id>/',vendor,name="restaurant"),
    path('food/<id>/',vendor_food,name="restaurant-food"),
    path('food/<int:id>/update_availability/', update_food_availability, name='update-food-availability'),
    
]
