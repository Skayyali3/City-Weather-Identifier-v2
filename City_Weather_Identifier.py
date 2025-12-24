import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime


weather_options = {
    "Temperature Range": ["temperature_2m_max", "temperature_2m_min"],
    "Precipitation Sum": ["precipitation_sum"],
    "Rain Sum": ["rain_sum"],
    "Snowfall Sum": ["snowfall_sum"],
    "Showers Sum": ["showers_sum"],
    "Current Temperature": ["temperature_2m"]
}


def fetch_coordinates(city):
    geolocator = Nominatim(user_agent="test")
    location = geolocator.geocode(city)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None


def fetch_weather_data(lat, lon, variables):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": variables,
        "timezone": "auto"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()['daily']
    else:
        return None


def fetch_current_temperature(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m",
        "timezone": "auto"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        hourly_data = response.json()['hourly']
        times = hourly_data['time']
        temps = hourly_data['temperature_2m']
        now = datetime.now().strftime('%Y-%m-%dT%H:00')
        if now in times:
            index = times.index(now)
            return temps[index]
    return None


def plot_weather(data, city, option):
    df = pd.DataFrame(data)
    plt.figure(figsize=(10, 5))

    if option == "Temperature Range":
        sns.lineplot(df, x='time', y='temperature_2m_max', marker='o', color='red', label='Max Temp')
        sns.lineplot(df, x='time', y='temperature_2m_min', marker='o', label='Min Temp')
        plt.ylabel("Temperature (°C)")
    else:
        key = weather_options[option][0]
        sns.barplot(df, x='time', y=key, color='skyblue')
        plt.ylabel(f"{option} (mm or cm)")

    plt.title(f"7-day {option} Forecast for {city.title()}")
    plt.xlabel("Date")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def on_get_weather():
    city = city_name.get().strip()
    option = option_var.get()

    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    lat, lon = fetch_coordinates(city)
    if lat is None or lon is None:
        messagebox.showerror("Error", f"Could not find location for '{city}'.")
        return

    if option == "Current Temperature":
        current_temp = fetch_current_temperature(lat, lon)
        if current_temp is not None:
            l.config(
                text=f"Current Temperature in {city.title()}: {current_temp}°C",
                fg="white", bg="#007ACC"
            )
        else:
            l.config(
                text="Current Temperature: N/A",
                fg="white", bg="#555555"
            )
    else:
        variables = weather_options[option]
        data = fetch_weather_data(lat, lon, variables)
        if data is None:
            messagebox.showerror("Error", "Failed to retrieve weather data. Try again later.")
            return
        plot_weather(data, city, option)
        l.config(text="")  


x = tk.Tk()
x.title("City Weather Identifier")
x.geometry("370x260")
x.resizable(False, False)


tk.Label(x, text="7-Day Weather Forecast Viewer", font=("Arial", 14, "bold")).grid(row=0, columnspan=2, pady=10)


tk.Label(x, text="Enter City:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
city_name = tk.Entry(x)
city_name.grid(row=1, column=1, padx=5, pady=5)


tk.Label(x, text="Select Weather Data:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
option_var = tk.StringVar(x)
option_var.set("Temperature Range")
option_menu = tk.OptionMenu(x, option_var, *weather_options.keys())
option_menu.grid(row=2, column=1, padx=5, pady=5)


b = tk.Button(x, text="Get Weather", command=on_get_weather, bg="#4CAF50", fg="white")
b.grid(row=3, columnspan=2, pady=10)


l = tk.Label(x, text="", font=("Arial", 10), bg="white")
l.grid(row=4, columnspan=2, pady=10)

x.mainloop()


