from machine import I2C, Pin
from time import sleep

# MPU6050 I2C address
MPU6050_ADDR = 0x68

# MPU6050 Registers
PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B
GYRO_XOUT_H = 0x43

# Initialize I2C
i2c = I2C(0, scl=Pin(22), sda=Pin(21))  # Adjust pins if needed

# Wake up MPU6050
i2c.writeto_mem(MPU6050_ADDR, PWR_MGMT_1, b"\x00")


# Helper to read 16-bit signed values
def read_word(reg):
    high = i2c.readfrom_mem(MPU6050_ADDR, reg, 1)[0]
    low = i2c.readfrom_mem(MPU6050_ADDR, reg + 1, 1)[0]
    value = (high << 8) | low
    if value >= 0x8000:
        value = -((65535 - value) + 1)
    return value


# Main loop
def read_mpu6050():
    # Accelerometer
    ax = read_word(ACCEL_XOUT_H) / 16384.0
    ay = read_word(ACCEL_XOUT_H + 2) / 16384.0
    az = read_word(ACCEL_XOUT_H + 4) / 16384.0

    # Gyroscope
    gx = read_word(GYRO_XOUT_H) / 131.0
    gy = read_word(GYRO_XOUT_H + 2) / 131.0
    gz = read_word(GYRO_XOUT_H + 4) / 131.0

    # print("Accel: X={:.2f}g Y={:.2f}g Z={:.2f}g".format(ax, ay, az))
    # print("Gyro : X={:.2f}°/s Y={:.2f}°/s Z={:.2f}°/s".format(gx, gy, gz))
    # print("-" * 40)
    sleep(0.5)
    return (ax, ay, az, gx, gy, gz)
