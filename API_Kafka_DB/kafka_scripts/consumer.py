from kafka import KafkaConsumer
import json
import requests

consumer = KafkaConsumer(
    'sensor-data',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    data = message.value
    response = requests.post('http://localhost:8000/api/real_time_sensor/', json=data)
    if response.status_code == 201:
        print(f"Successfully sent data to API: {data}")
    else:
        print(f"Failed to send data to API: {data}")
