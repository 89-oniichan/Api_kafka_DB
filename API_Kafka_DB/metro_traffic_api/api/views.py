from rest_framework import viewsets
from .models import RealTimeSensorData, HistoricalTraffic, MetroSchedule, Weather, Events, Socioeconomic, Geographic
from .serializers import RealTimeSensorDataSerializer, HistoricalTrafficSerializer, MetroScheduleSerializer, WeatherSerializer, EventsSerializer, SocioeconomicSerializer, GeographicSerializer

class RealTimeSensorDataViewSet(viewsets.ModelViewSet):
    queryset = RealTimeSensorData.objects.all()
    serializer_class = RealTimeSensorDataSerializer

# Define other viewsets similarly...
from rest_framework import viewsets
from .models import RealTimeSensorData, HistoricalTraffic, MetroSchedule, Weather, Events, Socioeconomic, Geographic
from .serializers import RealTimeSensorDataSerializer, HistoricalTrafficSerializer, MetroScheduleSerializer, WeatherSerializer, EventsSerializer, SocioeconomicSerializer, GeographicSerializer

class RealTimeSensorDataViewSet(viewsets.ModelViewSet):
    queryset = RealTimeSensorData.objects.all()
    serializer_class = RealTimeSensorDataSerializer

class HistoricalTrafficViewSet(viewsets.ModelViewSet):
    queryset = HistoricalTraffic.objects.all()
    serializer_class = HistoricalTrafficSerializer

class MetroScheduleViewSet(viewsets.ModelViewSet):
    queryset = MetroSchedule.objects.all()
    serializer_class = MetroScheduleSerializer

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

class SocioeconomicViewSet(viewsets.ModelViewSet):
    queryset = Socioeconomic.objects.all()
    serializer_class = SocioeconomicSerializer

class GeographicViewSet(viewsets.ModelViewSet):
    queryset = Geographic.objects.all()
    serializer_class = GeographicSerializer
