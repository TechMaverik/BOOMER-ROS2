import threading
import position_mapper
import paho.mqtt.client as mqtt
import json
import time
from Micropython import configurations

# MQTT broker details
BROKER = "10.120.3.159"  # You can replace with your own broker
PORT = 2025
COXA = "boomer/movement/sdk/coxa"
FEMUR = "boomer/movement/sdk/femur"
TIBIA = "boomer/movement/sdk/tibia"


class ControlSystem:

    def __init__(self):
        self.position = position_mapper
        self.difference_list = []
        self.direction_list = []

    def publish_message(self, TOPIC, payload):
        try:
            client = mqtt.Client()
            client.connect(BROKER, PORT, keepalive=60)

            client.publish(TOPIC, payload)
            print(f"Published to {TOPIC}: {payload}")
            client.disconnect()
        except Exception as e:
            print("Error:", e)

    def calculate_movement_default_to_stand(self, default_pos, standing_pos, channel):
        if default_pos[channel] > standing_pos[channel]:
            movement = False
            difference = default_pos[channel] - standing_pos[channel]
            self.difference_list.append(difference)
            self.direction_list.append(movement)
        else:
            movement = True
            difference = standing_pos[channel] - default_pos[channel]
            self.difference_list.append(difference)
            self.direction_list.append(movement)

    def move_coxa_default_stand(self):
        default_pos = self.position.DEFAULT_POSITION
        for counter in range(0, 40):
            c1 = default_pos["c1"] - counter
            c2 = default_pos["c2"] + counter
            c3 = default_pos["c3"] + counter
            c4 = default_pos["c4"] - counter
        coxa_payload = {
            "c1": 51,
            "c2": 129,
            "c3": 129,
            "c4": 51,
        }
        time.sleep(0.25)
        coxa_payload = json.dumps(coxa_payload)
        self.publish_message(COXA, coxa_payload)

    def move_femur_default_stand(self):
        default_pos = self.position.DEFAULT_POSITION
        for counter in range(0, 120):
            c5 = default_pos["c5"] - counter
            c7 = default_pos["c7"] - counter
        femur_payload = {
            "c5": 0,
            "c6": 129,
            "c7": 0,
            "c8": 120,
        }
        time.sleep(0.25)
        femur_payload = json.dumps(femur_payload)
        self.publish_message(FEMUR, femur_payload)

    def move_femur_default_stand2(self):
        default_pos = self.position.DEFAULT_POSITION
        for counter in range(0, 90):
            c6 = default_pos["c6"] + counter
            c8 = default_pos["c8"] + counter

    def move_tibia_default_stand(self):
        default_pos = self.position.DEFAULT_POSITION
        for counter in range(0, 90):
            c9 = default_pos["c9"] + counter
            c10 = default_pos["c10"] - counter
            c11 = default_pos["c11"] + counter
            c12 = default_pos["c12"] - counter

    def default_to_stand(self):
        default_pos = self.position.DEFAULT_POSITION
        standing_pos = self.position.STANDING_POSITION
        self.calculate_movement_default_to_stand(default_pos, standing_pos, "c1")
        self.calculate_movement_default_to_stand(default_pos, standing_pos, "c2")
        self.calculate_movement_default_to_stand(default_pos, standing_pos, "c3")
        self.calculate_movement_default_to_stand(default_pos, standing_pos, "c4")
        self.calculate_movement_default_to_stand(default_pos, standing_pos, "c5")
        self.calculate_movement_default_to_stand(default_pos, standing_pos, "c6")
        self.calculate_movement_default_to_stand(default_pos, standing_pos, "c7")
        self.calculate_movement_default_to_stand(default_pos, standing_pos, "c8")
        self.calculate_movement_default_to_stand(default_pos, standing_pos, "c9")
        self.calculate_movement_default_to_stand(default_pos, standing_pos, "c10")
        self.calculate_movement_default_to_stand(default_pos, standing_pos, "c11")
        self.calculate_movement_default_to_stand(default_pos, standing_pos, "c12")

        print(self.direction_list)
        print(self.difference_list)


# ControlSystem().move_coxa_default_stand()
ControlSystem().move_femur_default_stand()
