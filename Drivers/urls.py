from django.urls import path
from .views import *

urlpatterns = [
    path("profile/<id>",driver,name="driver"),
    path("myOrders/<id>",drivers_order,name="myorders"),
    path("delivered",delivered,name="delivered"),
    path("accepted",accepted,name="accepted"),
    path("moving",moving,name="moving"),
]
