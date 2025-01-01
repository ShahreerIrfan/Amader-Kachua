from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserProfileViewSet
from .views import CustomTokenObtainPairView

router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet, basename='userprofile')

urlpatterns = [
    path('', include(router.urls)),  
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Custom token view
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
]
