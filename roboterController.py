# -*- coding: utf-8 -*-

import sys
from pibot.nano import Nano
from typing import List, Tuple, Dict, Callable, TypeVar, Any
from logging import info, INFO, DEBUG
from time import sleep
import logging
logging.basicConfig(filename='debugging.log' ,level=INFO, format='%(asctime)s:%(levelname)s:%(message)s');


class RoboterController(Nano):
    B = TypeVar('B', bytearray, bytes);
    _MAX_SPEED:int= 30;
    _SPEED:int=20
    _MID_SPEED:int=15;
    _LOW_SPEED:int=20;
    _STOP:int=0;
    def __init__(self) -> None:
        super(RoboterController, self).__init__(); # Nano.__init__()

    def driveTroughATunnel(self)->None:
        self.driveStraigthforward(20)

    def driveStraigthforward(self, speed:int=None) -> None:
        if(speed is not None):
            self.set_motors(speed,speed);
        else:
            self.set_motors(self._SPEED, self._SPEED);

    def _stop(self) -> None:
        self.set_motors(self._STOP,self._STOP);

    def _turnRightActions(self, flag: int) -> None:
        if (flag == 75):
            self.set_motors(self._MAX_SPEED, self._SPEED);
            print('action -> OC-Right')
        elif (flag == 50):
            self.set_motors(self._SPEED, self._LOW_SPEED);
            print('action -> OC-Right')
        elif (flag ==25):
            self.set_motors(self._MID_SPEED, self._STOP);
            print('action -> CC-Right');

    def _turnLeftActions(self,flag:int) ->None:
        if (flag == 75):
            self.set_motors(self._SPEED, self._MAX_SPEED);
            print('action -> OC-Left')
        elif (flag == 50):
            self.set_motors(self._LOW_SPEED, self._SPEED);
            print('action -> OC-Left')
        elif (flag ==25):
            self.set_motors(self._STOP, self._MID_SPEED);
            print('action -> CC-Left');

    def _driveForward(self, flag:int) -> None:
        if(flag==75):
            self.set_motors(self._MAX_SPEED, self._MAX_SPEED);
            print('action -> forward');
        elif(flag==50):
            self.set_motors(self._SPEED, self._SPEED);
            print('action -> forward unaccelerated ')
        elif(flag==25):
            self.set_motors(self._STOP,self._STOP);
            print('action -> stop');
    def _spinRight(self) -> None:
        self.set_motors(self._MAX_SPEED,self._STOP);
    def _spinLeft(self) -> None:
        self.set_motors(self._STOP, self._MAX_SPEED);
    @staticmethod
    def _convertIntToBool(limit:int, obstacle:Tuple[int,int,int])-> Tuple[bool, bool, bool]:
        cL = limit - 20 <= obstacle[0] <= limit;  # clo -> 80-40 < x < 80
        cM = limit - 20 <= obstacle[1] <= limit;
        cR = limit - 20 <= obstacle[2] <= limit;
        return cL, cM, cR;

class DistanceHandler:
    def __init__(self, obstacle) ->None:
        self.left=obstacle[0];
        self.mid=obstacle[1];
        self.right=obstacle[2];

    def _convertDistanceToBoolean(self, limit) -> Tuple[bool, bool, bool]:
        cL = limit-20<= self.left <= limit;  # clo -> 80-40 < x < 80
        cM = limit-20<= self.mid <= limit;
        cR = limit-20<= self.right <= limit;
        return cL,cM,cR;
