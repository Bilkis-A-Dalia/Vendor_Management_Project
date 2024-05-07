from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('purchase_orders', views.OrderViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
