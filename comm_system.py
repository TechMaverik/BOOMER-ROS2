import paho.mqtt.client as mqtt
import json
import time

# MQTT broker details
BROKER = "broker.hivemq.com"  # You can replace with your own broker
PORT = 1883
TOPIC = "test/dps/sensor"


# Create a JSON payload
def create_payload():
    data = {
        "device_id": "dps_pc",
        "temperature": 28.5,
        "humidity": 65,
        "timestamp": time.time(),
    }
    return json.dumps(data)


# Initialize MQTT client
client = mqtt.Client()


# Connect and publish
def publish_message():
    try:
        client.connect(BROKER, PORT, keepalive=60)
        payload = create_payload()
        client.publish(TOPIC, payload)
        print(f"Published to {TOPIC}: {payload}")
        client.disconnect()
    except Exception as e:
        print("Error:", e)


# Run it
publish_message()
