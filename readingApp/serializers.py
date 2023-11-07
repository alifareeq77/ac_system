from rest_framework import serializers

from readingApp.models import MicrocontrollerData


class MicrocontrollerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MicrocontrollerData
        fields = ('timestamp', 'sensor_value')