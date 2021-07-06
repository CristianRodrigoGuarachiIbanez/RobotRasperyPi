import subprocess

from pibot import leds

from time import sleep
from pibot.nano import Nano
from pibot.lcd import LCD
import RPi.GPIO as GPIO
from pibot.background import background


def startup():
    lcd = LCD(fontsize=16)
    GPIO.setwarnings(False)

    # show TU-Chemnitz logo on screen
    lcd.view_image("/home/pi/.resources/tu.pgm", 1)

    sleep(2)
    # show TU-Chemnitz text on screen
    lcd.view_image("/home/pi/.resources/tutext.pgm", 1)

#    sleep(2)
    # show Roboschool logo on screen
#    lcd.view_image("/home/pi/.resources/roboschool.pgm", 1)

    sleep(2)
    # show PiBot logo on screen
    lcd.view_image("/home/pi/.resources/pibot.pgm", 1)

    # getting IP
    cmd = "hostname -I | cut -d\' \' -f1"
    ip = (subprocess.check_output(cmd, shell=True)).decode("utf-8")

    # getting voltage
    nano = Nano()
    voltage = nano.get_battery_voltage()

    message = ["IP: ",
               str(ip),     # on newline for IP's with mostly 3 digits
                            # (xxx.xxx.xxx.xxx)
               "Battery: {} mV".format(voltage)]
    lcd.print(message)
    sleep(2)
