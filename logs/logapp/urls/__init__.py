from django.urls import include, path

urlpatterns = [
    path('logs/', include('logapp.urls.urls')),
    # path('health/', include('logapp.urls.health_urls')),
]
