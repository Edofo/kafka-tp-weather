import streamlit as st
import pandas as pd
from kafka import KafkaConsumer
import json
import time

st.set_page_config(layout='wide')  # DÃ©finir la disposition de la page sur 'wide'

def create_consumer():
  consumer = KafkaConsumer(
    'weather-paris',
    bootstrap_servers=['kafka-kafdrop-kafka-1:9092'],
    auto_offset_reset='latest',  
    enable_auto_commit=True,
    group_id='weather-monitor-paris',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    api_version=(0, 10, 1))  
  return consumer

st.title('Weather Monitoring Dashboard')

consumer = create_consumer()

placeholder = st.empty()

try:
    while True:
        for message in consumer:
            weather = message.value
            location = weather['location']
            current = weather['current']
            
            with placeholder.container():
                st.header(f"Weather in {location['name']}, {location['country']}")
                st.write(f"**Region:** {location['region']}")
                st.write(f"**Local Time:** {location['localtime']}")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric(label="Temperature (°C)", value=current['temp_c'])
                    st.metric(label="Condition", value=current['condition']['text'])
                    st.image("https:" + current['condition']['icon'])
                    st.metric(label="Humidity (%)", value=current['humidity'])
                    st.metric(label="Pressure (mb)", value=current['pressure_mb'])
                    
                with col2:
                    st.metric(label="Wind (kph)", value=current['wind_kph'])
                    st.metric(label="Wind Direction", value=current['wind_dir'])
                    st.metric(label="Precipitation (mm)", value=current['precip_mm'])
                    st.metric(label="Visibility (km)", value=current['vis_km'])
                    st.metric(label="UV Index", value=current['uv'])
                    
except KeyboardInterrupt:
    st.write("Stream stopped.")
finally:
    consumer.close()