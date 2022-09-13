# to create a new token with refresh token
# http post http://127.0.0.1:8000/api/token/ username=rakibulislam password=rakib
# http post http://127.0.0.1:8000/api/vendor/ "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYyOTg3MzM0LCJpYXQiOjE2NjI5ODcwMzQsImp0aSI6IjE0YTVhNWU5ZDc5MzQ5MTg5ZDIwYjVmMDAwNWY3YjRjIiwidXNlcl9pZCI6MX0.yfvjGuANovNKdnG4jRM0i8pE2sJ9ShCKwaInP5z47-o"

from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.tokens import RefreshToken


schema_view = get_schema_view(
   openapi.Info(
      title="Multivendor API",
      default_version='v1',
      description="Multivendor Ecom",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/',include('main.urls')),
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
