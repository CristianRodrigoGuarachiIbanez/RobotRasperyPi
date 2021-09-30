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
        count = 0;
        while(True):
            if(self.searchForBarricade() is True):
                self._park();
            print(self.get_distances())
            # 1.- check if any obstacle in 5 cm
            if(any(self.anyHit(self.get_distances(), self.limits[0]))): # any Ob closer than 5 cm
                if((self.get_distances()[0] <= self.limits[0]) and (self.get_distances()[0]!=0)): # if Ob left <= 5
                    count += 1
                    while((self.get_distances()[0] <= self.limits[0]) and (self.get_distances()[0]!=0)):
                        self._spinRight()
                        print("turning right",self.get_distances())
                        if(self.searchForBarricade() is True):
                            self._park()
                    self._stop()
                if((self.get_distances()[2] <= self.limits[0]) and (self.get_distances()[2]!=0)): # obstacle_distance <= 5cm
                    count += 1
                    while((self.get_distances()[2] <= self.limits[0]) and (self.get_distances()[2]!=0)):
                        self._spinLeft()
                        print("turning left",self.get_distances())
                        if (self.searchForBarricade() is True):
                            self._park()
                    self._stop()
                while not ((self.get_distances()[0] <= self.limits[0] and self.get_distances()[0]!=0) or (self.get_distances()[2] <= self.limits[0] and self.get_distances()[2]!=0)):
                    # drive forward as long as obstacle in the middle is further away from the limit
                    if(self.get_distances()[1] <= 25 and self.get_distances()[1]!=0):
                        if (self.get_distances()[0] <= self.limits[0] and self.get_distances()[0]!=0):
                            self._spinRight()
                            count+=1;
                            sleep(1)
                        elif(self.get_distances()[2] <= self.limits[0] and self.get_distances()[2]!=0):
                            self._spinLeft()
                            count+=1;
                            sleep(1)
                        if(self.searchForBarricade() is True):
                            self._park()
                            #continue
                    elif((self.get_distances()[1] > 30) and (self.get_distances()[1]!=0)):
                        #self.regulateWheelRotation()
                        self.driveStraigthforward((30,30))
                        print("Index:", count)
                        if(count>2):
                            self.ledsEnd()
                            count = 0;
                        # break if the obstacles at both sides are gone
                        if(self.get_distances()[2]>self.limits[0]*3 and self.get_distances()[2]!=0):
                            print('distance:', self.get_distances())
                            self._spinRight()
                        else:
                            continue
                if(count==2):
                    print("driving through a tunnel")
                    self.ledsStart()
                    if(self.searchForBarricade() is True):  # barricade?
                        self._park()
                self._stop()
            else:
                # self.driveStraigthforward((30,30))
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
        if(all(self._convertIntToBool(5, self.get_distances()))):
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
        wait_for_button_press(c.BUTTON_LEFT)
        print('driving along wall')
        while not (self.get_distances()[0] < self.limits[0] and self.get_distances()[0]!=0):
             if (self.get_distances()[1] <= 30 and self.get_distances()[1]!=0):
                 if (self.get_distances()[0] <= self.limits[0] and self.get_distances()[0]!=0):
                     self._spinRight()
                     sleep(1)
                     #continue
                 else:
                     self._spinLeft()
                     sleep(1)
                     #continue

             else:
                 self.driveStraigthforward((30,30));

             if (self.get_distances()[2]>self.limits[0] and self.get_distances()[2]!=0):
                 if not (self.get_distances()[1] <= 30 and self.get_distances()[1]!=0):
                     while not(self.get_distances()[2]<=self.limits[0] and self.get_distances()[2]!=0):
                         self._turnRightActions(flag=None)
                         sleep(1)
                         if (self.get_distances()[2] < self.limits[0] and self.get_distances()[2]!=0):
                            self._stop()
                            break

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
