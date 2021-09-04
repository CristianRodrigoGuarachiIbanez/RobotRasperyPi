# -*- coding: utf-8 -*-
import sys
from pibot.nano import Nano
from typing import List, Tuple, Dict, Callable, TypeVar, Any
from logging import info, INFO, DEBUG
import logging
logging.basicConfig(filename='debugging.log' ,level=INFO, format='%(asctime)s:%(levelname)s:%(message)s');

class RoboterController(Nano):
    B = TypeVar('B', bytearray, bytes);
    _MAX_SPEED= 30;
    _SPEED=20
    _MID_SPEED=15;
    _LOW_SPEED=7;
    _STOP=0;
    def __init__(self) -> None:
        super(RoboterController, self).__init__(); # Nano.__init__()



    def driveTroughATunnel(self)->None:
        print('driving through a tunnel')
        self.driveStraigthforward(20)

    def driveStraigthforward(self, speed=None) -> None:
        assert(isinstance(speed,(list,tuple))), 'speed should be tuple or list'
        if(speed is not None):
            self.set_motors(speed[0],speed[1]);
            print('driving forwards')
        else:
            self.set_motors(self._SPEED, self._SPEED);
            print('driving forwards')

    def _stop(self) -> None:
        self.set_motors(self._STOP,self._STOP);
        self.set_buzzer(3, 0)
        print('stop')

    def _turnRightActions(self, flag) -> None:

        if (flag == 75):
            self.set_motors(self._MAX_SPEED, self._MID_SPEED);
            print('action -> OC-Right')
        elif (flag ==25):
            self.set_motors(self._SPEED, self._LOW_SPEED);
            print('action -> CC-Right');

    def _turnLeftActions(self,flag)->None:

        if (flag == 75):
            self.set_motors(self._MID_SPEED, self._MAX_SPEED);
            print('action -> OC-Left')
        elif (flag ==25):
            self.set_motors(self._LOW_SPEED, self._SPEED);
            print('action -> CC-Left');

    def _spinRight(self) -> None:
        self.set_motors(self._MAX_SPEED,self._STOP);
        print('spin right')

    def _spinLeft(self) -> None:
        self.set_motors(self._STOP, self._MAX_SPEED);
        print('spin left')

    @staticmethod
    def _convertIntToBool(limit, obstacle)->Tuple:
        cL = limit - 17 <= obstacle[0] <= limit;  # clo -> 80-40 < x < 80
        cM = limit - 17 <= obstacle[1] <= limit;
        cR = limit - 17 <= obstacle[2] <= limit;
        return cL, cM, cR;

