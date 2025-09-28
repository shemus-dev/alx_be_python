import requests
Apikey = "9de9f309c225044d03a5946386b3f832"
lon = "36.817223"
lat = "-1.286389"
url = f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={Apikey}"

try:
    response = requests.get(url)
    data = response.json()
    print(data)
except:
    print("error")
