from django.contrib.gis import admin
from .models import BaseScore

# Register your models here.
admin.site.register(BaseScore, admin.GeoModelAdmin)