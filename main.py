import requests
import json
import functions

API_key = functions.access_secret_weatherAPIKey()


def get_weather_forecast():
    api_key = "your_api_key_here"  # Replace with your actual API key
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_key}&q=Iasi&days=2&aqi=no&alerts=no"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        
        # print("Weather Forecast for Iași:")
        # for day in data["forecast"]["forecastday"]:
        #     date = day["date"]
        #     condition = day["day"]["condition"]["text"]
        #     max_temp = day["day"]["maxtemp_c"]
        #     min_temp = day["day"]["mintemp_c"]
        #     print(f"Date: {date}")
        #     print(f"Condition: {condition}")
        #     print(f"Max Temp: {max_temp}°C")
        #     print(f"Min Temp: {min_temp}°C")
        #     print("-" * 20)

        print(data)
    
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)

get_weather_forecast()