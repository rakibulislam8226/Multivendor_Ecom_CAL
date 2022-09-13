
from .models import Vendor,Product,ProductCategory,Customer,Order,OrderItems
from .serializers import (VendorSerializer,
                          ProductSerializer,
                          ProductCategorySerializer,
                          CustomerSerializer,
                          OrderSerializer,
                          OrderItemsSerializer,
                          )
from rest_framework import generics,permissions

# Create your views here.
# vendor api start #
class VendorList(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    # def user(self):
    #     user={{request.user}}

class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes=[permissions.IsAuthenticated]
# vendor api end #
    
# Product api start #
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes=[permissions.IsAuthenticated]
# Product api end #

# ProductCategory api start #
class ProductCategoryList(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

class ProductCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes=[permissions.IsAuthenticated]
# ProductCategory api end #


# Customer api start #
class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes=[permissions.IsAuthenticated]
# Customer api end #


# Order api start #
class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes=[permissions.IsAuthenticated]
# Order api end #


# OrderItems api start #
class OrderItemsList(generics.ListCreateAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

class OrderItemsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer
    permission_classes=[permissions.IsAuthenticated]
# OrderItems api end #