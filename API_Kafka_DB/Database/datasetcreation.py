import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_date_range(start_date, num_days):
    return [start_date + timedelta(days=i) for i in range(num_days)]

def generate_historical_traffic_data(num_stations, num_days, start_date):
    data = []
    date_range = generate_date_range(start_date, num_days)
    for station_id in range(101, 101 + num_stations):
        for date in date_range:
            for hour in range(24):
                timestamp = datetime(date.year, date.month, date.day, hour, 0, 0)
                entry_count = random.randint(50, 300)
                exit_count = random.randint(50, 300)
                day_of_week = timestamp.strftime("%A")
                data.append([station_id, entry_count, exit_count, timestamp, day_of_week])
    return pd.DataFrame(data, columns=["station_id", "entry_count", "exit_count", "timestamp", "day_of_week"])

def generate_metro_schedule_data(num_stations, num_trains, start_date):
    data = []
    for train_id in range(1, num_trains + 1):
        for station_id in range(101, 101 + num_stations):
            arrival_time = start_date + timedelta(minutes=random.randint(0, 1440))
            departure_time = arrival_time + timedelta(minutes=random.randint(1, 10))
            frequency = random.randint(5, 20)
            data.append([train_id, station_id, arrival_time, departure_time, frequency])
    return pd.DataFrame(data, columns=["train_id", "station_id", "arrival_time", "departure_time", "frequency"])

def generate_weather_data(num_days, start_date):
    data = []
    date_range = generate_date_range(start_date, num_days)
    for date in date_range:
        for hour in range(24):
            timestamp = datetime(date.year, date.month, date.day, hour, 0, 0)
            temperature = round(random.uniform(15, 35), 1)
            precipitation = round(random.uniform(0, 20), 1)
            humidity = random.randint(40, 100)
            weather_condition = random.choice(['Sunny', 'Rainy', 'Cloudy'])
            data.append([timestamp, temperature, precipitation, humidity, weather_condition])
    return pd.DataFrame(data, columns=["timestamp", "temperature", "precipitation", "humidity", "weather_conditions"])

def generate_event_data(num_days, start_date):
    event_names = ["Concert", "Sports Event", "Festival"]
    data = []
    date_range = generate_date_range(start_date, num_days)
    for date in date_range:
        if random.random() < 0.1:  
            event_name = random.choice(event_names)
            event_location = f"Location_{random.randint(1, 10)}"
            #event_time = datetime(date.year, date.month, date.day, random.randint(8, 22), 0, 0)
            event_time = datetime(date.year, date.month, date.day, random.randint(16, 22), 0, 0) #hm... 4pm - 10pm
            estimated_attendance = random.randint(1000, 10000)
            data.append([event_name, event_location, event_time, date, estimated_attendance])
    return pd.DataFrame(data, columns=["event_name", "event_location", "event_time", "event_date", "estimated_attendance"])

def generate_socioeconomic_data(num_areas=5):
    area_names = [f"Area_{i}" for i in range(1, num_areas + 1)]
    data = []
    for area in area_names:
        population_density = random.randint(1000, 10000)
        employment_rate = round(random.uniform(85, 99), 1)
        average_income = random.randint(30000, 100000)
        data.append([area, population_density, employment_rate, average_income])
    return pd.DataFrame(data, columns=["area_name", "population_density", "employment_rate", "average_income"])

def generate_real_time_sensor_data(num_stations, num_days, start_date):
    data = []
    date_range = generate_date_range(start_date, num_days)
    for station_id in range(101, 101 + num_stations):
        for date in date_range:
            for hour in range(24):
                timestamp = datetime(date.year, date.month, date.day, hour, 0, 0)
                passenger_count = random.randint(50, 300)
                data.append([f"S{station_id}", station_id, timestamp, passenger_count])
    return pd.DataFrame(data, columns=["sensor_id", "location", "timestamp", "passenger_count"])

def generate_geographic_data(num_stations):
    data = []
    for station_id in range(101, 101 + num_stations):
        latitude = round(random.uniform(-90, 90), 6)
        longitude = round(random.uniform(-180, 180), 6)
        distance_to_next_station = round(random.uniform(1, 5), 2)
        data.append([station_id, latitude, longitude, distance_to_next_station])
    return pd.DataFrame(data, columns=["station_id", "latitude", "longitude", "distance_to_next_station"])

def generate_data(num_stations, num_days, num_trains, start_date):
    historical_traffic_data = generate_historical_traffic_data(num_stations, num_days, start_date)
    metro_schedule_data = generate_metro_schedule_data(num_stations, num_trains, start_date)
    weather_data = generate_weather_data(num_days, start_date)
    event_data = generate_event_data(num_days, start_date)
    socioeconomic_data = generate_socioeconomic_data()
    real_time_sensor_data = generate_real_time_sensor_data(num_stations, num_days, start_date)
    geographic_data = generate_geographic_data(num_stations)


    historical_traffic_data.to_csv("historical_traffic_data.csv", index=False)
    metro_schedule_data.to_csv("metro_schedule_data.csv", index=False)
    weather_data.to_csv("weather_data.csv", index=False)
    event_data.to_csv("event_data.csv", index=False)
    socioeconomic_data.to_csv("socioeconomic_data.csv", index=False)
    real_time_sensor_data.to_csv("real_time_sensor_data.csv", index=False)
    geographic_data.to_csv("geographic_data.csv", index=False)

    print("Synthetic data generated and saved to CSV files.")

num_stations = int(input("Enter the number of stations: "))
num_days = int(input("Enter the number of days: "))
num_trains = int(input("Enter the number of trains: "))
start_date_input = input("Enter the start date (YYYY-MM-DD): ")
start_date = datetime.strptime(start_date_input, "%Y-%m-%d")

generate_data(num_stations, num_days, num_trains, start_date)

