from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from readingApp.models import MicrocontrollerData
from readingApp.serializers import MicrocontrollerDataSerializer


class MicrocontrollerDataViewset(viewsets.ModelViewSet):
    queryset = MicrocontrollerData.objects.all()
    serializer_class = MicrocontrollerDataSerializer
    http_method_names = ['post']


def index_view(request):
    return render(request, 'index.html')
