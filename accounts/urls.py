from django.urls import path
from .views import LoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='obtain_token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
]