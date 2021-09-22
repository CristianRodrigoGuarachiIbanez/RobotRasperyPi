# -*- coding: utf-8 -*-
import sys
from pibot.nano import Nano
from pibot.leds import set_led, init_leds
from pibot import constants as c
from typing import List, Tuple, Dict, Callable, TypeVar, Any
from logging import info, INFO, DEBUG
import logging
logging.basicConfig(filename='debugging.log' ,level=INFO, format='%(asctime)s:%(levelname)s:%(message)s');

class RoboterController(Nano):
    B = TypeVar('B', bytearray, bytes);
    _MAX_SPEED= 30;
    _SPEED=20
    _MID_SPEED=10;
    _LOW_SPEED=5;
    _STOP=0;
    def __init__(self) -> None:
        super(RoboterController, self).__init__(); # Nano.__init__()
    def driveTroughATunnel(self)->bool:
        print('driving through a tunnel')
        while ((4<self.get_distances()[0]<10 and self.get_distances()[0]!=0) or (4<self.get_distances()[2] <10 and self.get_distances()[2]!=0)):
            if(self.get_distances()[1] > 6 and self.get_distances()[1]!=0):
                self.driveStraigthforward((20,20))
                self.ledsStart()
            else:
                return True # object in front closer than 5 cm
        return False # lateral object further than 6 cm
    def ledsStart(self)->None:
        init_leds()
        set_led(c.LED_MID, c.RED)
        set_led(c.LED_RIGHT, c.YELLOW)
        set_led(c.LED_LEFT, c.GREEN)
        set_led(c.LED_FRONT_LEFT, c.ON)
        set_led(c.LED_FRONT_RIGHT, c.ON)
    def ledsEnd(self)->None:
        set_led(c.LED_FRONT_LEFT, c.OFF)
        set_led(c.LED_FRONT_RIGHT, c.OFF)
    def driveStraigthforward(self, speed=None) -> None:
        if(speed is not None):
            assert (isinstance(speed, (list, tuple))), 'speed should be tuple or list'
            self.set_motors(speed[0],speed[1]);
            print('driving forwards')
        else:
            self.set_motors(self._SPEED, self._SPEED);
            print('driving forwards')

    def _stop(self) -> None:
        self.set_motors(self._STOP,self._STOP);
        print('stop')
    def _park(self)->None:
        self._stop()
        self.set_buzzer(3, 0)
    def _turnRightActions(self, flag) -> None:

        if (flag == 25):
            self.set_motors(self._MAX_SPEED, self._MID_SPEED);
            print('action -> OC-Right')
        elif (flag ==5):
            self.set_motors(self._MAX_SPEED, self._LOW_SPEED);
            print('action -> CC-Right');

    def _turnLeftActions(self,flag)->None:

        if (flag == 25):
            self.set_motors(self._MID_SPEED, self._MAX_SPEED);
            print('action -> OC-Left')
        elif (flag ==5):
            self.set_motors(self._LOW_SPEED, self._MAX_SPEED);
            print('action -> CC-Left');

    def _spinRight(self) -> None:
        self.set_motors(self._MAX_SPEED,self._STOP);
        print('spin right')

    def _spinLeft(self) -> None:
        self.set_motors(self._STOP, self._MAX_SPEED);
        print('spin left')

    @staticmethod
    def _convertIntToBool(limit, obstacle)->Tuple:
        cL = 3 <= obstacle[0] <= limit;  # clo -> 80-40 < x < 80
        cM = 3 <= obstacle[1] <= limit;
        cR = 3 <= obstacle[2] <= limit;
        return cL, cM, cR;

