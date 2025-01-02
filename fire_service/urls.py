from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FireStationViewset

# Create a router and register the DoctorViewSet
router = DefaultRouter()
router.register(r'fire_service', FireStationViewset)

# Include the URLs from the router
urlpatterns = [
    path('', include(router.urls)),
]
