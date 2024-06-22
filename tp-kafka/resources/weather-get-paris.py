import json
import time
import urllib.request

from kafka import KafkaProducer

API_KEY = "2c43b2f668054774885132414242206" 

url = "https://api.weatherapi.com/v1/current.json?q=Paris&key={}".format(API_KEY)

producer = KafkaProducer(bootstrap_servers="localhost:9092")

while True:
    try:
        response = urllib.request.urlopen(url)
        weather = json.loads(response.read().decode())
        producer.send("weather-paris", json.dumps(weather).encode())
        print("{} Produced weather record".format(time.time()))
    except Exception as e:
        print(url)
        print(f"Failed to produce weather record: {e}")
    time.sleep(1)