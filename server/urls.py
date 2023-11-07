
from django.urls import path, include
from rest_framework import routers

from readingApp.views import MicrocontrollerDataViewset

router = routers.DefaultRouter()
router.register(r'microcontroller-data', MicrocontrollerDataViewset)

urlpatterns = [
    path('', include(router.urls)),
]
