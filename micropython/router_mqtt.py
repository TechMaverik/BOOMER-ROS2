import time
import ujson
import mpu6050
from umqtt.simple import MQTTClient
from display_content import DisplayContent
from high_level_movements import HighLevelMovements

MQTT_BROKER = "192.168.29.165"  # e.g., '192.168.1.100'
MQTT_PORT = 1883
CLIENT_ID = "Boomer 3.0"
MPU6050 = b"boomer/mpu6050"
DISPLAY = b"boomer/display"
SERVO = b"boomer/servo"
HIGH_LEVEL_MOVEMENTS = b"boomer/movements"


def mqtt_callback(topic, msg):
    print(f'📩 Received on "{topic.decode()}": {msg.decode()}')
    if topic.decode() == "boomer/display":
        DisplayContent().display_content_with_topic(msg.decode())
    if topic.decode() == "boomer/movements":
        HighLevelMovements().high_level_movements(msg.decode())


def setup_mqtt():
    client = MQTTClient(CLIENT_ID, MQTT_BROKER, port=MQTT_PORT)
    client.set_callback(mqtt_callback)
    client.connect()
    client.subscribe(DISPLAY)
    client.subscribe(SERVO)
    client.subscribe(HIGH_LEVEL_MOVEMENTS)
    return client  # ✅ Add this line


def main():
    client = setup_mqtt()
    while True:
        DisplayContent().display_content_with_topic("open eyes")
        time.sleep(0.5)
        DisplayContent().display_content_with_topic("close eyes")
        time.sleep(0.5)
        data = mpu6050.read_mpu6050()
        payload = {
            "ax": data[0],
            "ay": data[1],
            "az": data[2],
            "gx": data[3],
            "gy": data[4],
            "gz": data[5],
        }
        message = ujson.dumps(payload).encode()
        client.publish(MPU6050, message)
        client.check_msg()
