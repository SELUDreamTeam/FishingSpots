from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import RigoletsLayer
from rest_framework import viewsets, response
from rigolets.serializers import UserSerializer, GroupSerializer, RigoletsSerializer, MapSerializer
from django.core import serializers
import json

# Create your views here.
def index (request):
	template = loader.get_template('rigolets/index.html')
	return HttpResponse(template.render(request))

def about (request):
	template = loader.get_template('rigolets/about.html')
	return HttpResponse(template.render(request))

def ol_map (request):
	data_points =  RigoletsLayer.objects.all()
	serializer_class = MapSerializer(data_points, many=True)
	points = []
	for feat in serializer_class.data['features']:
		points.append(feat)
	context = { 'request' : request }

	return render(request, "rigolets/openlayers.html", {'data_points' : points })
