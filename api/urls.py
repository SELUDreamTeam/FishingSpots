from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'basescore', views.BaseScoreViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
