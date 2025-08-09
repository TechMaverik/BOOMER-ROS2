from machine import I2C, Pin
from pca9685 import PCA9685
from servo import Servos  # Ensure you have this module, or adapt from your library
import time

i2c = I2C(0, scl=Pin(22), sda=Pin(21))  # Adapt pins if needed
pca = PCA9685(i2c)
pca.freq(50)  # Set frequency to 50Hz for servos

servos = Servos(i2c)  # This class handles angle conversion

# shoulder
channel_1 = 0
channel_2 = 4
channel_3 = 8
channel_4 = 12

# thy
channel_5 = 1
channel_6 = 5
channel_7 = 9
channel_8 = 13

# femur
channel_9 = 2
channel_10 = 6
channel_11 = 7
channel_12 = 14

angle = 90
speed = 20
servos.position(index=channel_1, degrees=angle)
servos.position(index=channel_2, degrees=angle)
servos.position(index=channel_3, degrees=angle)
servos.position(index=channel_4, degrees=angle)

servos.position(index=channel_5, degrees=angle)
servos.position(index=channel_6, degrees=angle)
servos.position(index=channel_7, degrees=angle)
servos.position(index=channel_8, degrees=angle)

servos.position(index=channel_9, degrees=angle)
servos.position(index=channel_10, degrees=angle)
servos.position(index=channel_11, degrees=angle)
servos.position(index=channel_12, degrees=angle)

counter = 0
time.sleep(2)
for angle in range(90, 30, -speed):
    counter = counter + speed
    new_angle = 90 + counter
    print(new_angle)
    servos.position(index=channel_5, degrees=angle)
    servos.position(index=channel_7, degrees=angle)
    servos.position(index=channel_6, degrees=new_angle)
    servos.position(index=channel_8, degrees=new_angle)
    time.sleep(0.3)

counter = 0
# for angle in range(50, 130, speed):
for angle in range(90, 0, -speed):
    counter = counter + speed
    new_angle = 90 + counter
    print(new_angle)
    servos.position(index=channel_9, degrees=angle)
    servos.position(index=channel_11, degrees=angle)
    servos.position(index=channel_10, degrees=new_angle)
    servos.position(index=channel_12, degrees=new_angle)
    time.sleep(0.3)

servos.position(index=channel_5, degrees=90)
time.sleep(1)
servos.position(index=channel_8, degrees=90)
time.sleep(1)
servos.position(index=channel_7, degrees=90)
time.sleep(1)
servos.position(index=channel_6, degrees=90)
time.sleep(1)
