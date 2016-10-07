from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import BaseScore

class BaseScoreSerializer(GeoFeatureModelSerializer):
	class Meta:
		model = BaseScore
		geo_field = 'geom'
		fields = ('name', 'url', 'lon', 'lat', 'geom', 'score') #'__all__'
