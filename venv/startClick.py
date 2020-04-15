import pyautogui as gui
import random
import time
gui.FAILSAFE = True

class start():
    def __init__(self):
        self.role = 1
        self.x = -1
        self.y = -1
        self.timeGap = 0

    def setRole(self,role):
        self.role = role

    def setX(self,x):
        self.x = x

    def setY(self,y):
        self.y = y

    def setTime(self,t):
        self.timeGap = t

    def click(self):
        if self.role == 1:
            self.leaderClick()
        else:
            self.teammateClick()

    def leaderClick(self):
        tempX = self.x + random.randint(-20, 20)
        tempY = self.y + random.randint(-20, 20)
        gui.moveTo(tempX, tempY, duration=0.5)
        gui.click(tempX, tempY)
        print('start')
        time.sleep(7 + random.randint(-50, 50) / 100)
        while True:
            time.sleep(self.timeGap + 10 + random.randint(-50,50)/100)
            tempX = self.x - 100 + random.randint(0,50)
            tempY = self.y - 100 + random.randint(0,50)
            gui.moveTo(tempX,tempY,duration=0.5)
            gui.click(tempX,tempY)
            print('end')
            time.sleep(3 + random.randint(-50, 50) / 100)
            tempX1 = self.x + random.randint(-20, 20)
            tempY1 = self.y + random.randint(-20, 20)
            gui.moveTo(tempX1, tempY1, duration=0.5)
            gui.click(tempX1, tempY1)
            print('start')
            time.sleep(7 + random.randint(-50, 50) / 100)

    def teammateClick(self):
        while True:
            time.sleep(self.timeGap + 10 + random.randint(-50,50)/100)
            tempX = self.x + random.randint(-20, 20)
            tempY = self.y + random.randint(-20, 20)
            gui.moveTo(tempX, tempY, duration=0.5)
            gui.click(tempX, tempY)
            time.sleep(3 + 7 + random.randint(-50, 50) / 100)




