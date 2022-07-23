from rest_framework import serializers
from .models import Guest,Order,Purchase_History,Cart,Address

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'
        
        
        # ('id', 'first_name', 'last_name', 'username','password', 'email', 'rewards_points', 'birthday', 'favorite_flavor')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'flavor', 'occasion', 'frosting_level', 'decoration', 'message_card', 'size', 'qty', 'cart')

class Purchase_HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase_History
        fields = ('id', 'guest', 'order_date', 'total')

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model =Cart 
        fields = ('id', 'guest', 'price')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'street_address', 'city', 'state','zip_code', 'guest')