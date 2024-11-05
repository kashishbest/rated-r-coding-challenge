# Create your views here.
from datetime import datetime

from django.db.models import Avg
from django.http import JsonResponse
from django.utils.timezone import make_aware

from logapp.models import Log
from logapp.models.api_models import Stats, StatsResponse
from logapp.serializers.serializers import StatsResponseSerializer


def health_check(request):
    return JsonResponse({"status": "ok"}, status=200)


def customer_stats(request, id):
    # Get the 'from' date from the query parameters
    from_date_str = request.GET.get('from')
    if not from_date_str:
        return JsonResponse({'error': 'Please provide a valid "from" date in YYYY-MM-DD format.'}, status=400)

    try:
        from_date = make_aware(datetime.strptime(from_date_str, '%Y-%m-%d'))
    except ValueError:
        return JsonResponse({'error': 'Invalid date format. Please use YYYY-MM-DD.'}, status=400)

    # Query logs for the specified customer and date range
    logs = Log.objects.filter(customer_id=id, time_stamp__gte=from_date)

    # Total number of successful and failed requests
    successful_requests = logs.filter(status_code__lt=400).count()
    failed_requests = logs.filter(status_code__gte=400).count()
    # Calculate Staats
    total_requests = successful_requests + failed_requests
    uptime = (successful_requests / total_requests * 100) if total_requests > 0 else 0

    average_latency = logs.aggregate(Avg('duration'))['duration__avg'] or 0
    if logs.exists():
        median_latency = logs.order_by('duration').values_list('duration', flat=True)[len(logs) // 2]
        p99_latency = logs.order_by('duration').values_list('duration', flat=True)[int(len(logs) * 0.99)]
    else:
        median_latency = 0
        p99_latency = 0

    stats = Stats(total_successful_requests=successful_requests,
                  total_failed_requests=failed_requests,
                  uptime=uptime,
                  average_latency=average_latency,
                  median_latency=median_latency,
                  p99_latency=p99_latency)
    # Prepare the response data
    response_data = StatsResponse(
        customer_id=id,
        from_date=from_date_str,
        stats=stats,
    )
    serializer = StatsResponseSerializer(response_data)
    return JsonResponse(serializer.data)  # return JsonResponse(response_data)
