import RPi.GPIO as GPIO
import subprocess
from os import popen
from time import sleep
from picamera import PiCamera
from PIL import Image
from io import BytesIO

from pibot.lcd import LCD
from pibot.nano import Nano
from pibot.buttons import *
from pibot import constants as c
from pibot import leds
from pibot import colorsensor


MENU_TOGGLE_PIN = 21


def background():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(MENU_TOGGLE_PIN, GPIO.IN, GPIO.PUD_UP)
    lcd = LCD(fontsize=21)

    while 1:
        if is_pressed(MENU_TOGGLE_PIN):
            menu(lcd)
        sleep(0.5)


def menu(lcd):
    init_buttons()

    menu_entries = [('Exit', exit_menu),
                    ('Poweroff', poweroff),
                    ('Show IP', show_ip),
                    ('Motor Test', actuator_test),
                    ('US-Sensor Test', sensor_test),
                    ('LED Test', led_test),
                    ('Camera Test', camera_test),
                    ('Buzzer Test', buzzer_test),
                    ('L-Sensor Test', l_sensor_test),
                    ('Greifer Test', gripper_test),
                    ('C-Sensor Test', c_sensor_test), ]

    current = 1
    in_menu = True
    while in_menu:
        message = [str(menu_entries[current][0]),
                   "",
                   "<-       ok       ->"]
        lcd.print(message)
        button = wait_for_any()
        if button == c.BUTTON_LEFT:
            current -= 1
        elif button == c.BUTTON_MID:
            menu_entries[current][1](lcd)
            if current == 0 or current == 1:
                in_menu = False
                lcd.clear()
        elif button == c.BUTTON_RIGHT:
            current += 1
        current %= len(menu_entries)
        sleep(0.02)


def exit_menu(lcd):
    pass


def poweroff(lcd):
    message = ["Are you sure?",
               "",
               "Yes            No"]
    lcd.print(message)
    button = wait_for_any()
    if button == c.BUTTON_LEFT:
        message = ["  Shutdown...",
                   "",
                   ""]
        lcd.print(message)
        sleep(1)
        popen("sudo poweroff")


def show_ip(lcd):
    cmd = "hostname -I | cut -d\' \' -f1"
    ip = (subprocess.check_output(cmd, shell=True)).decode("utf-8")
    leds.init_leds()
    leds.set_led(c.LED_MID, c.GREEN)
    message = ["IP:",
               str(ip),
               "              "]
    lcd.set_fontsize(17)
    lcd.print(message)
    lcd.set_fontsize(21)
    wait_for_button(c.BUTTON_MID)
    leds.set_led(c.LED_MID, c.OFF)


def actuator_test(lcd):
    message = ["Requesting",
               "Nano!",
               ""]
    lcd.print(message)
    nano = Nano()
    while nano.get_battery_voltage() == 0:
        message = ["Please plug in",
                   "the 9V battery!",
                   "              "]
        lcd.print(message)
        sleep(0.5)

    message = ["Make sure the",
               "motors are",
               "powered on!"]
    lcd.print(message)
    leds.init_leds()
    leds.set_led(c.LED_MID, c.GREEN)
    wait_for_button(c.BUTTON_MID)
    leds.set_led(c.LED_MID, c.OFF)

    nano.reset_encoders()
    nano.set_motors(-30, 30)
    sleep(2)
    nano.set_motors(30, -30)
    sleep(2)
    nano.set_motors(0, 0)
    message = [str(nano.get_encoders())]
    lcd.print(message)

    leds.set_led(c.LED_MID, c.GREEN)
    wait_for_button(c.BUTTON_MID)
    leds.set_led(c.LED_MID, c.OFF)


def sensor_test(lcd):
    message = ["Requesting",
               "Nano!",
               ""]
    lcd.print(message)
    nano = Nano()
    leds.init_leds()
    leds.set_led(c.LED_MID, c.GREEN)
    while not is_pressed(c.BUTTON_MID):
        message = [str(nano.get_distances()),
                   "",
                   "          ok"]
        lcd.print(message)
    leds.set_led(c.LED_MID, c.OFF)


def l_sensor_test(lcd):
    message = ["Requesting",
               "Nano!",
               ""]
    lcd.print(message)
    nano = Nano()
    leds.init_leds()
    leds.set_led(c.LED_MID, c.GREEN)
    while not is_pressed(c.BUTTON_MID):
        message = [str(nano.get_line_sensors()),
                   "",
                   "          ok"]
        lcd.print(message)
    leds.set_led(c.LED_MID, c.OFF)


def gripper_test(lcd):
    message = ["Requesting",
               "Nano!",
               ""]
    lcd.print(message)
    nano = Nano()
    leds.init_leds()
    leds.set_led(c.LED_MID, c.GREEN)
    message = ["",
               "",
               "open      close"]
    lcd.print(message)
    end = False
    while not end:
        button = wait_for_any()
        if button == c.BUTTON_RIGHT:
            nano.close_gripper()
        elif button == c.BUTTON_LEFT:
            nano.open_gripper()
        else:
            end = True
        sleep(0.5)
    nano.open_gripper()
    leds.set_led(c.LED_MID, c.OFF)


def c_sensor_test(lcd):
    message = ["Requesting",
               "Nano!",
               ""]
    lcd.print(message)
    nano = Nano()
    leds.init_leds()
    leds.set_led(c.LED_MID, c.GREEN)
    colorsensor.init_color_sensor()
    while not is_pressed(c.BUTTON_MID):
        message = [str(nano.get_color()),
                   "",
                   "          ok"]
        lcd.print(message)
    leds.set_led(c.LED_MID, c.OFF)


def led_test(lcd):
    message = ["Testing",
               "LEDs!",
               ""]
    lcd.print(message)
    leds.init_leds()
    leds.check_leds()


IMAGE_PATH = "/home/pi/Pictures/"


def camera_test(lcd):
    leds.init_leds()
    with PiCamera() as cam:
        cam.resolution = lcd.get_resolution()
        cam.rotation = 180

        leds.set_led(c.LED_MID, c.GREEN)
        leds.set_led(c.LED_FRONT_LEFT, c.ON)
        leds.set_led(c.LED_FRONT_RIGHT, c.ON)
        while not is_pressed(c.BUTTON_MID):
            stream = BytesIO()
            cam.capture(stream, 'jpeg')
            stream.seek(0)
            image = Image.open(stream)
            lcd.view_pil_image(image)
        leds.set_led(c.LED_MID, c.OFF)
        leds.set_led(c.LED_FRONT_LEFT, c.OFF)
        leds.set_led(c.LED_FRONT_RIGHT, c.OFF)
        wait_for_button_release(c.BUTTON_MID)


def buzzer_test(lcd):
    message = ["Requesting",
               "Nano!",
               ""]
    lcd.print(message)
    nano = Nano()
    lcd.clear()
    nano.set_buzzer(660, 100)
    sleep(0.150)
    nano.set_buzzer(660, 100)
    sleep(0.300)
    nano.set_buzzer(660, 100)
    sleep(0.300)
    nano.set_buzzer(510, 100)
    sleep(0.100)
    nano.set_buzzer(660, 100)
    sleep(0.300)
    nano.set_buzzer(770, 100)
    sleep(0.550)
    nano.set_buzzer(380, 100)
    sleep(0.575)
