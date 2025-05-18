from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import WeatherData
from .forms import WeatherDataForm

def weather_station(request):
    if request.method == 'POST':
        form = WeatherDataForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('weather_station'))
    else:
        form = WeatherDataForm()
    weather_data = WeatherData.objects.all().order_by('-timestamp')[:10]
    return render(request, 'weatherapp/weather_station.html', {'form': form, 'weather_data': weather_data})
