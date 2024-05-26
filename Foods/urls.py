from django.urls import path
from .views import *
urlpatterns = [
    path('restaurants/',restaurants,name="restaurant"),
    path('restaurant/food/<id>',restaurant_food,name="restaurant-food"),

    path('delivered/<pk>',received,name="received"),
    path("addorder/",add_to_order,name="add-order"),
    path("vieworder/<id>",view_orders,name="view-orders"),

    path('search/<str:query>/', search, name='search'),
    path('foodsearch/<id>/<str:query>/', search_food, name='search2'),
]
