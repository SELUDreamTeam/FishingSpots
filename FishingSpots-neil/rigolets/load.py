import os
from django.contrib.gis.utils import LayerMapping
from .models import RigoletsLayer

rigolets_mapping = {
	'name' : 'NAME',
	'area' : 'AREA',
	'lon' : 'LON',
	'lat' : 'LAT',
	'geom' : 'GEOMETRY',
	'depth' : 'DEPTH',
	'waveheight' : 'WAVEHEIGHT',
	'velocity' : 'VELOCITY',
	'wind_velocity' : 'WINDVELOCITY',
	'trib_width' : 'TRIBWIDTH',
	'trib_count' : 'TRIBCOUNT',
	'fetch' : 'FETCH',
	'ufarea' : 'UFAREA',
	'tide_range' : 'TIDERANGE',
	'turbidity' : 'TURBIDITY',
	'score' : 'SCORE',
}

