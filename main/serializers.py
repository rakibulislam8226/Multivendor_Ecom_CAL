from rest_framework import serializers
from . models import Product, Vendor, ProductCategory,Customer,Order,OrderItems


class VendorSerializer(serializers.ModelSerializer):
    # user_name= serializers.ReadOnlyField(source='request.vendor.user.username')
    # user={{vendor.user.username }}
    class Meta:
        model = Vendor
        fields = ['id','user', 'address']
        # depth = 1


class ProductSerializer(serializers.ModelSerializer):
    category_name= serializers.ReadOnlyField(source='category.title')
    vendor_name= serializers.ReadOnlyField(source='vendor.user.username')

    class Meta:
        model = Product
        fields = '__all__'
        # exclude=('vendor','id')
        # depth = 1
        

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'
        # depth = 1        
        
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        # depth = 1        
        
        
# Order
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        # depth = 1    
            
# OrderItems
class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = '__all__'
        # depth = 1        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        