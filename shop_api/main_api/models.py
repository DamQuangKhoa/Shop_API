
from django.db import models

# Create your models here.i

from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex = r'^\+?1?\d{9, 15}$', message = "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
class Logins(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 50)
    customer_id = models.ForeignKey('Customers', on_delete = models.CASCADE)

    def __str__(self):
        return self.username


class Customers(models.Model):
    forename = models.CharField(max_length = 100)
    surename = models.CharField(max_length = 100)
    add1 = models.CharField(max_length = 200)
    add2 = models.CharField(max_length = 200)
    add3 = models.CharField(max_length = 200)
    phone = models.CharField(validators = [phone_regex], max_length = 14, blank = True)
    email = models.EmailField()
    postcode = models.IntegerField(default = 0)
    registered = models.BooleanField(default = False)

    def __str__(self):
        return self.forename

class Dilivery_addresses (models.Model):
    forename = models.CharField(max_length = 100)
    surename = models.CharField(max_length = 100)
    add1 = models.CharField(max_length = 200)
    add2 = models.CharField(max_length = 200)
    add3 = models.CharField(max_length = 200)
    phone = models.CharField(validators = [phone_regex], max_length = 14, blank = True)
    email = models.EmailField()
    postcode = models.IntegerField(default = 0)

    def __str__(self):
        return self.forename


class Others(models.Model):
    customer = models.ForeignKey(Customers, on_delete = models.CASCADE)
    registered = models.BooleanField(default = False)
    delivery = models.ForeignKey(
    Dilivery_addresses, on_delete = models.CASCADE)
    payment_type = models.CharField(max_length = 20)
    date = models.DateTimeField()
    status = models.CharField(max_length = 50)
    session = models.CharField(max_length = 100)
    total = models.IntegerField(default = 0)

    def __str__(self):
        return self.status


class Other_items(models.Model):
    other = models.ForeignKey(Others, on_delete = models.CASCADE)
    product_id = models.ForeignKey('Products', on_delete = models.Case)
    quanlity = models.IntegerField(default = 0)

    def __str__(self):
        return self.quanlity


class Products(models.Model):
    cat = models.ForeignKey('Categories', on_delete = models.CASCADE)
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