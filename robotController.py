# -*- coding: utf-8 -*-
from pibot.nano import Nano
from pibot.leds import set_led, init_leds
from pibot import constants as c
from typing import List, Tuple, Dict, Callable, TypeVar, Any
from logging import info, INFO, DEBUG
import logging
from sys import exit
logging.basicConfig(filename='debugging.log' ,level=INFO, format='%(asctime)s:%(levelname)s:%(message)s');

class RobotController(Nano):
    B = TypeVar('B', bytearray, bytes);
    _MAX_SPEED= 30;
    _SPEED=20
    _MID_SPEED=-5;
    _LOW_SPEED=5;
    _STOP=0;
    def __init__(self) -> None:
        super(RobotController, self).__init__(); # Nano.__init__()
    def driveTroughATunnel(self)->None:
        print('driving through a tunnel')
        self.ledsStart()
        self.driveStraigthforward((30,30))
    def ledsStart(self)->None:
        init_leds()
        set_led(c.LED_MID, c.RED)
        set_led(c.LED_RIGHT, c.YELLOW)
        set_led(c.LED_LEFT, c.GREEN)
        set_led(c.LED_FRONT_LEFT, c.ON)
        set_led(c.LED_FRONT_RIGHT, c.ON)
    def ledsEnd(self)->None:
        if(self.get_distances()[0]>10 and self.get_distances()[0]!=0):
            if(self.get_distances()[1] >10 and self.get_distances()[1]!=0):
                set_led(c.LED_FRONT_LEFT, c.OFF)
                set_led(c.LED_FRONT_RIGHT, c.OFF)

    def driveStraigthforward(self, speed=None) -> None:
        if(speed is not None):
            assert (isinstance(speed, (list, tuple))), 'speed should be tuple or list'
            self.set_motors(speed[0],speed[1]);
            print('driving forward')
        else:
            self.set_motors(self._SPEED, self._SPEED);
            print('driving forward')

    def _stop(self) -> None:
        self.set_motors(self._STOP,self._STOP);
        print('stop')
    def _park(self)->None:
        self._stop()
        self.set_buzzer(3, 0)
        exit("exit the programm")
    def _turnRightActions(self, flag) -> None:

        if (flag is None):
            self.set_motors(self._MAX_SPEED, self._MID_SPEED);
            print('action -> OC-Right')
        else:
            self.set_motors(flag[0], flag[1]);
            print('action -> CC-Right');

    def _turnLeftActions(self,flag)->None:

        if (flag is None):
            self.set_motors(self._MID_SPEED, self._MAX_SPEED);
            print('action -> OC-Left')
        else:
            self.set_motors(flag[0], flag[1]);
            print('action -> CC-Left');

    def _spinRight(self) -> None:
        self.set_motors(self._MAX_SPEED,self._STOP);
        print('spin right')

    def _spinLeft(self) -> None:
        self.set_motors(self._STOP, self._MAX_SPEED);
        print('spin left')

    @staticmethod
    def _convertIntToBool(limit, obstacle)->List[bool]:
        cL = obstacle[0] <= limit and obstacle[0]!=0;  # clo -> 80-40 < x < 80
        cM = obstacle[1] <= limit and obstacle[1]!=0;
        cR = obstacle[2] <= limit and obstacle[2]!=0;

        return [cL, cM, cR];

