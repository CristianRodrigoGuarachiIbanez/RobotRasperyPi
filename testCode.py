# -*- coding: utf-8 -*-
import sys
from pibot.nano import Nano


def drive_until_obstacle():
    free = True
    while free:
        dist = nano.get_distances()
        print(dist)
        if dist[1] <= 20 and dist[1] != 0:
            nano.set_motors(0, 0)
            free = False
        else:
            nano.set_motors(30, 30)


def drive_along_wall():
    # code here and remove the pass placeholder
    pass


def main():
    nano.set_motors(0, 0)
    nano.reset_encoders()

    drive_until_obstacle()  # you should comment this line
    # drive_along_wall()    # and uncomment this line in order to run the
                            # drive_along_wall() function


if __name__ == "__main__":
    nano = Nano()
    main()
