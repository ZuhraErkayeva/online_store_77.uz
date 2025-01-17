from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import RegistrationViewSet

router = DefaultRouter()
router.register(r'registration', RegistrationViewSet, basename='registration')

urlpatterns = [
    path('api/', include(router.urls))
]