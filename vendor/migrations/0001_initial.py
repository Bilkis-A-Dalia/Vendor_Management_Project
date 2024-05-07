# Generated by Django 4.2.7 on 2024-05-01 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact_details', models.TextField()),
                ('address', models.TextField()),
                ('vendor_code', models.CharField(max_length=100, unique=True)),
                ('on_time_delivery_rate', models.FloatField(null=True)),
                ('quality_rating_avg', models.FloatField(null=True)),
                ('average_response_time', models.FloatField(null=True)),
                ('fulfillment_rate', models.FloatField(null=True)),
            ],
        ),
    ]
