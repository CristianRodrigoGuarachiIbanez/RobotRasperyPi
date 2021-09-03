# -*- coding: utf-8 -*-
import sys
from pibot.nano import Nano
from typing import List, Tuple, Dict, Callable, TypeVar, Any, Generator
from logging import info, INFO, DEBUG
from robotController import RoboterController
from pibot.leds import set_led, init_leds
from pibot import constants as c
from sys import exit
class DrivingRoboter(RoboterController):
    B = TypeVar('B', bytearray, bytes);
    _dist = None;
    _distance_limit= 20;
    def __init__(self) -> None:
        super(DrivingRoboter, self).__init__(); # Nano.__init__()
        self.limits = [25, 75]
    def mainLoop(self) -> None:
        obstacle = (0, 0, 0)
        tunnelLeft = None
        tunnelRight = None
        obstacleCloser = None
        init_leds()
        while(True):
            if(self.searchForBarricade() is True):
                self._stop();
                break;
            obstacle = self.get_distances()
            print(obstacle)
            # if all sensors are NOT detecting a obstacle, drive forward -> regardless the limit
            while(obstacle[0] < self.limits[0] and obstacle[1] < self.limits[0] and obstacle[2] < self.limits[0]):
                    self.driveStraigthforward();
            # if no tunnel, no obstacle on any of both sides closer than 20 cm AND
            # no obstacle in front side closer than 20cm
            while not ((self.get_distances()[0] <= self.limits[0] and self.get_distances()[0]!=0)or (self.get_distances()[2] <= self.limits[0] and self.get_distances()[2]!=0)):
                if (self.get_distances()[1] >= self.limits[0] and self.get_distances()[1]!=0):
                    #drive forward
                    self.driveStraigthforward();
                else:
                    # spin around
                    self._spinRight();
            # 1.- check if any obstacle in 20 cm
            if(self.anyHit(obstacle, self.limits[0])):
                # this will be activated if any obstacle at any side is closer than 20 cm
                # True if obstacles on both sides, but not in the middle
                print('obstacle is closer than 20 cm', self.get_distances())
                print(self.avoidCloseRightObstacle(self.limits[0]),"VS", self.avoidCloseLeftObstacle(self.limits[0]))
                while(self.avoidCloseLeftObstacle(self.limits[0]) or self.avoidCloseRightObstacle(self.limits[0])):
                    # drive forward as long as obstacle in the middle is further away from the limit
                    if(self.get_distances()[1] >= self.limits[0]):
                        self.driveTroughATunnel();
                        # break if the obstacles at both sides are gone
                        set_led(c.LED_MID, c.RED)
                        set_led(c.LED_RIGHT, c.YELLOW)
                        set_led(c.LED_LEFT, c.GREEN)
                        set_led(c.LED_FRONT_LEFT, c.ON)
                        set_led(c.LED_FRONT_RIGHT, c.ON)
                        if(self.get_distances()[0] > self.limits[0] or self.get_distances()[2] > self.limits[0]):
                            print('out of the tunnel');
                            set_led(c.LED_FRONT_LEFT,c.OFF)
                            set_led(c.LED_FRONT_RIGHT,c.OFF)
                            continue;
                    else:
                        # if the obstacle in the middle is closer than the limit than search for barricade
                        while(self.searchForBarricade()):
                            self._stop();
                            exit('the robot was successfully parked')
            else:
                while not (self.get_distances()[0] <= self.limits[1] or self.get_distances()[2] <= self.limits[1]):
                    if (self.get_distances()[1] >= self.limits[1]):
                        self.driveStraigthforward();
                    else:
                        break;
            # 2.- check if any obstacle is in 50 cm
            if(self.anyHit(obstacle, self.limits[1])):
                print('obstacle is closer than 50 cm', self.get_distances())
                print(self.avoidDistantLeftObstacle(self.limits[1]), 'VS', self.avoidDistantRightObstacle(self.limits[1]))
                while (self.avoidDistantLeftObstacle(self.limits[1]) or self.avoidDistantRightObstacle(self.limits[1])):
                    if not(self.get_distances()[1]<=self.limits[1] and self.get_distances()[1]!=0):
                        print('drive slowly forward')
                        self.driveStraigthforward(15);
                    while(self.avoidCloseLeftObstacle(self.limits[0]) or self.avoidCloseRightObstacle(self.limits[0])):
                        # drive forward as long as obstacle in the middle is further away from the limit
                        if(self.get_distances()[1] >= 20):
                            self.driveTroughATunnel();
                            set_led(c.LED_MID, c.RED)
                            set_led(c.LED_RIGHT, c.YELLOW)
                            set_led(c.LED_LEFT,c.GREEN)
                            set_led(c.LED_FRONT_LEFT, c.ON)
                            set_led(c.LED_FRONT_RIGHT, c.ON)
                            if (self.get_distances()[0] > 20 or self.get_distances()[2] >20):
                                print('out of the tunnel');
                                set_led(c.LED_FRONT_LEFT, c.OFF)
                                set_led(c.LED_FRONT_RIGHT, c.OFF)
                                continue;
                        else:
                            # if the obstacle is closer than 20 cm search for barricade
                            if(self.searchForBarricade()):
                                self._stop();
                                exit('the robot was parked');
            else:
                while not (self.get_distances()[0] <= 100 or self.get_distances()[2] <= 100):
                    if (self.get_distances()[1] >= 100):
                        self.driveStraigthforward();
                    else:
                        break;

    def anyHit(self, obstacle:Tuple[int,int,int], limit:int)->bool:
        print('ANY HIT:{}'.format(any([obstacle[0]<=limit and obstacle[0]!=0,
                                       obstacle[1]<=limit and obstacle[1]!=0,
                                       obstacle[2]<=limit and obstacle[2]!=0])))
        return any([obstacle[0]<=limit and obstacle[0]!=0,
                    obstacle[1]<=limit and obstacle[1]!=0,
                    obstacle[2]<=limit and obstacle[2]!=0])

    def searchForBarricade(self)->bool:
        distance = self._convertIntToBool(self.limits[0],self.get_distances())
        if(distance[0] and distance[1] and distance[2]):
            return True
        return False

    def avoidDistantLeftObstacle(self, limit) -> bool:
            # as long as the first criteria is met, than it'll turn a bit to the right.
            while (self.get_distances()[0] <= limit and self.get_distances()[0]!=0):
                # and nothing on the right side
                if not (self.get_distances()[2] <= limit and self.get_distances()[2]!=0):
                    self._turnRightActions(limit);
                # it stops to turning to the left if any obstacle is closer than 50 cm
                if(any([self.get_distances()[2] <= self.limits[1] and self.get_distances()[2]!=0, self.get_distances()[1] <= self.limits[1] and self.get_distances()[1] !=0])):
                    print('obstacle gets closer than 50 cm!')
                    return True;
            return False
    def avoidDistantRightObstacle(self, limit)->bool:

            while (self.get_distances()[2] <= limit and self.get_distances()[2]!=0):
                if not (self.get_distances()[0] <= limit and self.get_distances()[0]!=0):
                    self._turnLeftActions(limit);
                if(any([self.get_distances()[0] <= self.limits[1] and self.get_distances()[0]!=0, self.get_distances()[1] <= self.limits[1] and self.get_distances()[1]!=0])):
                    print('obstacle gets closer than 50 cm!')
                    return True;
            return False
    def avoidCloseLeftObstacle(self, limit)->bool:
            while((self.get_distances()[0] <= limit) and (self.get_distances()[0]!=0)):
                if not (self.get_distances()[2] <= limit and self.get_distances()[2]!=0):
                    self._turnRightActions(limit);
                if (self.get_distances()[2]<=limit and self.get_distances()[2]!=0):
                    print('TUNNEL IN FRONT')
                    return True
                # elif((get_distances[1] >= self.limits[1]*2 and get_distances[1]!=0)
                #      and (get_distances[2] >= self.limits[1]*2 and get_distances[2]!=0)):
                return False;
    def avoidCloseRightObstacle(self,limit)->bool:
            while ((self.get_distances()[2] <= limit) and (self.get_distances()[2]!=0)):
                if not (self.get_distances()[0] <= limit and self.get_distances()[0]!=0):
                    self._turnLeftActions(limit);
                if (self.get_distances()[0] <= limit and self.get_distances()[0]!=0):
                    print('TUNNEL IN FRONT')
                    return True
                # elif (((self.get_distances()[0] >= self.limits[1]*2) and (self.get_distances()[0]!=0))
                #       and ((self.get_distances()[1] >= self.limits[1]*2) and (self.get_distances()[1]!=0))):
                return False;

def main():

    robot = DrivingRoboter()
    robot.mainLoop()
    print("outside the main loop")

if __name__ == "__main__":
    main()
