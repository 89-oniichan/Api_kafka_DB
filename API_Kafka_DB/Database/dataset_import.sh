PGPASSWORD=password psql -h localhost -d metro_traffic -U metro_user <<EOF
\copy historical_traffic(station_id, entry_count, exit_count, timestamp, day_of_week) FROM '/root/database/historical_traffic_data.csv' DELIMITER ',' CSV HEADER;
\copy metro_schedule(train_id, station_id, arrival_time, departure_time, frequency) FROM '/root/database/metro_schedule_data.csv' DELIMITER ',' CSV HEADER;
\copy weather(timestamp, temperature, precipitation, humidity, weather_conditions) FROM '/root/database/weather_data.csv' DELIMITER ',' CSV HEADER;
\copy events(event_name, event_location, event_time, event_date, estimated_attendance) FROM '/root/database/event_data.csv' DELIMITER ',' CSV HEADER;
\copy socioeconomic(area_name, population_density, employment_rate, average_income) FROM '/root/database/socioeconomic_data.csv' DELIMITER ',' CSV HEADER;
\copy real_time_sensor(sensor_id, location, timestamp, passenger_count) FROM '/root/database/real_time_sensor_data.csv' DELIMITER ',' CSV HEADER;
\copy geographic(station_id, latitude, longitude, distance_to_next_station) FROM '/root/database/geographic_data.csv' DELIMITER ',' CSV HEADER;
EOF
