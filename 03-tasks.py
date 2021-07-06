# -*- coding: utf-8 -*-
import sys
from pibot.nano import Nano
from typing import List, Tuple, Dict, Callable, TypeVar, Any
from logging import info, INFO, DEBUG
import logging
logging.basicConfig(filename='debugging.log' ,level=INFO, format='%(asctime)s:%(levelname)s:%(message)s');
#logging.getLogger().setLevel(INFO)

from sys import exit


class Roboter(Nano):
    B = TypeVar('B', bytearray, bytes);
    _dist =  None;
    _distance_limit:int = 20;
    def __init__(self) -> None:
        super(Roboter, self).__init__(); # Nano.__init__()
        self._dist: Tuple[int]

    def driveForward(self,  setLimit:int = 10000) -> None:
        """
        main loop
        :return: None
        """

        obstacle_in_front:bool = False;
        conditions:bool = False;
        free_direction:str = " ";
        self._dist = self.get_distances()
        i = 0
        while (True): # 20 Test zahl

            if(self._drive_through_tunnel()):
                print('if -> driving through a Tunnel')
            elif(self._drive_along_wall() == 'Left'):
                free_direction = 'Right';
            elif(self._drive_along_wall() == 'Right'):
                free_direction = 'Left';

            try:
                obstacle_in_front = self._drive_until_obstacle()
            except Exception as e:
                info('[Exception]: {}'.format(e))

            while(obstacle_in_front):
                self._dist = self.get_distances();  # left, mid, right
                info('free direction: {}'.format(free_direction))
                self._turning(free_direction)
                if not (self._drive_until_obstacle()):
                    obstacle_in_front = False;

            info('OUTER LOOP: index: {}, value: {}'.format(i, self._dist));
            self._dist = self.get_distances();
            i += 1

            if(setLimit == i):
                break;

    @staticmethod
    def _check_distance(distance_limit, dist: Tuple[int, int, int]) -> Tuple[bool, bool, bool]:
        conditionLeft = 0 <= dist[0] <= distance_limit;  # True, True - mid>0 and mid <40
        conditionMid = 0 <= dist[1] <= distance_limit;
        conditionRight = 0 <= dist[2] <= distance_limit;
        return conditionLeft, conditionMid, conditionRight

    @staticmethod
    def _check_closest_one(value1:int, value2:int ) -> str:
        if(value1 > value2):
            return 'Left'
        elif(value1 < value2):
            return 'Right'
        else:
            return 'Right'

    def _drive_until_obstacle(self) -> bool:
        """
        check for the distance values
        :return: None
        """
        conditions: Tuple[bool, bool, bool] = self._check_distance(self._distance_limit, self._dist)
        if(conditions[1] is True):
            self.set_motors(0,0);
            print('elif -> obstacle in front');
            return True
        elif(conditions[1] is False):
            self.set_motors(30,30);
            return False

    def _drive_through_tunnel(self) -> bool:
        conditions: Tuple[bool, bool, bool] = self._check_distance(self._distance_limit, self._dist)
        if (conditions[0] and not conditions[1] and  conditions[2]):  # 0-20 ->
            return True;

    def _drive_along_wall(self) -> str:
        conditions: Tuple[bool, bool, bool] = self._check_distance(self._distance_limit, self._dist)
        if(conditions[0] is True and conditions[2] is False):
            return 'Right';
        elif(conditions[0] is False and conditions[2] is True):
            return 'Left';
        elif(conditions[0] is False and conditions[2] is False):
            return self._check_closest_one(self._dist[0], self._dist[2]);

    def _turning(self, direction_to_turn: str) -> None:
        """
        call the turning right and turning left
        :param right: boolen value True or False
        :param left: boolen value True or False
        :return: None
        """
        if(direction_to_turn == 'Right'):
            self.__turningRight()
            print('turned right')
        elif(direction_to_turn == 'Left'):
            self.__turningLeft()
            print('turned left')

    def __turningRight(self) -> None:
        '''
        check for the values of getDistance() and pass a integer value to the function set_motors()
        :return: None
        '''

        self.set_motors(-30,30)

    def __turningLeft(self) -> None:
        '''
       check for the values of getDistance() and pass a integer value to the function set_motors()
       :return: None
       '''

        self.set_motors(30, -30)

def main():
    #nano.set_motors(0, 0)
    #nano.reset_encoders()

    #drive_until_obstacle()  # you should comment this line
    # drive_along_wall()    # and uncomment this line in order to run the
                            # drive_along_wall() function
    robot = Roboter()
    robot.driveForward()
    print("outside the main loop")

if __name__ == "__main__":
     #nano = Nano()
    main()
