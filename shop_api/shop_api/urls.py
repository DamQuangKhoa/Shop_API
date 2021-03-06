"""shop_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from main_api import views as view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.SimpleRouter()
router.register('categories', view.CategoriesList, base_name="Categories")
router.register('categories', view.CateogoriesDetail, base_name="Categories")
router.register('products', view.ProductList, base_name="Products")
router.register('products', view.ProductDetail, base_name="Products")
router.register('orders', view.OrderList, base_name="orders")
router.register('orders', view.OrderDetail, base_name="orders")
router.register('current-order', view.OrderCurrent, base_name="current-order")
router.register('current-user', view.RetrieveCurrentUser, 
                base_name="current-user")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/sessions', TokenObtainPairView.as_view(), 
         name='token_obtain_pair'),
    path('api/v1/current-session', TokenRefreshView.as_view(),
         name='token_refesh')
]
