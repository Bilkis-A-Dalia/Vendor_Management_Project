from django.shortcuts import render
from .serializers import VendorSerializer,PerformanceSerializer
from .models import Vendor,Performance
from rest_framework import viewsets
# Create your views here.
class VendorViewSet(viewsets.ReadOnlyModelViewSet): 
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
class PerformanceViewSet(viewsets.ReadOnlyModelViewSet): 
    queryset = Vendor.objects.all()
    serializer_class = PerformanceSerializer

