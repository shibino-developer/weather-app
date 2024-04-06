# weather/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather, name='weather'),
    path('forecast/', views.forecast, name='forecast')  # URL pattern for forecast view

]
