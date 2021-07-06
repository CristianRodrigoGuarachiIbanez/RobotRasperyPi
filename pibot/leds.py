import RPi.GPIO as GPIO

from pibot import constants as c
from time import sleep


def init_leds():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    pins = [c.LED_LEFT_RED_PIN,
            c.LED_LEFT_GREEN_PIN,
            c.LED_MID_RED_PIN,
            c.LED_MID_GREEN_PIN,
            c.LED_RIGHT_RED_PIN,
            c.LED_RIGHT_GREEN_PIN,
            c.LED_FRONT_LEFT_PIN,
            c.LED_FRONT_RIGHT_PIN
            ]

    GPIO.setup(pins, direction=GPIO.OUT, initial=0)


def set_led(led, color):
    if led == c.LED_LEFT:
        if color == c.RED:
            GPIO.output(c.LED_LEFT_RED_PIN, GPIO.HIGH)
            GPIO.output(c.LED_LEFT_GREEN_PIN, GPIO.LOW)
        elif color == c.GREEN:
            GPIO.output(c.LED_LEFT_RED_PIN, GPIO.LOW)
            GPIO.output(c.LED_LEFT_GREEN_PIN, GPIO.HIGH)
        elif color == c.YELLOW:
            GPIO.output(c.LED_LEFT_RED_PIN, GPIO.HIGH)
            GPIO.output(c.LED_LEFT_GREEN_PIN, GPIO.HIGH)
        elif color == c.OFF:
            GPIO.output(c.LED_LEFT_RED_PIN, GPIO.LOW)
            GPIO.output(c.LED_LEFT_GREEN_PIN, GPIO.LOW)
        else:
            raise Exception("Color {} not supported".format(color))
    elif led == c.LED_MID:
        if color == c.RED:
            GPIO.output(c.LED_MID_RED_PIN, GPIO.HIGH)
            GPIO.output(c.LED_MID_GREEN_PIN, GPIO.LOW)
        elif color == c.GREEN:
            GPIO.output(c.LED_MID_RED_PIN, GPIO.LOW)
            GPIO.output(c.LED_MID_GREEN_PIN, GPIO.HIGH)
        elif color == c.YELLOW:
            GPIO.output(c.LED_MID_RED_PIN, GPIO.HIGH)
            GPIO.output(c.LED_MID_GREEN_PIN, GPIO.HIGH)
        elif color == c.OFF:
            GPIO.output(c.LED_MID_RED_PIN, GPIO.LOW)
            GPIO.output(c.LED_MID_GREEN_PIN, GPIO.LOW)
        else:
            raise Exception("Color {} not supported".format(color))
    elif led == c.LED_RIGHT:
        if color == c.RED:
            GPIO.output(c.LED_RIGHT_RED_PIN, GPIO.HIGH)
            GPIO.output(c.LED_RIGHT_GREEN_PIN, GPIO.LOW)
        elif color == c.GREEN:
            GPIO.output(c.LED_RIGHT_RED_PIN, GPIO.LOW)
            GPIO.output(c.LED_RIGHT_GREEN_PIN, GPIO.HIGH)
        elif color == c.YELLOW:
            GPIO.output(c.LED_RIGHT_RED_PIN, GPIO.HIGH)
            GPIO.output(c.LED_RIGHT_GREEN_PIN, GPIO.HIGH)
        elif color == c.OFF:
            GPIO.output(c.LED_RIGHT_RED_PIN, GPIO.LOW)
            GPIO.output(c.LED_RIGHT_GREEN_PIN, GPIO.LOW)
        else:
            raise Exception("Color {} not supported".format(color))
    elif led == c.LED_FRONT_LEFT:
        if color == c.ON:
            GPIO.output(c.LED_FRONT_LEFT_PIN, GPIO.HIGH)
        elif color == c.OFF:
            GPIO.output(c.LED_FRONT_LEFT_PIN, GPIO.LOW)
        else:
            raise Exception("Color {} not supported".format(color))
    elif led == c.LED_FRONT_RIGHT:
        if color == c.ON:
            GPIO.output(c.LED_FRONT_RIGHT_PIN, GPIO.HIGH)
        elif color == c.OFF:
            GPIO.output(c.LED_FRONT_RIGHT_PIN, GPIO.LOW)
        else:
            raise Exception("Color {} not supported".format(color))


def check_leds():
    # front
    # ON
    GPIO.output(c.LED_FRONT_LEFT_PIN, GPIO.HIGH)
    GPIO.output(c.LED_FRONT_RIGHT_PIN, GPIO.HIGH)
    sleep(0.1)
    GPIO.output(c.LED_FRONT_LEFT_PIN, GPIO.LOW)
    GPIO.output(c.LED_FRONT_RIGHT_PIN, GPIO.LOW)
    sleep(0.1)
    GPIO.output(c.LED_FRONT_LEFT_PIN, GPIO.HIGH)
    GPIO.output(c.LED_FRONT_RIGHT_PIN, GPIO.HIGH)
    sleep(0.1)
    GPIO.output(c.LED_FRONT_LEFT_PIN, GPIO.LOW)
    GPIO.output(c.LED_FRONT_RIGHT_PIN, GPIO.LOW)

    # others
    # RED LEFT
    GPIO.output(c.LED_LEFT_RED_PIN, GPIO.HIGH)
    GPIO.output(c.LED_LEFT_GREEN_PIN, GPIO.LOW)
    sleep(0.05)
    # RED MID
    GPIO.output(c.LED_MID_RED_PIN, GPIO.HIGH)
    GPIO.output(c.LED_MID_GREEN_PIN, GPIO.LOW)
    sleep(0.05)
    # RED RIGHT
    GPIO.output(c.LED_RIGHT_RED_PIN, GPIO.HIGH)
    GPIO.output(c.LED_RIGHT_GREEN_PIN, GPIO.LOW)
    sleep(0.5)

    # YELLOW LEFT
    GPIO.output(c.LED_LEFT_RED_PIN, GPIO.HIGH)
    GPIO.output(c.LED_LEFT_GREEN_PIN, GPIO.HIGH)
    sleep(0.05)
    # YELLOW  MID
    GPIO.output(c.LED_MID_RED_PIN, GPIO.HIGH)
    GPIO.output(c.LED_MID_GREEN_PIN, GPIO.HIGH)
    sleep(0.05)
    # YELLOW RIGHT
    GPIO.output(c.LED_RIGHT_RED_PIN, GPIO.HIGH)
    GPIO.output(c.LED_RIGHT_GREEN_PIN, GPIO.HIGH)
    sleep(0.5)

    # GREEN LEFT
    GPIO.output(c.LED_LEFT_RED_PIN, GPIO.LOW)
    GPIO.output(c.LED_LEFT_GREEN_PIN, GPIO.HIGH)
    sleep(0.05)
    # GREEN MID
    GPIO.output(c.LED_MID_RED_PIN, GPIO.LOW)
    GPIO.output(c.LED_MID_GREEN_PIN, GPIO.HIGH)
    sleep(0.05)
    # GREEN RIGHT
    GPIO.output(c.LED_RIGHT_RED_PIN, GPIO.LOW)
    GPIO.output(c.LED_RIGHT_GREEN_PIN, GPIO.HIGH)
    sleep(1)

    # OFF LEFT
    GPIO.output(c.LED_LEFT_RED_PIN, GPIO.LOW)
    GPIO.output(c.LED_LEFT_GREEN_PIN, GPIO.LOW)
    # OFF MID
    GPIO.output(c.LED_MID_RED_PIN, GPIO.LOW)
    GPIO.output(c.LED_MID_GREEN_PIN, GPIO.LOW)
    # OFF RIGHT
    GPIO.output(c.LED_RIGHT_RED_PIN, GPIO.LOW)
    GPIO.output(c.LED_RIGHT_GREEN_PIN, GPIO.LOW)
