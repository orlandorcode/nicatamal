from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # additional classes
    profile_pic = models.ImageField(upload_to='profile_pics', blank = True)
    
    def __str__(self):
        return self.user.username

def utc_tomorrow():
    return datetime.utcnow() + timedelta(days=1)

class ClientType(models.Model):
    usertype_id = models.AutoField(primary_key = True)
    type_name = models.CharField(max_length = 264, unique = True)
    
    def __str__(self):
        return self.type_name

class Product(models.Model):
    name = models.CharField(primary_key = True, max_length = 264, unique = True)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(primary_key = True, max_length = 264)
    clienttype_id = models.ForeignKey(ClientType, on_delete = models.PROTECT)
    email = models.CharField(default = 'null', max_length = 264, unique = False)
    telephone = models.CharField(default = 'null', max_length = 264, unique = False)
    address = models.TextField(max_length = 264, default = 'null')
    address_2 = models.TextField(max_length = 264, default = 'null')
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    
    ENTREGADO = 'ENT'
    PROCESO = 'PROC'
    NOENTREGADO = 'NOT'
    
    completed_choices = [(ENTREGADO,'Entregado'),(PROCESO,'En proceso'),(NOENTREGADO,'No se entregó')]
    
    client = models.ForeignKey(Client, on_delete = models.PROTECT)
    product = models.ForeignKey(Product, default = 'Nacatamal de cerdo', on_delete = models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add = True)
    delivery_date = models.DateTimeField(default=utc_tomorrow)
    completed = models.CharField(max_length = 4, choices = completed_choices, default = PROCESO )
    nota = models.TextField(blank = True)
    
    def total_price(self):
        return self.quantity * self.price
    
    
    def __str__(self):
        return f"Orden #{self.id} - Cliente: {self.user} - {self.completed}"  



    
