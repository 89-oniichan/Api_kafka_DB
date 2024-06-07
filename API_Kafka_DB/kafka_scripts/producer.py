from kafka import KafkaProducer
import json
from datetime import datetime
import time

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    sensor_data = {
        "sensor_id": "S101",
        "location": 101,
        "timestamp": datetime.now().isoformat(),
        "passenger_count": 150
    }
    producer.send('sensor-data', sensor_data)
    print(f"Sent data: {sensor_data}")
    time.sleep(5)  
