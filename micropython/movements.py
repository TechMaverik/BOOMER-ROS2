import time
from servo import Servos
from pca9685 import PCA9685
from machine import I2C, Pin


class Movements:

    def __init__(self):
        self.i2c = I2C(0, scl=Pin(22), sda=Pin(21))
        self.pca = PCA9685(self.i2c)
        self.pca.freq(50)
        self.servos = Servos(self.i2c)
        self.channel_1 = 0
        self.channel_2 = 4
        self.channel_3 = 8
        self.channel_4 = 12
        self.channel_5 = 1
        self.channel_6 = 5
        self.channel_7 = 9
        self.channel_8 = 13
        self.channel_9 = 2
        self.channel_10 = 6
        self.channel_11 = 10
        self.channel_12 = 14
        self.default_angle = 90
        self.speed = 20

    def set_to_default_positions(self):
        self.servos.position(index=self.channel_1, degrees=self.default_angle)
        time.sleep(0.3)
        self.servos.position(index=self.channel_2, degrees=self.default_angle)
        time.sleep(0.3)
        self.servos.position(index=self.channel_3, degrees=self.default_angle)
        time.sleep(0.3)
        self.servos.position(index=self.channel_4, degrees=self.default_angle)
        time.sleep(0.3)

        self.servos.position(index=self.channel_5, degrees=150)
        time.sleep(0.3)
        self.servos.position(index=self.channel_6, degrees=30)
        time.sleep(0.3)
        self.servos.position(index=self.channel_7, degrees=150)
        time.sleep(0.3)
        self.servos.position(index=self.channel_8, degrees=30)
        time.sleep(0.3)

        self.servos.position(index=self.channel_9, degrees=0)
        time.sleep(0.3)
        self.servos.position(index=self.channel_10, degrees=180)
        time.sleep(0.3)
        self.servos.position(index=self.channel_11, degrees=0)
        time.sleep(0.3)
        self.servos.position(index=self.channel_12, degrees=180)
        time.sleep(0.3)

    def set_to_x_position(self):
        self.servos.position(index=self.channel_1, degrees=50)
        time.sleep(1)
        self.servos.position(index=self.channel_3, degrees=130)
        time.sleep(1)
        self.servos.position(index=self.channel_2, degrees=130)
        time.sleep(1)
        self.servos.position(index=self.channel_4, degrees=50)

    def set_to_standing_position(self):
        counter = 0
        for angle in range(90, 30, -self.speed):
            counter = counter + self.speed
            new_angle = 90 + counter
            print(new_angle)
            self.servos.position(index=self.channel_5, degrees=angle)
            self.servos.position(index=self.channel_7, degrees=angle)
            self.servos.position(index=self.channel_6, degrees=new_angle)
            self.servos.position(index=self.channel_8, degrees=new_angle)
            time.sleep(0.3)

        # self.servos.position(index=self.channel_9, degrees=0)
        # self.servos.position(index=self.channel_11, degrees=0)
        # self.servos.position(index=self.channel_10, degrees=180)
        # self.servos.position(index=self.channel_12, degrees=180)

        self.servos.position(index=self.channel_9, degrees=90)
        self.servos.position(index=self.channel_11, degrees=90)
        self.servos.position(index=self.channel_10, degrees=90)
        self.servos.position(index=self.channel_12, degrees=90)
        time.sleep(0.3)

        self.servos.position(index=self.channel_5, degrees=90)
        time.sleep(1)
        self.servos.position(index=self.channel_8, degrees=90)
        time.sleep(1)
        self.servos.position(index=self.channel_7, degrees=90)
        time.sleep(1)
        self.servos.position(index=self.channel_6, degrees=90)
        time.sleep(1)
        self.set_to_x_position()

    def set_to_sit_down_position(self):
        counter = 0
        for angle in range(0, 150, self.speed):
            counter = counter + self.speed
            new_angle = 180 - counter
            print(new_angle)
            self.servos.position(index=self.channel_9, degrees=angle)
            self.servos.position(index=self.channel_11, degrees=angle)
            self.servos.position(index=self.channel_10, degrees=new_angle)
            self.servos.position(index=self.channel_12, degrees=new_angle)
            time.sleep(0.3)

    def set_to_move_forward(self):
        time.sleep(1)
        self.servos.position(index=self.channel_1, degrees=120)
        self.servos.position(index=self.channel_5, degrees=90)
        self.servos.position(index=self.channel_9, degrees=90)
        time.sleep(1)
        self.servos.position(index=self.channel_2, degrees=50)
        self.servos.position(index=self.channel_6, degrees=90)
        self.servos.position(index=self.channel_10, degrees=90)
        time.sleep(1)
        self.servos.position(index=self.channel_1, degrees=50)
        self.servos.position(index=self.channel_2, degrees=130)
        self.servos.position(index=self.channel_3, degrees=90)
        self.servos.position(index=self.channel_4, degrees=90)
        time.sleep(1)
        self.set_to_x_position()
