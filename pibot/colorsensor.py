import RPi.GPIO as GPIO
from pibot import constants as c


def init_color_sensor():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(c.COLOR_SENSOR_S2, GPIO.OUT)
    GPIO.setup(c.COLOR_SENSOR_S3, GPIO.OUT)
