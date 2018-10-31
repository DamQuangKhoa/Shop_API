from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
User = get_user_model()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
        depth = 2


class CategoriesSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Categories
        fields = ('__all__')


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_items
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    order_item = OrderItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
