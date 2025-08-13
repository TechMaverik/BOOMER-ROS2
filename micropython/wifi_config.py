import time
import network
from machine import Pin

# Set up station (client) mode
led = Pin(2, Pin.OUT)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Connect to Wi-Fi
ssid = "F106-5G"
password = "12345678"
wlan.connect(ssid, password)

# Wait for connection
while not wlan.isconnected():
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)


print("Connected to WiFi")
print("Network config:", wlan.ifconfig())
