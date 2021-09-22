# -*- coding: utf-8 -*-
import sys
from pibot.nano import Nano
from typing import List, Tuple, Dict, Callable, TypeVar, Any, Generator
from logging import info, INFO, DEBUG, basicConfig
from robotController import RoboterController
from pibot.leds import set_led, init_leds

from sys import exit
from time import sleep
basicConfig(filename='debugging.log' ,level=INFO, format='%(asctime)s:%(levelname)s:%(message)s');
class DrivingRoboter(RoboterController):
    B = TypeVar('B', bytearray, bytes);
    _dist = None;
    _distance_limit= 20;
    def __init__(self) -> None:
        super(DrivingRoboter, self).__init__(); # Nano.__init__()
        self.limits = [5, 20]
    def mainLoop(self) -> None:
        obstacle = (0, 0, 0)
        tunnelLeft = None
        tunnelRight = None
        obstacleCloser = None

        while(True):
            if(self.searchForBarricade() is True):
                self._stop();
                break;
            obstacle = self.get_distances()
            print(obstacle)

            # 1.- check if any obstacle in 5 cm
            if(any(self.anyHit(obstacle, self.limits[0]))): # any Ob closer than 5 cm
                # True if obstacles on both sides, but not in the middle
                if(self.anyHit(self.get_distances(),self.limits[0])[0]): # if Ob left <= 5
                    if not (self.avoidCloseLeftObstacle(self.limits[0])): #True: Ob right < 5
                        self._stop()
                        pass
                    else:
                        self._stop()
                        if (self.driveTroughATunnel()):  # True: Ob Mid < 5, False: Ob laterals > 5 or < 2
                            self._stop()
                            if (self.searchForBarricade()):
                                self.ledsEnd()
                                self._park();
                                exit('the robot was successfully parked')
                            else:
                                self._stop()
                                self.ledsEnd()
                                continue
                        else:
                            self._stop()
                            pass
                if(self.anyHit(self.get_distances(),self.limits[0])[2]): # obstacle_distance <= 5
                    # check, if none object right or object in front
                    if not (self.avoidCloseRightObstacle(self.limits[0])): # False: Ob right > 5 or Ob Mid < 5,
                        self._stop()
                        pass
                    # check if obstacle left closer < 5 cm
                    else: # True: Ob left < 5
                        self._stop()
                        # check if obstacle in front < 6 cm
                        if(self.driveTroughATunnel()): #True: Ob Mid < 5, False: Ob laterals > 5 cm or < 2
                            self._stop()
                            if (self.searchForBarricade()): # True: Ob all over < 2-5
                                self.ledsEnd()
                                self._park()
                                exit('the robot was successfully parked')
                            else: # obstacles out of relevant range
                                self._stop()
                                self.ledsEnd()
                                continue
                        # check if obstacle is out of range 4-10
                        else:
                            self._stop()
                            pass
                while not (self.anyHit(self.get_distances(),self.limits[0])[0] or self.anyHit(self.get_distances(),self.limits[0])[2]):
                    # drive forward as long as obstacle in the middle is further away from the limit
                    if(self.get_distances()[1] <= 5 and self.get_distances()[1]!=0):
                        self._spinRight()
                        sleep(1)
                    else:
                        self.driveStraigthforward((30,30))
                        # break if the obstacles at both sides are gone
                self._stop()
            elif(all(self.anyHit(self.get_distances(), self.limits[0]))):
                # if all sensors are NOT detecting a obstacle, drive forward -> regardless the limit
                self._park()
            else:
                while not (self.get_distances()[0] <= self.limits[1] or self.get_distances()[2] <= self.limits[1]):
                    if (self.get_distances()[1] >= self.limits[1]):
                        self.driveStraigthforward();
                    else:
                        break;

    def anyHit(self, obstacle:Tuple[int,int,int], limit:int)->List[bool]:
        print('ANY HIT:{}'.format(any([obstacle[0]<=limit and obstacle[0]!=0,
                                       obstacle[1]<=limit and obstacle[1]!=0,
                                       obstacle[2]<=limit and obstacle[2]!=0])))
        return [obstacle[0]<=limit and obstacle[0]!=0,
                    obstacle[1]<=limit and obstacle[1]!=0,
                    obstacle[2]<=limit and obstacle[2]!=0]

    def searchForBarricade(self)->bool:
        '''
        check if the distance values in range of 3-6
        '''
        distance = self._convertIntToBool(self.limits[0]+1,self.get_distances())
        if(distance[0] and distance[1] and distance[2]):
            return True
        return False

    def avoidDistantLeftObstacle(self, limit) -> bool:
            # as long as the first criteria is met, than it'll turn a bit to the right.
            while (self.get_distances()[0] <= limit and self.get_distances()[0]!=0):
                # and nothing on the right side
                if not (self.get_distances()[2] <= limit and self.get_distances()[2]!=0):
                    self._turnRightActions(limit)
                else:
                    return True;
                if(self.get_distances()[1]<=limit and self.get_distances()[1]!=0):
                    return False
            return False
    def avoidDistantRightObstacle(self, limit)->bool:
            while (self.get_distances()[2] <= limit and self.get_distances()[2]!=0):
                if not (self.get_distances()[0] <= limit and self.get_distances()[0]!=0):
                    self._turnLeftActions(limit);
                else:
                    return True;
                if (self.get_distances()[1] <= limit and self.get_distances()[1] != 0):
                    return False
            return False
    def avoidCloseLeftObstacle(self, limit)->bool:
            while((self.get_distances()[0] <= limit) and (self.get_distances()[0]!=0)):
                if (self.get_distances()[2] <= limit and self.get_distances()[2]!=0):
                    self._turnRightActions(limit);
                else:
                    print('TUNNEL IN FRONT')
                    return True
                if (self.get_distances()[1] <= limit and self.get_distances()[1] != 0):
                    return False
            return False;
    def avoidCloseRightObstacle(self,limit)->bool:

            while ((self.get_distances()[2] <= limit) and (self.get_distances()[2]!=0)):
                if (self.get_distances()[0] <= limit and self.get_distances()[0]!=0):
                    self._turnLeftActions(limit);
                else:
                    print('TUNNEL IN FRONT')
                    return True
                if (self.get_distances()[1] <= limit and self.get_distances()[1] != 0):
                    return False
            return False;
    def regulateWheelRotation(self)->None:
             if (self.get_encoders()[0] > self.get_encoders()[1]):
                 self.driveStraigthforward((0, 20))
             elif (self.get_encoders()[0] < self.get_encoders()[1]):
                 self.driveStraigthforward((20, 0))
             else:
                 self.driveStraigthforward((20, 20));

    def driveAlongtheWall(self) -> None:
        print('driving along wall')
        while not (self.get_distances()[2] <= 5 and self.get_distances()[2]!=0):
             if (self.get_distances()[1] > 20):
                 info('no obstacles {}'.format(self.get_encoders()))
                 #self.driveStraigthforward();
                 if(self.get_encoders()[0] > self.get_encoders()[1]):
                    self.driveStraigthforward((0,20))#
                    info('rotate right {}'.format(self.get_encoders()))
                 elif(self.get_encoders()[0]<self.get_encoders()[1]):
                    self.driveStraigthforward((20,0))
                    info('rotate left {}'.format(self.get_encoders()))
                 else:
                     #self.driveStraigthforward((20,20));
                    pass
                 info('after adjustment of the wheel rotation: {}'.format(self.get_encoders()))
             else:
                 self._stop()
    def test(self)->None:
        counter=0;
        while(True):
            print('index: {}, value:{}'.format(counter, self.get_encoders()))
            if(10<counter<50):
                self.set_motors(40,0)
                print('left rotation -> value:{}'.format(self.get_encoders()))
            elif(50<counter<100):
                self.set_motors(0,40)
                print('right rotation -> value:{}'.format(self.get_encoders()))
            else:
                pass
            counter+=1
            print('index: {}, value:{}'.format(counter, self.get_encoders()))
            if(counter>100):
                break



def main():

    robot = DrivingRoboter()
    #robot.mainLoop()
    #robot.driveAlongtheWall()
    robot.test()
    print("outside the main loop")

if __name__ == "__main__":
    main()
