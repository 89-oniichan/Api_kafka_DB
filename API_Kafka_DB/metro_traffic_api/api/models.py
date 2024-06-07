from django.db import models

class RealTimeSensorData(models.Model):
    sensor_id = models.CharField(max_length=10)
    location = models.IntegerField()
    timestamp = models.DateTimeField()
    passenger_count = models.IntegerField()


class HistoricalTraffic(models.Model):
    station_id = models.IntegerField()
    entry_count = models.IntegerField()
    exit_count = models.IntegerField()
    timestamp = models.DateTimeField()
    day_of_week = models.CharField(max_length=10)

class MetroSchedule(models.Model):
    train_id = models.IntegerField()
    station_id = models.IntegerField()
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()
    frequency = models.IntegerField()

class Weather(models.Model):
    timestamp = models.DateTimeField()
    temperature = models.FloatField()
    precipitation = models.FloatField()
    humidity = models.IntegerField()
    weather_conditions = models.CharField(max_length=20)

class Events(models.Model):
    event_name = models.CharField(max_length=50)
    event_location = models.CharField(max_length=50)
    event_time = models.DateTimeField()
    event_date = models.DateField()
    estimated_attendance = models.IntegerField()

class Socioeconomic(models.Model):
    area_name = models.CharField(max_length=50)
    population_density = models.IntegerField()
    employment_rate = models.FloatField()
    average_income = models.IntegerField()

class Geographic(models.Model):
    station_id = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    distance_to_next_station = models.FloatField()
