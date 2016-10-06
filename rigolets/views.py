from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import RigoletsLayer
from rest_framework import viewsets
from rigolets.serializers import UserSerializer, GroupSerializer, RigoletsSerializer
from django.core import serializers

# Create your views here.
def index (request):
	template = loader.get_template('rigolets/index.html')
	return HttpResponse(template.render(request))

def about (request):
	template = loader.get_template('rigolets/about.html')
	return HttpResponse(template.render(request))

def ol_map (request):
	data_points =  serializers.serialize("json", RigoletsLayer.objects.all())
	context = {'data_points' : data_points}
	template = loader.get_template('rigolets/openlayers.html')
	return HttpResponse(template.render(request))

class RigoletsViewSet(viewsets.ModelViewSet):
	queryset = RigoletsLayer.objects.all()
	serializer_class = RigoletsSerializer
