import sys
sys.path.append('/home/pi/hufabot')

from pibot.background import background
from pibot.startup import startup

startup()
background()
