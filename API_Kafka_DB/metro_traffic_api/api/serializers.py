from rest_framework import serializers
from .models import RealTimeSensorData, HistoricalTraffic, MetroSchedule, Weather, Events, Socioeconomic, Geographic

class RealTimeSensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealTimeSensorData
        fields = '__all__'

class HistoricalTrafficSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalTraffic
        fields = '__all__'

class MetroScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetroSchedule
        fields = '__all__'

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'

class SocioeconomicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socioeconomic
        fields = '__all__'

class GeographicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geographic
        fields = '__all__'
