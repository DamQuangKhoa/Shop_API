from rest_framework import serializers
from main_api  import models as models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Products
        fields = '__all__'
class CategoriesSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True,read_only= True)
    class Meta:
        model = models.Categories
        fields = ('name', 'products')
