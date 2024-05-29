from django.urls import path
from .views import *

urlpatterns = [
    path("drivers",company_drivers,name="company_drivers"),
    path("sentOrders",sent_orders,name="Drivers_orders"),
    path("sendorder",add_to_drivers_order,name="Send_order"),
]
