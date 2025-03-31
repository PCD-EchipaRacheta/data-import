import requests
import json
import functions

API_key = functions.access_secret_weatherAPIKey()

def get_2day_weather_forecast():
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_key}&q=Iasi&days=2&aqi=no&alerts=yes"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Save the data to a .jsonl file
        with open("weather_forecast.jsonl", "w") as jsonl_file:
            # Write each top-level key-value pair as a separate JSONL line
            for key, value in data.items():
                jsonl_file.write(json.dumps({key: value}) + "\n")

        # Save the file to the Google Cloud Storage bucket
        functions.upload_to_gcs("weather_forecast.jsonl", "weather_forecast.jsonl")
    
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)

get_2day_weather_forecast()