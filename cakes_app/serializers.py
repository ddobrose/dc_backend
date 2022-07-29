from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from .models import Guest,Order,Cart

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model= User
        fields = ('username', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields did not match."}
            )
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username= validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'
        
        
        # ('id', 'first_name', 'last_name', 'username','password', 'email', 'rewards_points', 'birthday', 'favorite_flavor')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'flavor', 'occasion', 'frosting_level', 'decoration', 'message_card', 'size', 'qty', 'cart','price')

# class Purchase_HistorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Purchase_History
#         fields = ('id', 'guest', 'order_date', 'total')

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model =Cart 
        fields = ('id', 'guest', 'price')

# class AddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Address
#         fields = ('id', 'street_address', 'city', 'state','zip_code', 'guest')