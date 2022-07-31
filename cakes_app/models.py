
from django.db import models
from django.contrib.auth.models import User
import uuid

FLAVOR_CHOICES = [
        ("Very Vanilla","Very Vanilla"),
        ("Crazy Coco","Crazy Coco"),
        ("Sweetie Strawberry","Sweetie Strawberry"),
        ("Birthday Bonanza","Birthday Bonanza"),
        ("Loco Lemon","Loco Lemon"),
        ("White Coco Razz","White Coco Razz"),
        ("Gluten Free Cookie Craze","Gluten Free Cookie Craze"),
        ("Ridiculous Red Velvet","Ridiculous Red Velvet"),
        ("Scintillating Cinnamon","Scintillating Cinnamon"),
        ("Crisp Carrot","Crisp Carrot"),
        ]
FROSTING = [
    ("None", "None"),
    ("Drizzle", "Drizzle"),
    ("Normal", "Normal"),
    ("Extra", "Extra")
]
DECO_OPTIONS = [
    ("Happy Birthday", "Happy Birthday"),
    ("Graduation", "Graduation"),
    ("Independence Day", "Independence Day"),
    ("Thank You", "Thank You"),
    ("Just Because", "Just Because"),
    ("None", "None")
]
SIZE_OPTIONS = [
    ("Dozen Cupcakes", "Dozen Cupcakes"),
    ("Personal Size Cake", "Personal Size Cake"),
    ("Triple Tower Personal Size Cakes", "Triple Tower Personal Size Cakes"),
    ("12 box of Personal Size Cakes","12 box of Personal Size Cakes"),
    ("8 Inch Cake", "8 Inch Cake"),
    ("10 Inch Cake", "10 Inch Cake"),
    ("Layered Cake(10in bottom 8in top)", "Layered Cake(10in bottom 8in top)")
]

PAYMENT_OPTIONS = [
    ("CRD", "Credit"),
    ("DBT", "Debit")
]

# Create your models here.
class Guest(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    # username = models.CharField(max_length=100, unique=True,blank=False)
    # password = models.CharField(max_length=20, blank=False)
    email = models.CharField(max_length=100, unique=True, blank=True)
    rewards_points:models.IntegerField(default=50)
    # birthday = models.DateField(blank=False)
    favorite_flavor = models.CharField(max_length= 40, choices = FLAVOR_CHOICES, default = "Very Vanilla")

    def __str__(self):
        return self.user.username

# class Purchase_History(models.Model):
#     guest= models.ForeignKey(Guest, on_delete=models.CASCADE,related_name="purchase_history")
#     # order_id = models.IntegerField(primary_key=True, default=uuid.uuid4, editable=False)
#     order_date = models.DateTimeField(auto_now=True)
#     total = models.IntegerField()

    # def __str__(self):
    #     return self.total

class Cart(models.Model):
    guest= models.ForeignKey(Guest, on_delete=models.CASCADE,null=True, related_name="cart")
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    price= models.DecimalField(decimal_places=2,max_digits=10)
    previous= models.BooleanField(default=False)
    # purchase_history=models.ForeignKey(Purchase_History, on_delete=models.CASCADE)

    def __int__(self):
        return self.guest

class Order(models.Model):
    flavor = models.CharField(max_length=100, choices=FLAVOR_CHOICES, blank=False  )
    occasion = models.CharField(max_length=100, blank=True)
    frosting_level= models.CharField(max_length=100, choices=FROSTING, default="Normal")
    decoration = models.CharField(max_length=100, choices=DECO_OPTIONS, default="None")
    message_card = models.CharField(max_length=200, blank=True)
    size = models.CharField(max_length=100, choices=SIZE_OPTIONS, blank=False)
    qty = models.IntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, related_name='orders')
    price = models.DecimalField(null=True,max_digits=10, decimal_places=2)

    def __str__(self):
        return self.cart.guest.user.username



# class Address(models.Model):
#     street_address = models.CharField(max_length=200,blank=False)
#     city = models.CharField(max_length=200,blank=False)
#     state = models.CharField(max_length=100,blank=False)
#     zip_code = models.IntegerField( blank=False)
#     guest = models.ForeignKey(Guest,on_delete=models.CASCADE,related_name="address")



# class Payment_Method():
#     guest: models.ForeignKey(Guest, on_delete=models.CASCADE)
#     payment_type: models.CharField(max_length=100, choices=PAYMENT_OPTIONS)
#     name_on_card: models.CharField(max_length=100, blank=False)
#     card_number: models.IntegerField(max_length=16,blank=False)
#     cvv: models.IntegerField(max_length=3, blank=False)
#     exp: models.IntegerField(max_length=4,blank=False)

