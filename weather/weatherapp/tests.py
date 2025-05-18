from django.test import TestCase
import pytest
from django.urls import reverse
from django.test import Client
from .models import WeatherData

@pytest.mark.django_db
def test_weatherdata_creation():
    data = WeatherData.objects.create(temperature=25.5, humidity=60.0, pressure=1012.0)
    assert WeatherData.objects.count() == 1
    assert data.temperature == 25.5
    assert data.humidity == 60.0
    assert data.pressure == 1012.0

@pytest.mark.django_db
def test_weather_station_view_get():
    client = Client()
    response = client.get(reverse('weather_station'))
    assert response.status_code == 200
    assert b"Weather Station Data Collection" in response.content

@pytest.mark.django_db
def test_weather_station_view_post():
    client = Client()
    post_data = {'temperature': 22.0, 'humidity': 55.0, 'pressure': 1008.0}
    response = client.post(reverse('weather_station'), post_data, follow=True)
    assert response.status_code == 200
    assert WeatherData.objects.count() == 1
    assert b"22.0" in response.content
    assert b"55.0" in response.content
    assert b"1008.0" in response.content
