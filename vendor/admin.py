from django.contrib import admin
from .import models
# Register your models here.
admin.site.register(models.Vendor)
admin.site.register(models.Performance)


# user: vendor
# passs: 123987
# mail: dalia@gmail.com