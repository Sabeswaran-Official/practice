from django.urls import path
from .views import *

urlpatterns = [
    path('all/customers/', CustomerList),
    path('add/customers/', CustomerAdd),
    path('Update/customer/<int:id>/', CustomerUpdate, name='customer_update'),
    path('Delete/customer/<int:id>/', CustomerDelete, name='customer_delete'),

    path('orders/', OrdersList),
    path('add/orders/', OrdersAdd),
    path('delete/order/<int:id>/', OrdersDelete, name='order_delete'),
    path('update/order/<int:id>/', OrdersUpdate, name='order_update'),
]