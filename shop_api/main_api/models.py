
from django.db import models

# Create your models here.i

from django.core.validators import RegexValidator

class Logins(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 50)
    customer_id = models.ForeignKey('Customers', on_delete = models.CASCADE)

    def __str__(self):
        return self.username


class Customers(models.Model):
    forename = models.CharField(max_length = 100)
    surename = models.CharField(max_length = 100)
    add =  models.ForeignKey("Dilivery_address", on_delete=models.CASCADE)
    phone = models.CharField( max_length = 14, blank = True)
    email = models.EmailField()
    postcode = models.IntegerField(default = 0)
    registered = models.BooleanField(default = False)

    def __str__(self):
        return self.forename

class Dilivery_address(models.Model):
    forename = models.CharField(max_length = 100)
    surename = models.CharField(max_length = 100)
    add1 = models.CharField(max_length = 200)
    phone = models.CharField(  max_length = 14, blank = True)
    postcode = models.IntegerField(default = 0)

    def __str__(self):
        return self.forename


class Order(models.Model):
    customer = models.ForeignKey(Customers, on_delete = models.CASCADE)
    registered = models.BooleanField(default = False)
    delivery = models.ForeignKey(
    Dilivery_address, on_delete = models.CASCADE)
    payment_type = models.CharField(max_length = 20)
    date = models.DateTimeField( auto_now=False ,auto_now_add=True)
    status = models.CharField(max_length = 50,default='waiting')
    session = models.CharField(max_length = 100,default ='00000')
    total = models.IntegerField(default = 0)

    def __str__(self):
        return self.status


class Order_items(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    product_id = models.ForeignKey('Products', on_delete = models.Case)
    quanlity = models.IntegerField(default = 0)
    def __str__(self):
        return 'Product: {} and quality: {}'.format(self.product_id,self.quanlity)


class Products(models.Model):
    cat = models.ForeignKey('Categories',related_name='products', on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.CharField(max_length = 200,default = '')
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.CharField(max_length = 100, default = '')

    def __str__(self):
        return self.name