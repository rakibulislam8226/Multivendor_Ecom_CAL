from django.urls import path
from main import views
urlpatterns = [
    path('vendor/', views.VendorList.as_view()),
    path('vendor/<int:pk>/', views.VendorDetail.as_view()),
    
    path('product/', views.ProductList.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    
    path('product/category/', views.ProductCategoryList.as_view()),
    path('product/category/<int:pk>/', views.ProductCategoryDetail.as_view()),
    
    path('customer/', views.CustomerList.as_view()),
    path('customer/<int:pk>/', views.CustomerDetail.as_view()),
    
    path('order/', views.OrderList.as_view()),
    path('order/<int:pk>/', views.OrderDetail.as_view()),
    
    path('order_item/', views.OrderItemsList.as_view()),
    path('order_item/<int:pk>/', views.OrderItemsDetail.as_view()),
]