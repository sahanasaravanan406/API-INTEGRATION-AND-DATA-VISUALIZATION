import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
API_KEY = "YOUR_API_KEY"  
CITY = "Chennai"         
NUM_HOURS = 12          
url = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()
time_list = []
temp_list = []
humidity_list = []
for entry in data["list"][:NUM_HOURS]:
    time = datetime.fromtimestamp(entry["dt"])
    temp = entry["main"]["temp"]
    humidity = entry["main"]["humidity"]
    time_list.append(time)
    temp_list.append(temp)
    humidity_list.append(humidity)
df = pd.DataFrame({
    "Time": time_list,
    "Temperature (°C)": temp_list,
    "Humidity (%)": humidity_list
})
print(df)
plt.figure(figsize=(10,5))
plt.plot(df["Time"], df["Temperature (°C)"], marker='o', label="Temperature (°C)")
plt.plot(df["Time"], df["Humidity (%)"], marker='s', label="Humidity (%)")
plt.xlabel("Time")
plt.ylabel("Values")
plt.title(f"Weather Forecast for {CITY}")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
