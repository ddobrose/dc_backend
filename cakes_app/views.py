# from typing_extensions import Self
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GuestSerializer,CartSerializer,Purchase_HistorySerializer,OrderSerializer,AddressSerializer
from .models import Guest,Order,Purchase_History,Cart,Address

# Create your views here.
class GuestView(viewsets.ModelViewSet):
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()

class CartView(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    

class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class Purchase_HistoryView(viewsets.ModelViewSet):
    serializer_class = Purchase_HistorySerializer
    queryset = Purchase_History.objects.all()

class AddressView(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

class CartOrderView(viewsets.ModelViewSet):
    serializer_class= OrderSerializer
    def get_queryset(self):
         cart = self.kwargs["cart"]
         return Order.objects.filter(cart=cart)
    
    # queryset = Order.objects.filter(cart=2)


