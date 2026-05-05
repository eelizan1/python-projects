import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os 

# funtion to get weather data for the past 7 days
def get_weather(lat, long, start_date, end_date): 
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

    response = requests.get(url)
    data = response.json() 

    return data 

def organize_data(data): 
    daily_data = data["daily"]
    
    # create a data frame 
    df = pd.DataFrame({
        "date" : daily_data["time"], 
        "max_temp" : daily_data["temperature_2m_max"], 
        "min_temp" : daily_data["temperature_2m_min"]
    })

    # convert date strings to date time
    df["date"] = pd.to_datetime(df["date"])

    return df

# takes in the data frame (df) and creates line plot chart
def create_line_chart(df): 
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
    plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

    # Add labels and title
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Paris Weather - Past 7 Days')
    plt.legend()

    # Rotate x-axis labels for readability
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot
    plt.savefig('weather_chart.png')
    return plt 

def save_as_csv(df): 
    file_path = "data/paris_weather.csv"
    # create data folder if doesnt exist 
    if not os.path.exists("data"): 
        os.makedirs("data")


    # save csv 
    df.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")


# calculate dates 
today = datetime.now()
week_ago = today - timedelta(days=7)

# format dates for API format (YYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# call api with lat, long and dates
temp_data = get_weather(48.85, 2.35, start_date, end_date)
# clean and organize data
organized_data_df = organize_data(temp_data)

print(organized_data_df)

# create line chart
chart_plt = create_line_chart(organized_data_df)
chart_plt.show() # show line chart

# save data frame as CSV 
save_as_csv(organized_data_df)




