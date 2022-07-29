# from typing_extensions import Self
from django.shortcuts import render
from rest_framework import viewsets,generics,status
from .serializers import GuestSerializer,CartSerializer,OrderSerializer
from .models import Guest,Order,Cart
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.http import JsonResponse
from cakes_app.serializers import MyTokenObtainPairSerializer,RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny,IsAuthenticated

# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/'
    ]
    return Response(routes)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == 'GET':
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.POST.get('text')
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)


class GuestView(viewsets.ModelViewSet):
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()

class CartView(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    

class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

# class Purchase_HistoryView(viewsets.ModelViewSet):
#     serializer_class = Purchase_HistorySerializer
#     queryset = Purchase_History.objects.all()

# class AddressView(viewsets.ModelViewSet):
#     serializer_class = AddressSerializer
#     queryset = Address.objects.all()

class CartOrderView(viewsets.ModelViewSet):
    serializer_class= OrderSerializer
    def get_queryset(self):
         cart = self.kwargs["cart"]
         return Order.objects.filter(cart=cart)
    
    # queryset = Order.objects.filter(cart=2)


