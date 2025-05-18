from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather_station, name='weather_station'),
]