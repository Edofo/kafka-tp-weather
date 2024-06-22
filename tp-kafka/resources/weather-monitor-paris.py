import json
from kafka import KafkaConsumer

weather = {}
consumer = KafkaConsumer("weather-paris", bootstrap_servers='localhost:9092', group_id="weather-monitor-paris")

for message in consumer:
    weather = json.loads(message.value.decode())
    print("Received weather record")
    print("Weather in Paris: {}".format(weather["current"]["condition"]["text"]))
    print("Temperature in Paris: {}°C".format(weather["current"]["temp_c"]))
    print("Wind in Paris: {} km/h".format(weather["current"]["wind_kph"]))
    print("Pressure in Paris: {} hPa".format(weather["current"]["pressure_mb"]))
    print("Humidity in Paris: {}%".format(weather["current"]["humidity"]))
    print("Cloud in Paris: {}%".format(weather["current"]["cloud"]))
    print("Visibility in Paris: {} km".format(weather["current"]["vis_km"]))
    print("UV in Paris: {}".format(weather["current"]["uv"]))
    print("Gust in Paris: {} km/h".format(weather["current"]["gust_kph"]))
    print("Last updated: {}".format(weather["current"]["last_updated"]))
    print("Local time: {}".format(weather["location"]["localtime"]))
    
    # return value to frontend
    weather.update(weather)
    break



    