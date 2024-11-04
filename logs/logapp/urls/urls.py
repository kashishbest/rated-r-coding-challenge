from django.urls import path

from logs.logapp.views import views

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
]
