
from django.contrib import admin
from . models import Vendor,Product,ProductCategory,Order,OrderItems,Customer


# Register your models here.
admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(Customer)