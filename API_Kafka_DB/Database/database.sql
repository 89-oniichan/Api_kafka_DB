CREATE DATABASE metro_traffic;

CREATE USER metro_user WITH ENCRYPTED PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE metro_traffic TO metro_user;


-- Historical Passenger Traffic Data
CREATE TABLE historical_traffic (
    id SERIAL PRIMARY KEY,
    station_id INT,
    entry_count INT,
    exit_count INT,
    timestamp TIMESTAMP,
    day_of_week VARCHAR(10)
);

-- Metro Schedule Data
CREATE TABLE metro_schedule (
    id SERIAL PRIMARY KEY,
    train_id INT,
    station_id INT,
    arrival_time TIMESTAMP,
    departure_time TIMESTAMP,
    frequency INT
);

-- Weather Data
CREATE TABLE weather (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    temperature FLOAT,
    precipitation FLOAT,
    humidity INT,
    weather_conditions VARCHAR(20)
);

-- Event Data
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    event_name VARCHAR(50),
    event_location VARCHAR(50),
    event_time TIMESTAMP,
    event_date DATE,
    estimated_attendance INT
);

-- Socioeconomic Data
CREATE TABLE socioeconomic (
    id SERIAL PRIMARY KEY,
    area_name VARCHAR(50),
    population_density INT,
    employment_rate FLOAT,
    average_income INT
);

-- Real-Time Sensor Data
CREATE TABLE real_time_sensor (
    id SERIAL PRIMARY KEY,
    sensor_id VARCHAR(10),
    location INT,
    timestamp TIMESTAMP,
    passenger_count INT
);

-- Geographic Data
CREATE TABLE geographic (
    id SERIAL PRIMARY KEY,
    station_id INT,
    latitude FLOAT,
    longitude FLOAT,
    distance_to_next_station FLOAT
);
