from pibot.nano import Nano
from time import sleep
from pibot import leds
from pibot import constants as c
from pibot import buttons
from pibot import colorsensor


def test_motors():
    print(nano.get_encoders())
    nano.set_motors(50, 50)
    sleep(1)
    nano.set_motors(0, 0)
    print(nano.get_encoders())
    nano.set_motors(-50, -50)
    sleep(1)
    nano.set_motors(0, 0)
    print(nano.get_encoders())


def test_front_leds():
    leds.init_leds()
    leds.set_led(c.LED_FRONT_LEFT, c.ON)
    leds.set_led(c.LED_FRONT_RIGHT, c.ON)
    sleep(2)
    leds.set_led(c.LED_FRONT_LEFT, c.OFF)
    leds.set_led(c.LED_FRONT_RIGHT, c.OFF)


def test_mid_button():
    buttons.init_buttons()
    buttons.wait_for_button(c.BUTTON_MID)


def test_ultrasonics():
    for _ in range(10):
        dist = nano.get_distances()
        print(dist)
        sleep(0.5)


def test_gripper():

    nano.close_gripper()
    sleep(1)
    nano.open_gripper()
    sleep(1)
    nano.close_gripper()
    sleep(1)
    nano.open_gripper()


def test_line_sensors():
    for _ in range(10):
        print(nano.get_line_sensors())
        sleep(1)


def test_color_sensor():

    colorsensor.init_color_sensor()
    for _ in range(10):
        print(nano.get_color())
        sleep(1)


def main():
    nano.set_motors(0, 0)
    nano.reset_encoders()

    test_motors()

    test_front_leds()
    test_ultrasonics()

    test_gripper()
    test_line_sensors()

    test_color_sensor()


if __name__ == "__main__":
    nano = Nano()
    main()
