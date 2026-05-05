import requests 

# location 
latitude = 48.85 
longitude = 2.35 

# API url 
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

response = requests.get(url)
data = response.json()

temperature = data["current"]["temperature_2m"]
print(temperature)


# received a TUPLE of coordinates 
def get_weather(coordinates): 
    lat = coordinates[0]
    long = coordinates[1]

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m"

    response = requests.get(url)
    data = response.json()

    # extract only temp from response 
    return data["current"]["temperature_2m"]


# pass in lat long as a TUPLE 
paris_temp = get_weather((48.85, 2.35))
london_temp = get_weather((51.50, -0.12))
tokyo_temp = get_weather((35.68, 139.69))

print(f"Paris temp: {paris_temp} C")
print(f"London temp: {london_temp} C")
print(f"Tokyo temp: {tokyo_temp} C")