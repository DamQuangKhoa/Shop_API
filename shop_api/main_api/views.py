from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import mixins
User = get_user_model()
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView
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
class ProductList(viewsets.GenericViewSet, ListCreateAPIView):
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
class OrderCurrent(viewsets.GenericViewSet,RetrieveAPIView ):
    queryset = models.Order.objects.all()
    serializer_class = serial.OrderSerializer
    permission_classes = (IsAdmindNotGet,)

class RetrieveCurrentUser(RetrieveUpdateAPIView,viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = serial.UserSerializer
    permission_classes = (IsAuthenticated,)
    def get_object(self):
        return self.request.user
    def list(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)     
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.



    """