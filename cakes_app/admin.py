from django.contrib import admin
from .models import Guest,Cart,Address,Purchase_History,Order
# Register your models here.
admin.site.register(Guest)
admin.site.register(Cart)
admin.site.register(Address)
admin.site.register(Purchase_History)
admin.site.register(Order)
