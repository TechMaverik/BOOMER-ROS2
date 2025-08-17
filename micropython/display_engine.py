"""display engine.py"""

"""
Since OLED display driver shows some anomalities in loading classes. I am writing the display contents 
in a general module
"""
from image_archives import *
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import time

WIDTH = 128
HEIGHT = 64
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=200000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

PI_FRAME_BUFFER = framebuf.FrameBuffer(PI, 32, 32, framebuf.MONO_HLSB)
ARCH_FRAME_BUFFER = framebuf.FrameBuffer(ARCH, 128, 64, framebuf.MONO_HLSB)
OPEN_EYES_FRAME_BUFFER = framebuf.FrameBuffer(OPEN_EYES, 128, 64, framebuf.MONO_HLSB)
CLOSE_EYES_FRAME_BUFFER = framebuf.FrameBuffer(CLOSE_EYES, 128, 64, framebuf.MONO_HLSB)
LOGO_FRAME_BUFFER = framebuf.FrameBuffer(LOGO, 128, 64, framebuf.MONO_HLSB)
SAD_FACE_FRAME_BUFFER = framebuf.FrameBuffer(SAD_FACE, 128, 64, framebuf.MONO_HLSB)
HAPPY_FRAME_BUFFER = framebuf.FrameBuffer(HAPPY, 128, 64, framebuf.MONO_HLSB)
IDLE_FRAME_BUFFER = framebuf.FrameBuffer(IDLE, 128, 64, framebuf.MONO_HLSB)
WATER_FRAME_BUFFER = framebuf.FrameBuffer(WATER, 128, 64, framebuf.MONO_HLSB)


def startup():
    """Startup"""
    oled.fill(0)
    oled.blit(PI_FRAME_BUFFER, 96, 0)
    oled.text("BOOMER V 3.0", 0, 0)
    time.sleep(1)
    oled.show()
    time.sleep(1)
    oled.text("HL", 0, 20)
    oled.text("Engine 3.0", 0, 30)
    oled.show()
    time.sleep(2)
    oled.fill(0)
    oled.show()
    time.sleep(2)
    oled.text("Built using", 0, 30)
    oled.show()
    time.sleep(2)
    oled.fill(0)
    oled.show()
    time.sleep(2)
    oled.blit(ARCH_FRAME_BUFFER, 0, 0)
    oled.show()
    time.sleep(2)
    oled.fill(0)
    oled.show()
    time.sleep(2)
    oled.blit(LOGO_FRAME_BUFFER, 0, 0)
    oled.show()


def blink_eye():
    """Blink eyes"""
    while True:
        oled.fill(0)
        oled.blit(OPEN_EYES_FRAME_BUFFER, 0, 0)
        oled.show()
        time.sleep(1)
        oled.fill(0)
        oled.blit(CLOSE_EYES_FRAME_BUFFER, 0, 0)
        oled.show()
        time.sleep(1)


def open_eyes():
    """Open eyes"""
    oled.fill(0)
    oled.blit(OPEN_EYES_FRAME_BUFFER, 0, 0)
    oled.show()
    time.sleep(0.25)


def close_eyes():
    """Close eyes"""
    oled.fill(0)
    oled.blit(CLOSE_EYES_FRAME_BUFFER, 0, 0)
    oled.show()
    time.sleep(0.25)


def look_close():
    """Look close"""
    oled.fill(0)
    oled.blit(IDLE_FRAME_BUFFER, 0, 0)
    oled.show()
    time.sleep(1)


def happy_face():
    """Happy face"""
    oled.fill(0)
    oled.blit(HAPPY_FRAME_BUFFER, 0, 0)
    oled.show()
    time.sleep(1)


def sad_face():
    """Happy face"""
    oled.fill(0)
    oled.blit(SAD_FACE_FRAME_BUFFER, 0, 0)
    oled.show()
    time.sleep(1)
