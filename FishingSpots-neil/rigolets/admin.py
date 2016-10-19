from django.contrib.gis import admin
from .models import RigoletsLayer

# Register your models here.
admin.site.register(RigoletsLayer, admin.GeoModelAdmin)
