from django.urls import (
    include,
    path
)
from rest_framework.routers import DefaultRouter

from user.views import UserViewSet


router = DefaultRouter()
router.register('employee', UserViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls)),
]
