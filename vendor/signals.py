from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Vendor, Performance
@receiver(post_save, sender=Vendor)
def performance_create(sender, instance, created, **kwargs):
    if created:
        Performance.objects.create(
            vendor=instance,
            on_time_delivery_rate=instance.on_time_delivery_rate,
            quality_rating_avg=instance.quality_rating_avg,
            average_response_time=instance.average_response_time,
            fulfillment_rate=instance.fulfillment_rate
        )
