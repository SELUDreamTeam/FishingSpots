from django.contrib.auth.models import User, Group
from rigolets.models import RigoletsLayer
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('name', 'url')

class RigoletsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = RigoletsLayer
		fields = ('name', 'url', 'lon', 'lat', 'geom')

class MapSerializer(GeoFeatureModelSerializer):
	class Meta:
		model = RigoletsLayer
		geo_field = 'geom'
		fields = ('name', 'lon', 'lat', 'geom')
