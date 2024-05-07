from django.db import models
from vendor.models import Vendor

# Create your models here.
class Order(models.Model):
    STATUS = [
        ('pending','Pending'),
        ('complete','Complete'),
        ('canceled','Canceled'),
    ]
    po_number = models.CharField(max_length=50,unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50,choices=STATUS,default='Pending')
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True)
    
    def __str__(self):
        return f'{self.po_number},{self.vendor.name}'