import json
import time
import urllib.request

from kafka import KafkaProducer

API_KEY = "XXX" 

url = "https://api.weatherapi.com/v1/current.json?q=Paris&key={}".format(API_KEY)

producer = KafkaProducer(bootstrap_servers="kafka-kafdrop-kafka-1:9092")

while True:
    try:
        response = urllib.request.urlopen(url)
        print("{} Sent request to weather API".format(time.time()))
        weather = json.loads(response.read().decode())
        print("{} Received weather record".format(time.time()), weather)
        producer.send("weather-paris", json.dumps(weather).encode())
        print("{} Produced weather record".format(time.time()))
    except Exception as e:
        print(url)
        print(f"Failed to produce weather record: {e}")
    time.sleep(1)