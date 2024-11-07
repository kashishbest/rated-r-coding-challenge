from django.urls import path

from logapp.views import views

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
    path('customers/<str:id>/stats/', views.customer_stats, name='customer_stats'),
    path('load', views.load, name='load_data'),
]
