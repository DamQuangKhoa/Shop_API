from rest_framework import serializers
# from main_api  import models as models
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
class CategoriesSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many = True, read_only = True)
    class Meta:
        model = Categories
        fields = ('name', 'products')

class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_items
        fields = '__all__'
class OrderSerializer(serializers.ModelSerializer):
    order_item = OrderItemsSerializer(many = True, read_only = True)
    class Meta:
        model = Order
        fields = ('status', 'order_item')