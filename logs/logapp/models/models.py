# Create your models here.

from django.db import models


class Log(models.Model):
    time_stamp = models.DateTimeField()
    customer_id = models.CharField(max_length=255)
    request_path = models.CharField(max_length=255)
    status_code = models.IntegerField()
    duration = models.FloatField()

    def __str__(self):
        return f"Log from {self.customer_id} at {self.time_stamp}"
