#libaries 
from ohbot import ohbot
import random
import os
import ffmpeg


#test block (commands)
#ohbot.reset()
#ohbot.move(ohbot.HEADNOD, 10)
#ohbot.wait(1)
#ohbot.move(ohbot.HEADTURN, 10)
#ohbot.wait(1)
#ohbot.move(ohbot.EYETRUN, 10)
#ohbot.wait(1)
#ohbot.move(ohbot.LIDBLINK, 10)
#ohbot.wait(1)
#ohbot.move(ohbot.TOPLIP, 10)
#ohbot.wait(1)
#ohbot.move(ohbot.BOTTOMLIP, 10)
#ohbot.wait(1)
#ohbot.move(ohbot.EYETILT, 10)
#ohbot.wait(1)
#ohbot.say("Hello World")
#ohbot.wait(1)
#ohbot.reset()

#main block - 
ohbot.reset()

def main():
    input("Press Enter to start")
    ohbot.move(ohbot.HEADNOD, 10)
    ohbot.wait(1)
    ohbot.move(ohbot.HEADTURN, 1)
    ohbot.move(ohbot.HEADNOD, 1)

