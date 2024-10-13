import requests
from bs4 import BeautifulSoup

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'YOUR_API_KEY'

# Get user input for city and state
city = input("Enter the city: ")
state = input("Enter the state (optional): ")

# Construct the API URL based on your chosen provider
url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{state}&appid={api_key}"

# Make the API request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()   

    # Extract relevant weather information
    temperature = data['main']['temp']
    description = data['weather'][0]['description']   

    # Convert temperature to Celsius (if needed)
    temperature_celsius = temperature - 273.15

    # Print the weather forecast
    print(f"Weather in {city}, {state}:")
    print(f"Temperature: {temperature_celsius:.2f} °C")
    print(f"Description: {description}")
else:
    print("Error: Unable to retrieve weather data.")