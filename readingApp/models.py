from django.db import models

# Create your models here.
from django.db import models

class MicrocontrollerData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    sensor_value = models.FloatField()