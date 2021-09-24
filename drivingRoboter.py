# -*- coding: utf-8 -*-
import sys
from pibot.nano import Nano
from typing import List, Tuple, Dict, Callable, TypeVar, Any, Generator
from logging import info, INFO, DEBUG, basicConfig
from robotController import RoboterController
from pibot import constants as c
from pibot.buttons import wait_for_any, wait_for_button_press, init_buttons
from sys import exit
from time import sleep
basicConfig(filename='debugging.log' ,level=INFO, format='%(asctime)s:%(levelname)s:%(message)s');
init_buttons()
class DrivingRoboter(RoboterController):
    B = TypeVar('B', bytearray, bytes);
    _dist = None;
    _distance_limit= 20;
    def __init__(self) -> None:
        super(DrivingRoboter, self).__init__(); # Nano.__init__()
        self.limits = [10, 20]
    def mainLoop(self) -> None:
        print('press left button to continue :)')
        wait_for_button_press(c.BUTTON_LEFT)
        while(True):
            if(self.searchForBarricade() is True):
                self._stop();
                break;
            print(self.get_distances())
            # 1.- check if any obstacle in 5 cm
            if(any(self.anyHit(self.get_distances(), self.limits[0]))): # any Ob closer than 5 cm
                #left=
                if((self.get_distances()[0] <= self.limits[0]) and (self.get_distances()[0]!=0)): # if Ob left <= 5
                    #left = self.get_distances()
                    while((self.get_distances()[0] <= self.limits[0]) and (self.get_distances()[0]!=0)):
                        self._spinRight()
                        print(self.get_distances()[0])
                    #left = self.avoidCloseLeftObstacle(self.limits[0])
                    #if not (left): #True: Ob right < 5
                        # active, if obstacle left further than 5 cm or obstacle in front closer than 5 cm
                    #     pass
                    # else: # active if obstacles on both sides, but not in the middle
                    #     self._stop()
                    #     if (self.driveTroughATunnel()):  # True: Ob Mid < 5, False: Ob laterals > 5 or < 2
                    #         self._stop()
                    #         if (self.searchForBarricade()):
                    #             self.ledsEnd()
                    #             self._park();
                    #             exit('the robot was successfully parked')
                    #         else:
                    #             self._stop()
                    #             self.ledsEnd()
                    #             continue
                    #     else:
                    #         self._stop()
                    #         pass
                    self._stop()
                # right = self.get_distances()
                if((self.get_distances()[2] <= self.limits[0]) and (self.get_distances()[2]!=0)): # obstacle_distance <= 5
                    #right =
                    while((self.get_distances()[2] <= self.limits[0]) and (self.get_distances()[2]!=0)):
                        #self._spinLeft()
                        self.set_motors(0, 30)
                        print(self.get_distances()[2])
                    # check, if no object right or object in front
                    # right = self.avoidCloseRightObstacle(self.limits[0])
                    # if not (right): # False: Ob right > 5 or Ob Mid < 5,
                    #     self._stop()
                    #     pass
                    # # check if obstacle left closer < 5 cm
                    # else: # True: Ob left < 5
                    #     self._stop()
                    #     # check if obstacle in front < 6 cm
                    #     if(self.driveTroughATunnel()): #True: Ob Mid < 5, False: Ob laterals > 5 cm or < 2
                    #         self._stop()
                    #         if (self.searchForBarricade()): # True: Ob all over < 2-5
                    #             self.ledsEnd()
                    #             self._park()
                    #             exit('the robot was successfully parked')
                    #         else: # obstacles out of relevant range
                    #             self._stop()
                    #             self.ledsEnd()
                    #             continue
                    #     # check if obstacle is out of range 4-10
                    #     else:
                    #         self._stop()
                    #         pass
                    self._stop()
                while not ((self.get_distances()[0] <= self.limits[0] and self.get_distances()[0]!=0) or (self.get_distances()[2] <= self.limits[0] and self.get_distances()[2]!=0)):
                    # drive forward as long as obstacle in the middle is further away from the limit
                    if(self.get_distances()[1] <= 30 and self.get_distances()[1]!=0):
                        if (self.get_distances()[0] <= self.limits[0] and self.get_distances()[0]!=0):
                            self._spinRight()
                            sleep(1)
                        else:
                            self._spinLeft()
                            sleep(1)
                    else:
                        self.driveStraigthforward((30,30))
                        # break if the obstacles at both sides are gone
                    if ((self.get_distances()[0] <= self.limits[0]-5 and self.get_distances()[0]!=0) and (self.get_distances()[2]-5 <= self.limits[0] and self.get_distances()[2]!=0)):
                        break
                self._stop()
                while((self.get_distances()[0] <= self.limits[0]-5 and self.get_distances()[0]!=0) and (self.get_distances()[2]-5 <= self.limits[0] and self.get_distances()[2]!=0)):
                    if (self.get_distances()[1] <= 30 and self.get_distances()[1] != 0):
                        self.driveTroughATunnel()
                        self.ledsEnd()
                    else: # barricade?
                        if not (self.get_distances()[0]<3 and self.get_distances()[0]!=0):
                            self._turnLeftActions((-3,10))
                        if not (self.get_distances()[0] < 3 and self.get_distances()[0] != 0):
                            self._turnRightActions(((10,-3)))
                        continue
            elif(all(self.anyHit(self.get_distances(), self.limits[0]))):
                # if all sensors are NOT detecting a obstacle, drive forward -> regardless the limit
                self._park()
            else:
                # while not (self.get_distances()[0] <= self.limits[1] or self.get_distances()[2] <= self.limits[1]):
                #     if (self.get_distances()[1] >= self.limits[1]):
                #         self.driveStraigthforward();
                #     else:
                #         break;
                pass

    def anyHit(self, obstacle:Tuple[int,int,int], limit:int)->List[bool]:
        print('ANY HIT:{}'.format(any([obstacle[0]<=limit and obstacle[0]!=0,
                                       obstacle[1]<=limit and obstacle[1]!=0,
                                       obstacle[2]<=limit and obstacle[2]!=0])))
        return [obstacle[0]<=limit and obstacle[0]!=0,
                    obstacle[1]<=limit and obstacle[1]!=0,
                    obstacle[2]<=limit and obstacle[2]!=0]

    def searchForBarricade(self)->bool:
        '''
        check if a obstacle in range of 2-6 cm
        :return: a boolean value if all sensors detect obstacles
        '''
        distance = self._convertIntToBool(self.limits[0]+1,self.get_distances())
        if(distance[0] and distance[1] and distance[2]):
            return True
        return False

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
            elif(50<counter<55):
                self.set_motors(0, 0)
                self.reset_encoders()
                print('reset -> value:{}'.format(self.get_encoders()))
            elif(55<counter<100):
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
    robot.mainLoop()
    #robot.driveAlongtheWall()
    #robot.test()
    print("outside the main loop")

if __name__ == "__main__":
    main()
