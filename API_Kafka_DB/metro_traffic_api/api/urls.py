from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import RealTimeSensorDataViewSet, HistoricalTrafficViewSet, MetroScheduleViewSet, WeatherViewSet, EventsViewSet, SocioeconomicViewSet, GeographicViewSet

router = DefaultRouter()
router.register(r'real_time_sensor', RealTimeSensorDataViewSet)
router.register(r'historical_traffic', HistoricalTrafficViewSet)
router.register(r'metro_schedule', MetroScheduleViewSet)
router.register(r'weather', WeatherViewSet)
router.register(r'events', EventsViewSet)
router.register(r'socioeconomic', SocioeconomicViewSet)
router.register(r'geographic', GeographicViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
