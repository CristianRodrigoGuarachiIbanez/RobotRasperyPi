import time

import RPi.GPIO as GPIO
from time import sleep
from pibot.serial_comm import (write_order,
                               Order,
                               read_i16,
                               write_i8,
                               read_ui8,
                               write_ui16)
from pibot.utils import open_serial_port, clamp
import pibot.constants as c
import struct
from typing import Tuple, List, Dict

class Nano:
    def __init__(self):
        # Reset Nano
        print("Resetting Nano...")
        self.reset_nano()

        print("Waiting for Serial Connection to Nano...")
        sleep(5)

        try:
            self.serial_file = open_serial_port(baudrate=115200, timeout=None)
        except Exception as e:
            raise e

        is_connected = False

        # Initialize communication with Arduino
        print("Requesting Connection to Nano...")
        while not is_connected:
            write_order(self.serial_file, Order.START)
            if self.serial_file.inWaiting():
                byte = self.serial_file.read(1)
                if struct.unpack('B', byte)[0] == Order.CONNECTED.value:
                    is_connected = True
            else:
                time.sleep(1)
        print("Connected to Nano.")

        # voltage check (minimum: 6500 mV, for testing: 7000mV)

        voltage = self.get_battery_voltage()
        if voltage < 7000:
            print("Warning! Battery voltage low! ({} mV)".format(voltage))
            # popen("sudo poweroff")
        else:
            print("Battery voltage okay! ({} mV)".format(voltage))

    def set_stat_led(self, toggle):
        write_order(self.serial_file, order=Order.STAT_LED)
        write_i8(self.serial_file, toggle)

    def open_gripper(self):
        write_order(self.serial_file, order=Order.GRIPPER)
        write_i8(self.serial_file, 0)

    def close_gripper(self):
        write_order(self.serial_file, order=Order.GRIPPER)
        write_i8(self.serial_file, 1)

    def set_motors(self, left, right):
        write_order(self.serial_file, order=Order.MOTORS)
        # Write left
        write_i8(self.serial_file, clamp(left, -128, 127))
        # Write right
        write_i8(self.serial_file, clamp(right, -128, 127))

    def get_encoders(self):
        write_order(self.serial_file, order=Order.GET_ENCODERS)

        # Wait for 2 values
        left = read_i16(self.serial_file)
        right = read_i16(self.serial_file)
        return left, right

    def get_line_sensors(self):
        write_order(self.serial_file, order=Order.GET_LINE_SENSORS)

        # Wait for 3 values
        left = read_i16(self.serial_file)
        mid = read_i16(self.serial_file)
        right = read_i16(self.serial_file)
        return left, mid, right

    def reset_encoders(self):
        write_order(self.serial_file, order=Order.RESET_ENCODERS)

    def get_battery_voltage(self):
        write_order(self.serial_file, order=Order.VOLTAGE)
        return read_i16(self.serial_file)

    def get_distances(self):
        write_order(self.serial_file, order=Order.DISTANCES)

        # Wait for 3 values
        left = read_ui8(self.serial_file)
        mid = read_ui8(self.serial_file)
        right = read_ui8(self.serial_file)
        return left, mid, right

    def set_buzzer(self, freq, duration):
        write_order(self.serial_file, order=Order.BUZZER)
        # send the frequency
        write_ui16(self.serial_file, freq)
        # send the duration
        write_ui16(self.serial_file, duration)

    def get_color_rgb(self):
        # red
        GPIO.output(c.COLOR_SENSOR_S2, GPIO.LOW)
        GPIO.output(c.COLOR_SENSOR_S3, GPIO.LOW)
        write_order(self.serial_file, order=Order.COLOR)
        red = read_i16(self.serial_file)

        # blue
        GPIO.output(c.COLOR_SENSOR_S2, GPIO.LOW)
        GPIO.output(c.COLOR_SENSOR_S3, GPIO.HIGH)
        write_order(self.serial_file, order=Order.COLOR)
        blue = read_i16(self.serial_file)

        # green
        GPIO.output(c.COLOR_SENSOR_S2, GPIO.HIGH)
        GPIO.output(c.COLOR_SENSOR_S3, GPIO.HIGH)
        write_order(self.serial_file, order=Order.COLOR)
        green = read_i16(self.serial_file)

        return red, green, blue

    def get_color(self):
        # red
        GPIO.output(c.COLOR_SENSOR_S2, GPIO.LOW)
        GPIO.output(c.COLOR_SENSOR_S3, GPIO.LOW)
        write_order(self.serial_file, order=Order.COLOR)
        red = read_i16(self.serial_file)

        # blue
        GPIO.output(c.COLOR_SENSOR_S2, GPIO.LOW)
        GPIO.output(c.COLOR_SENSOR_S3, GPIO.HIGH)
        write_order(self.serial_file, order=Order.COLOR)
        blue = read_i16(self.serial_file)

        # green
        GPIO.output(c.COLOR_SENSOR_S2, GPIO.HIGH)
        GPIO.output(c.COLOR_SENSOR_S3, GPIO.HIGH)
        write_order(self.serial_file, order=Order.COLOR)
        green = read_i16(self.serial_file)

        if red > green and blue > green:
            return "green"
        elif red > blue and green > blue:
            return "blue"
        elif green > red and blue > red:
            return "red"
        else:
            return "none"

    @staticmethod
    def reset_nano():
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(4, GPIO.OUT)
        GPIO.output(4, GPIO.LOW)
        sleep(0.001)
        GPIO.output(4, GPIO.HIGH)
