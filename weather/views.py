# weather/views.py
from django.shortcuts import render
import requests

def weather(request):
    city = request.GET.get('city')
    if city:
        api_key = '84b15b6200a9ba9ab7015b2730a57b5a'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        weather_data = response.json()
        
        return render(request, 'weather/weather.html', {'weather_data': weather_data})
    else:
        return render(request, 'weather/weather.html')


# Create your views here.
# views.py
def forecast(request):
    city = request.GET.get('city')
    if city:
        api_key = '84b15b6200a9ba9ab7015b2730a57b5a'
        url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        forecast_data = response.json()
        print(forecast_data)
        return render(request, 'weather/forecast.html', {'forecast_data': forecast_data})
    else:
        return render(request, 'weather/forecast.html')
