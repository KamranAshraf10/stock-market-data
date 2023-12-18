from django.urls import path, include
from . import views
from . views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'pre_market', PreMarketViewSet, basename='premarket')

urlpatterns = [
    path('data/pre_market/', include(router.urls)),
]