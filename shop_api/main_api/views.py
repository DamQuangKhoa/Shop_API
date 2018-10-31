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
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


# Create your views here. 

class IsAdmindNotGet(IsAdminUser):
    """
    If request == get >>> just request = get not authen, other request must admin
    """
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return super(IsAdmindNotGet, self).has_permission(request, view)
class CategoriesList(viewsets.GenericViewSet,ListCreateAPIView):
    queryset = models.Categories.objects.all()
    serializer_class = serial.CategoriesSerializer
    permission_classes = (IsAdmindNotGet,)
    # authentication_classes = (TokenAuthentication)
class CateogoriesDetail(viewsets.GenericViewSet,RetrieveUpdateDestroyAPIView):
    queryset = models.Categories.objects.all()
    serializer_class = serial.CategoriesSerializer
    permission_classes = (IsAdmindNotGet,)

# class CateogoriesDetail(viewsets.GenericViewSet,RetrieveAPIView):
#     queryset = models.Categories.objects.all()
#     serializer_class = serial.CategoriesSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
    
    # lookup_field = 'id'
class ProductList(viewsets.GenericViewSet, ListAPIView):
    queryset = models.Products.objects.all()
    serializer_class = serial.ProductSerializer
    permission_classes = (IsAdmindNotGet,)
class ProductDetail(viewsets.GenericViewSet,RetrieveUpdateDestroyAPIView):
    queryset = models.Products.objects.all()
    serializer_class = serial.ProductSerializer
    permission_classes = (IsAdmindNotGet,)

class OrderList(viewsets.GenericViewSet, ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serial.OrderSerializer
    permission_classes = (IsAdmindNotGet,)
class OrderDetail(viewsets.GenericViewSet,RetrieveUpdateDestroyAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serial.OrderSerializer
    permission_classes = (IsAdmindNotGet,)
class OrderCurrent(viewsets.GenericViewSet,RetrieveAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serial.OrderSerializer
    permission_classes = (IsAdmindNotGet,)
