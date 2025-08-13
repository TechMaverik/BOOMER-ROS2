from machine import I2C, Pin
from pca9685 import PCA9685
from servo import Servos  # Ensure you have this module, or adapt from your library
import time

i2c = I2C(0, scl=Pin(22), sda=Pin(21))  # Adapt pins if needed
pca = PCA9685(i2c)
pca.freq(50)  # Set frequency to 50Hz for servos

servos = Servos(i2c)  # This class handles angle conversion


def boomer_leg_limit_checker():
    """
    Check if the servo angles are within the limits.
    This function should be implemented based on your specific requirements.
    """

    # shoulder
    channel_1 = 0
    channel_2 = 4
    channel_3 = 8
    channel_4 = 12

    # thy
    # channel_1 = 1
    # channel_2 = 1
    # channel_3 = 9
    # channel_4 = 13

    angle = 90
    servos.position(index=channel_1, degrees=angle)
    servos.position(index=channel_2, degrees=angle)
    servos.position(index=channel_3, degrees=angle)
    servos.position(index=channel_4, degrees=angle)

    for angle in range(50, 130, 2):
        servos.position(index=channel_1, degrees=angle)
        time.sleep(0.1)
    for angle in range(130, 50, -2):
        servos.position(index=channel_1, degrees=angle)
        time.sleep(0.1)
    for angle in range(50, 90, 2):
        servos.position(index=channel_1, degrees=angle)
        time.sleep(0.1)

    for angle in range(50, 130, 2):
        servos.position(index=channel_3, degrees=angle)
        time.sleep(0.1)
    for angle in range(130, 50, -2):
        servos.position(index=channel_3, degrees=angle)
        time.sleep(0.1)
    for angle in range(50, 90, 2):
        servos.position(index=channel_3, degrees=angle)
        time.sleep(0.1)

    for angle in range(130, 50, -2):
        servos.position(index=channel_2, degrees=angle)
        time.sleep(0.1)
    for angle in range(50, 130, 2):
        servos.position(index=channel_2, degrees=angle)
        time.sleep(0.1)
    for angle in range(130, 90, -2):
        servos.position(index=channel_2, degrees=angle)
        time.sleep(0.1)

    for angle in range(130, 50, -2):
        servos.position(index=channel_4, degrees=angle)
        time.sleep(0.1)
    for angle in range(50, 130, 2):
        servos.position(index=channel_4, degrees=angle)
        time.sleep(0.1)
    for angle in range(130, 90, -2):
        servos.position(index=channel_4, degrees=angle)
        time.sleep(0.1)


def multiple_leg_movement_tester():
    """
    Test the movement of multiple legs.
    This function should be implemented based on your specific requirements.
    """
    # shoulder
    # channel_1 = 0
    # channel_2 = 4
    # channel_3 = 8
    # channel_4 = 12

    # thy
    # channel_1 = 1
    # channel_2 = 5
    # channel_3 = 9
    # channel_4 = 13

    # femur
    channel_1 = 2
    channel_2 = 6
    channel_3 = 10
    channel_4 = 14

    angle = 90
    speed = 2
    servos.position(index=channel_1, degrees=angle)
    servos.position(index=channel_2, degrees=angle)
    servos.position(index=channel_3, degrees=angle)
    servos.position(index=channel_4, degrees=angle)
    counter = 0
    # for angle in range(50, 130, speed):
    for angle in range(50, 130, speed):
        counter = counter + speed
        new_angle = 130 - counter
        print(new_angle)
        servos.position(index=channel_1, degrees=angle)
        servos.position(index=channel_3, degrees=angle)
        servos.position(index=channel_2, degrees=new_angle)
        servos.position(index=channel_4, degrees=new_angle)
        time.sleep(0.3)
    counter = 0
    # for angle in range(130, 50, -speed):
    for angle in range(130, 50, -speed):
        counter = counter + speed
        new_angle = 50 + counter
        print(new_angle)
        servos.position(index=channel_1, degrees=angle)
        servos.position(index=channel_3, degrees=angle)
        servos.position(index=channel_2, degrees=new_angle)
        servos.position(index=channel_4, degrees=new_angle)
        time.sleep(0.3)
    counter = 0
    for angle in range(50, 90, speed):
        # for angle in range(50, 90, speed):
        counter = counter + speed
        new_angle = 90 - counter
        print(new_angle)
        servos.position(index=channel_1, degrees=angle)
        servos.position(index=channel_3, degrees=angle)
        servos.position(index=channel_2, degrees=new_angle)
        servos.position(index=channel_4, degrees=new_angle)
        time.sleep(0.3)
    counter = 0


multiple_leg_movement_tester()
