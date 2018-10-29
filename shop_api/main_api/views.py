from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    UpdateAPIView
    
)
from rest_framework.permissions import IsAuthenticated,AllowAny

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

class OrderList(viewsets.GenericViewSet, ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serial.OrderSerializer

class OrderDetail(viewsets.GenericViewSet,RetrieveUpdateDestroyAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serial.OrderSerializer
    # lookup_field = 'id'
class OrderCurrent(viewsets.GenericViewSet,RetrieveAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serial.OrderSerializer

