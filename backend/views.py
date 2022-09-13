# from rest_framework import generics
# from rest_framework_simplejwt.tokens import RefreshToken

# class Login(generics.CreateAPIView):
#     def create(self, request, *args, **kwargs):
#         user = request.user
#         token = RefreshToken.for_user(user)
        
#         token.access_token