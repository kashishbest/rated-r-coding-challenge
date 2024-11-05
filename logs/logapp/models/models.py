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

    class Meta:
        indexes = [
            models.Index(fields=['customer_id']),  # Single-field index
            models.Index(fields=['time_stamp']),  # Single-field index
            models.Index(fields=['customer_id', 'time_stamp']),  # Composite index
        ]
