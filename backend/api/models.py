from django.db import models


class FloodData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    distance = models.FloatField()
    flow = models.FloatField()
    status = models.CharField(max_length=20)
