from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework import viewsets
from main_api import models as models
from main_api import serializer as serial# Create your views here. 
class CategoriesList(viewsets.GenericViewSet, ListCreateAPIView):
    queryset = models.Categories.objects.all()
    serializer_class = serial.CategoriesSerializer

class CateogoriesDetail(viewsets.GenericViewSet,RetrieveUpdateDestroyAPIView):
    queryset = models.Categories.objects.all()
    serializer_class = serial.CategoriesSerializer
    # lookup_field = 'id'
class ProductList(viewsets.GenericViewSet, ListCreateAPIView):
    queryset = models.Products.objects.all()
    serializer_class = serial.ProductSerializer

class ProductDetail(viewsets.GenericViewSet,RetrieveUpdateDestroyAPIView):
    queryset = models.Products.objects.all()
    serializer_class = serial.ProductSerializer
    # lookup_field = 'id'