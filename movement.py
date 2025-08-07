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
    # channel_2 = 5
    # channel_3 = 9
    # channel_4 = 13

    angle = 90
    servos.position(index=channel_1, degrees=angle)
    servos.position(index=channel_2, degrees=angle)
    servos.position(index=channel_3, degrees=angle)
    servos.position(index=channel_4, degrees=angle)

    for angle in range(50, 130, 5):
        servos.position(index=channel_1, degrees=angle)
        time.sleep(0.1)
    for angle in range(130, 50, -5):
        servos.position(index=channel_1, degrees=angle)
        time.sleep(0.1)
    for angle in range(50, 90, 5):
        servos.position(index=channel_1, degrees=angle)
        time.sleep(0.1)

    for angle in range(50, 130, 5):
        servos.position(index=channel_3, degrees=angle)
        time.sleep(0.1)
    for angle in range(130, 50, -5):
        servos.position(index=channel_3, degrees=angle)
        time.sleep(0.1)
    for angle in range(50, 90, 5):
        servos.position(index=channel_3, degrees=angle)
        time.sleep(0.1)

    for angle in range(130, 50, -5):
        servos.position(index=channel_2, degrees=angle)
        time.sleep(0.1)
    for angle in range(50, 130, 5):
        servos.position(index=channel_2, degrees=angle)
        time.sleep(0.1)
    for angle in range(130, 90, -5):
        servos.position(index=channel_2, degrees=angle)
        time.sleep(0.1)

    for angle in range(130, 50, -5):
        servos.position(index=channel_4, degrees=angle)
        time.sleep(0.1)
    for angle in range(50, 130, 5):
        servos.position(index=channel_4, degrees=angle)
        time.sleep(0.1)
    for angle in range(130, 90, -5):
        servos.position(index=channel_4, degrees=angle)
        time.sleep(0.1)


def multiple_leg_movement_tester():
    """
    Test the movement of multiple legs.
    This function should be implemented based on your specific requirements.
    """
    # shoulder
    channel_1 = 0
    channel_2 = 4
    channel_3 = 8
    channel_4 = 12

    # thy
    # channel_1 = 1
    # channel_2 = 5
    # channel_3 = 9
    # channel_4 = 13

    angle = 90
    servos.position(index=channel_1, degrees=angle)
    servos.position(index=channel_2, degrees=angle)
    servos.position(index=channel_3, degrees=angle)
    servos.position(index=channel_4, degrees=angle)
    counter = 5
    for angle in range(50, 130, 5):
        servos.position(index=channel_1, degrees=angle)
        servos.position(index=channel_3, degrees=angle)
        servos.position(index=channel_2, degrees=angle)
        servos.position(index=channel_4, degrees=angle)
        time.sleep(0.3)


boomer_leg_limit_checker()
