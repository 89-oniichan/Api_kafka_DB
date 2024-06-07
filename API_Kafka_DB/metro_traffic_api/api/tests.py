from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import RealTimeSensorData

class RealTimeSensorDataTests(APITestCase):
    def test_create_realtime_sensor_data(self):
        url = reverse('realtimesensordata-list')
        data = {
            "sensor_id": "S101",
            "location": 101,
            "timestamp": "2024-06-05T12:34:56",
            "passenger_count": 150
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_realtime_sensor_data(self):
        url = reverse('realtimesensordata-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
