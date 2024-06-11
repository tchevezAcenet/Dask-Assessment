import os
import pandas as pd
import numpy as np
import random

# Create the weather_data directory if it doesn't exist
if not os.path.exists('weather_data'):
    os.makedirs('weather_data')

# Define the columns for the weather data
columns = ['year', 'month', 'day', 'location', 'temperature_celsius', 'humidity_percent', 'wind_speed_mps', 'precipitation_mm']

# Define some sample data for the columns
years = list(range(2000, 2024))
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
locations = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Atlanta']

# Days in each month
days_in_month = {
    'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30,
    'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31
}

# Define the number of CSV files and rows per file
num_files = 1000
num_rows_per_file = 1000

# Function to generate random weather data
def generate_weather_data():
    data = []
    for _ in range(num_rows_per_file):
        year = random.choice(years)
        month = random.choice(months)
        day = random.randint(1, days_in_month[month])
        location = random.choice(locations)
        temperature = round(np.random.normal(20, 5), 1)  # Normal distribution around 20 degrees Celsius
        humidity = random.randint(40, 80)  # Random humidity between 40% and 80%
        wind_speed = round(np.random.uniform(0, 10), 1)  # Random wind speed between 0 and 10 m/s
        precipitation = round(np.random.uniform(0, 5), 1)  # Random precipitation between 0 and 5 mm
        data.append([year, month, day, location, temperature, humidity, wind_speed, precipitation])
    return data

# Generate and save multiple CSV files
for i in range(num_files):
    data = generate_weather_data()
    df = pd.DataFrame(data, columns=columns)
    
    # Save the DataFrame to a CSV file
    df.to_csv(f'weather_data/weather_data_{i+1}.csv', index=False)

print("CSV files created in the 'weather_data' folder.")