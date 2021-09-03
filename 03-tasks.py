# -*- coding: utf-8 -*-
import sys
from pibot.nano import Nano
from typing import List, Tuple, Dict, Callable, TypeVar, Any, Generator
from logging import info, INFO, DEBUG
from robotController import RoboterController
from time import sleep
import logging
from abc import ABCMeta
logging.basicConfig(filename='debugging.log' ,level=INFO, format='%(asctime)s:%(levelname)s:%(message)s');
#logging.getLogger().setLevel(INFO)
from sys import exit
class Roboter(RoboterController):
    B = TypeVar('B', bytearray, bytes);
    _dist = None;
    _distance_limit:int = 20;
    def __init__(self) -> None:
        super(Roboter, self).__init__(); # Nano.__init__()
        self.limits:List[int] = [20,50]
    def mainLoop(self) -> None:
        obstacle:Tuple[int,int,int];
        tunnelLeft: Generator;
        tunnelRight:Generator;
        obstacleCloser:Generator[bool];
        while(True):
            if(self.searchForBarricade() is True):
                self._stop();
                break;
            obstacle = self.get_distances()
            try:
                # if all sensors are NOT detecting a obstacle, drive forward -> regardless the limit
                while(obstacle[0] < self.limits[0] and obstacle[1] < self.limits[0] and obstacle[2] < self.limits[0]):
                        self.driveStraigthforward();

                # if no tunnel, no obstacle on any of both sides closer than 20 cm AND
                # no obstacle in front side closer than 20cm
                while not (self.get_distances()[0] <= self.limits[0] or self.get_distances()[2] <= self.limits[0]):
                    if (self.get_distances()[1] >= self.limits[0]):
                        #drive forward
                        self.driveStraigthforward();
                    else:
                        # spin around
                        self._spinRight()

                # 1.- check if any obstacle in 20 cm
                if(self.anyHit(obstacle, self.limits[0])):
                    # this will be activated if any obstacle at any side is closer than 20 cm
                    # True if obstacles on both sides, but not in the middle
                    tunnelLeft = self.avoidCloseLeftObstacles(self.limits[0]);
                    tunnelRight = self.avoidCloseRightObstacle(self.limits[0])
                    while(next(tunnelLeft) or next(tunnelRight)):
                        # drive forward as long as obstacle in the middle is further away from the limit
                        if(self.get_distances()[1] >= self.limits[0]):
                            self.driveTroughATunnel();
                            # braak if the obstacles at both sides are gone
                            if(self.get_distances()[0] > self.limits[0] or self.get_distances()[2] > self.limits[0]):
                                print('out of the tunnel');
                                break;
                        else:
                            # if the obstacle in the middle is closer than the limit than search for barricade
                            while(self.searchForBarricade()):
                                self._spinRight();
                                # turn around till it finds a free direction (parking)
                                if not (any([self.get_distances()[2] <= 20, self.get_distances()[1] <= 20, self.get_distances()[0]<=20])):
                                    self._stop()
                                    exit('the robot was successfully parked')
                # 2.- check if any obstacle is in 50 cm
                elif(self.anyHit(obstacle, self.limits[1])):
                    obstacleLeft = self.avoidDistantLeftObstacle(self.limits[1]);
                    obstacleRight = self.avoidDistantRightObstacle(self.limits[1]);
                    while (next(obstacleLeft) or next(obstacleRight)):
                        tunnelLeft = self.avoidCloseLeftObstacles(20);
                        tunnelRight = self.avoidCloseRightObstacle(20);
                        while(next(tunnelRight) or next(tunnelLeft)):
                            # drive forward as long as obstacle in the middle is further away from the limit
                            if(self.get_distances()[1] >= 20):
                                self.driveTroughATunnel();
                                if (self.get_distances()[0] > 20 or self.get_distances()[2] >20):
                                    print('out of the tunnel');
                                    break;
                            else:
                                # if the obstacle is closer than 20 cm search for barricade
                                while (self.searchForBarricade()):
                                    self._spinRight()
                                    if not(any([self.get_distances()[2] <= 20, self.get_distances()[1] <= 20, self.get_distances()[0]<=20])):
                                        self._stop();
                                        exit('the robot was parked');
                    else:
                        while not (self.get_distances()[0] <= 20 or self.get_distances()[2] <= 20):
                            if (self.get_distances()[1] >= 20):
                                self.driveStraigthforward();
                            else:
                                self._spinLeft()
                # 3.-
            except Exception as e:
                print('[Exception Main Loop]: {}'.format(e));

    def anyHit(self, obstacle:Tuple[int,int,int], limit:int)->bool:
        return any([obstacle[0]<=limit,obstacle[1]<=limit,obstacle[2]<=limit])

    def searchForBarricade(self)->bool:
        distance:Tuple[bool, bool, bool] = self._convertIntToBool(self.limits[0],self.get_distances())
        if(distance[0] and distance[1] and distance[2]):
            return True
        return False

    def avoidDistantLeftObstacle(self, limit: int) -> Generator[bool]:
            # as long as the first criteria is met, than it'll turn a bit to the right.
            while (self.get_distances()[0] <= limit):
                # and nothing on the right side
                if not (self.get_distances()[2] <= limit):
                    self._turnRightActions(limit);
                # it stops to turning to the left if any obstacle is closer than 50 cm
                if(any([self.get_distances()[2] <= 25, self.get_distances()[1] <= 25])):
                    print('obstacle gets closer than 50 cm!')
                    yield True;
            yield False
    def avoidDistantRightObstacle(self, limit:int)->Generator[bool]:

            while (self.get_distances()[2] <= limit):
                if not (self.get_distances()[0] <= limit):
                    self._turnLeftActions(limit);
                if(any([self.get_distances()[0] <= 25, self.get_distances()[2] <= 25])):
                    print('obstacle gets closer than 50 cm!')
                    yield True;
            yield False

    def avoidCloseLeftObstacles(self, limit: int) -> Generator[bool]:
            while((self.get_distances()[0] <= limit)):
                if not (self.get_distances()[2] <= limit):
                    self._turnRightActions(limit);
                if (self.get_distances()[2]<=limit):
                    print('TUNNEL IN FRONT')
                    yield True
                elif(self.get_distances()[1] >= limit and self.get_distances()[2] >= limit):
                    yield False;
            return False
    def avoidCloseRightObstacle(self,limit:int)->Generator:
            while ((self.get_distances()[2] <= limit)):
                if not (self.get_distances()[0] <= limit):
                    self._turnLeftActions(limit);
                if (self.get_distances()[0] <= limit):
                    print('TUNNEL IN FRONT')
                    yield True
                elif (self.get_distances()[0] >= limit and self.get_distances()[1] >= limit):
                    return False;
            return False



def main():

    robot = Roboter()
    robot.mainLoop()
    print("outside the main loop")

if __name__ == "__main__":
    main()
