# from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BaseScore
from rest_framework import viewsets
from .serializers import BaseScoreSerializer

# List all stocks or create a new one
# base/
class BaseScoreList(APIView):
	
	def get(self, request):
		print(request)
		base_scores = BaseScore.objects.all()
		serializer = BaseScoreSerializer(base_scores, many=True)
		return Response(serializer.data)

	def post(self):
		pass

class BaseScoreViewSet(viewsets.ModelViewSet):
	queryset = BaseScore.objects.all()
	serializer_class = BaseScoreSerializer
