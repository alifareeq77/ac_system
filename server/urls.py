from django.urls import path, include
from rest_framework import routers

from readingApp.views import MicrocontrollerDataViewset, index_view

router = routers.DefaultRouter()
router.register(r'microcontroller-data', MicrocontrollerDataViewset)

urlpatterns = [
    path("", index_view, name='index'),
    path('', include(router.urls)),
]
