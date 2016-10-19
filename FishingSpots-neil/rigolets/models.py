from django.contrib.gis.db import models

class RigoletsLayer(models.Model):
	name = models.CharField(max_length=50, blank=True)
	area = models.IntegerField(blank=True)
	lon = models.FloatField()
	lat = models.FloatField()
	geom = models.PointField(blank=True)
	depth = models.FloatField(blank=True)
	waveheight = models.FloatField(blank=True)
	velocity = models.FloatField(blank=True)
	wind_velocity = models.FloatField('Wind Speed', blank=True)
	trib_width = models.FloatField('Tributary Width', blank=True)
	trib_count = models.FloatField('Tributary Count', blank=True)
	fetch = models.FloatField(blank=True)
	ufarea = models.FloatField('Up Flow Area', blank=True)
	tide_range = models.FloatField('Tide Range', blank=True)
	turbidity = models.FloatField(blank=True)
	score = models.FloatField(blank=True)

	def __str__(self):
		return self.name
