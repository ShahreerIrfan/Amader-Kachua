from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserProfileViewSet

router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet, basename='userprofile')

urlpatterns = [
    path('', include(router.urls)),  # Automatically handles CRUD operations
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT Token Obtain
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT Token Refresh
]
