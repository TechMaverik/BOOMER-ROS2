import network
import time, socket
from machine import Pin


class Wifi:

    def connect(self):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        led = Pin(23, Pin.OUT)
        ssid = "F106-4G"
        password = "12345678"
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            print("Connecting...")
            led.on()
            time.sleep(1)
            led.off()
            time.sleep(1)
        print("Connected to WiFi!")
        print("Network config:", wlan.ifconfig())


Wifi().connect()
