import time
import ujson
import mpu6050
import configurations
from umqtt.simple import MQTTClient
from display_content import DisplayContent
from movements_sdk import HighLevelMovements, HighLevelMovementSDK

MQTT_BROKER = configurations.BROKER_ADDRESS
MQTT_PORT = configurations.BROKER_PORT
CLIENT_ID = configurations.CLIENT_ID
MPU6050 = configurations.MPU6050_TOPIC_BIN
DISPLAY = configurations.DISPLAY_TOPIC_BIN
SERVO_POSITION = configurations.SERVO_TOPIC_BIN
HIGH_LEVEL_MOVEMENTS = configurations.MOVEMENTS_TOPIC_BIN
MOVEMENTS_SDK_COXA = configurations.MOVEMENTS_TOPIC_SDK_COXA_BIN
MOVEMENT_SDK_FEMUR = configurations.MOVEMENTS_TOPIC_SDK_FEMUR_BIN
MOVEMENT_SDK_TIBIA = configurations.MOVEMENTS_TOPIC_SDK_TIBIA_BIN


def mqtt_callback(topic, msg):
    print(f'📩 Received on "{topic.decode()}": {msg.decode()}')
    if topic.decode() == "boomer/display":
        DisplayContent().display_content_with_topic(msg.decode())
    if topic.decode() == "boomer/movements":
        HighLevelMovements().high_level_movements(msg.decode())
    if topic.decode() == "boomer/movement/sdk/coxa":
        HighLevelMovementSDK().movements_sdk_coxa(msg.decode())
    if topic.decode() == "boomer/movement/sdk/femur":
        HighLevelMovementSDK().movements_sdk_femur(msg.decode())
    if topic.decode() == "boomer/movement/sdk/tibia":
        HighLevelMovementSDK().movements_sdk_tibia(msg.decode())


def setup_mqtt():
    client = MQTTClient(CLIENT_ID, MQTT_BROKER, port=MQTT_PORT)
    client.set_callback(mqtt_callback)
    client.connect()
    client.subscribe(DISPLAY)
    client.subscribe(SERVO_POSITION)
    client.subscribe(HIGH_LEVEL_MOVEMENTS)
    client.subscribe(MOVEMENTS_SDK_COXA)
    client.subscribe(MOVEMENT_SDK_FEMUR)
    client.subscribe(MOVEMENT_SDK_TIBIA)
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
