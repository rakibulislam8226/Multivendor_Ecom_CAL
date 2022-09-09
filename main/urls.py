from django.urls import path
from . import views
urlpatterns = [
    path('vendor/', views.VendorList.as_view()),
    path('vendor/<int:pk>/', views.VendorDetail.as_view()),
]