from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers

class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

