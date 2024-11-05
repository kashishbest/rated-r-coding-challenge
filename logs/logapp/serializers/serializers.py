from rest_framework import serializers


class StatsSerializer(serializers.Serializer):
    total_successful_requests = serializers.IntegerField()
    total_failed_requests = serializers.IntegerField()
    uptime = serializers.FloatField()
    average_latency = serializers.FloatField()
    median_latency = serializers.FloatField()
    p99_latency = serializers.FloatField()


class StatsResponseSerializer(serializers.Serializer):
    customer_id = serializers.CharField()
    from_date = serializers.DateField()
    stats = StatsSerializer()
