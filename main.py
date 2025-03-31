import requests
import json
import functions

API_key = functions.access_secret_weatherAPIKey()

def get_2day_weather_forecast():
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_key}&q=Iasi&days=2&aqi=no&alerts=no"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        with open("weather_forecast.json", "w") as json_file:
            json.dump(data, json_file, indent=4)  # Save for readability

        # Save the file to the Google Cloud Storage bucket
        functions.upload_to_gcs("weather_forecast.json", "weather_forecast.json")
    
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)

get_2day_weather_forecast()