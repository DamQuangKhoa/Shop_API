from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView
)
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

from rest_framework import viewsets
from main_api import models as models
from main_api import serializer as serial
# Create your views here. 
class CategoriesList(viewsets.GenericViewSet,ListAPIView):
    queryset = models.Categories.objects.all()
    serializer_class = serial.CategoriesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # authentication_classes = (TokenAuthentication)
class CateogoriesDetail(viewsets.GenericViewSet,UpdateAPIView,DestroyAPIView):
    queryset = models.Categories.objects.all()
    serializer_class = serial.CategoriesSerializer
    permission_classes = (IsAdminUser,)
# class CateogoriesDetail(viewsets.GenericViewSet,RetrieveAPIView):
#     queryset = models.Categories.objects.all()
#     serializer_class = serial.CategoriesSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
    
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

