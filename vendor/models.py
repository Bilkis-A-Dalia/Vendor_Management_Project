from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=50)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=100, unique=True)
    on_time_delivery_rate = models.FloatField(null=True)
    quality_rating_avg = models.FloatField(null=True)
    average_response_time = models.FloatField(null=True)
    fulfillment_rate = models.FloatField(null=True)

    def calculate_performance_metrics(self):
        completed_pos = self.purchaseorder_set.filter(status='completed')
        total_completed_pos = completed_pos.count()

        # On-time delivery rate
        if total_completed_pos > 0:
            on_time_deliveries = completed_pos.filter(delivery_date__lte=models.F('expected_delivery_date')).count()
            self.on_time_delivery_rate = (on_time_deliveries / total_completed_pos) * 100
        else:
            self.on_time_delivery_rate = 0.0

        # Quality rating average
        completed_pos_with_rating = completed_pos.exclude(quality_rating__isnull=True)
        if completed_pos_with_rating.exists():
            self.quality_rating_avg = completed_pos_with_rating.aggregate(models.Avg('quality_rating'))['quality_rating__avg']
        else:
            self.quality_rating_avg = 0.0

        # Average response time
        acknowledged_pos = completed_pos.exclude(acknowledgment_date__isnull=True)
        if acknowledged_pos.exists():
            total_response_time = sum((po.acknowledgment_date - po.issue_date).total_seconds() for po in acknowledged_pos)
            self.average_response_time = total_response_time / acknowledged_pos.count() / 3600  # in hours
        else:
            self.average_response_time = 0.0

        # Fulfilment rate
        fulfilled_pos = completed_pos.filter(issues__isnull=True)
        if total_completed_pos > 0:
            self.fulfillment_rate = (fulfilled_pos.count() / total_completed_pos) * 100
        else:
            self.fulfillment_rate = 0.0

        self.save()
        
    def __str__(self):
        return self.name
    
class Performance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(null=True)
    quality_rating_avg = models.FloatField(null=True)
    average_response_time = models.FloatField(null=True)
    fulfillment_rate = models.FloatField(null=True)

    def __str__(self):
        return f'{self.vendor} - {self.date.strftime("%Y-%m-%d")}'
