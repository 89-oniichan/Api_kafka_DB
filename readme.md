
```
# Steps to Start API and Kafka

## 1. Start Zookeeper
Open a terminal and start Zookeeper:

```bash
cd /path/to/kafka
bin/zookeeper-server-start.sh config/zookeeper.properties
```

## 2. Start Kafka
Open a new terminal window and start the Kafka server:

```bash
cd /path/to/kafka
bin/kafka-server-start.sh config/server.properties
```

## 3. Create Kafka Topic
Create a Kafka topic named `sensor-data`:

```bash
cd /path/to/kafka
bin/kafka-topics.sh --create --topic sensor-data --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

## 4. Start Django Development Server
Activate your virtual environment and start the Django development server:

```bash
source /path/to/your/venv/bin/activate
cd /path/to/your/django/project
python manage.py runserver 0.0.0.0:8000
```

## 5. Run Kafka Producer Script
Open a new terminal window, activate your virtual environment, and run the Kafka producer script:

```bash
source /path/to/your/venv/bin/activate
cd /path/to/your/django/project/kafka_scripts
python producer.py
```

## 6. Run Kafka Consumer Script
Open another terminal window, activate your virtual environment, and run the Kafka consumer script:

```bash
source /path/to/your/venv/bin/activate
cd /path/to/your/django/project/kafka_scripts
python consumer.py
```
```
