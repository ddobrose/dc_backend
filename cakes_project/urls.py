"""cakes_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from cakes_app import views

from rest_framework_simplejwt.views import(
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'guest', views.GuestView, 'guest')
router.register(r'order', views.OrderView, 'order')
router.register(r'cart', views.CartView, 'cart')
router.register(r'user', views.UserView, 'user')
# router.register(r'purchase_history', views.Purchase_HistoryView, 'purchase_history')
# router.register(r'address', views.AddressView, 'address')
router.register(r'cartorders/(?P<cart>\d+)',views.CartOrderView,'cartorders')
router.register(r'userguest/(?P<user>\d+)',views.UserGuestView,'userguest')
router.register(r'usercart/(?P<user>\d+)',views.UserCartView,'usercart')
router.register(r'pastorders/(?P<user>\d+)',views.PastOrderView,'pastorders')
# router.register(r'cart/int:pk/orders/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("cakes_app.urls")),
    path('ddcakes/', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    
]
