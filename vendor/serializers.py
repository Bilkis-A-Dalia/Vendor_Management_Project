from .models import Vendor,Performance
from rest_framework import serializers

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        moedel = Vendor
        fields = '__all__'

class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = '__all__'