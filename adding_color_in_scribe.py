import time
import os
import math
import random
from termcolor import colored



class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        #making cartesian cordinates x and y axis from top to bottom
        self._canvas = [[" " for y in range(self._y)] for x in range(self._x)]


    def setPosition(self, pos, mark):
        #setting the position of canvas from where it will start
        self._canvas[round(pos[0])][round(pos[1])] = mark

    def hitswallVertical(self, point):
        return round(point[0]) < 0 or round(point[0]) >= self._x

    def hitswallHorizontal(self, point):
        return round(point[1]) < 0 or round(point[1]) >= self._y

    def hitswall(self, point):
        #returns True if given point hits the boundaries of the canvas
        return round(self.hitswallHorizontal(point)) or round(self.hitswallVertical(point))

    def getReflection(self, point):
        return [-1 if self.hitswallVertical(point) else 1, -1 if self.hitswallHorizontal(point) else 1]


    def clear(self):
        os.system("clear")


    def print(self):
        self.clear()
        for y in range(self._y):
            print([" ".join([col[y] for col in self._canvas])])


class CanvasAxis(Canvas):
    #pads 1-deigit numbers with an extra space
    def formatAxisNumber(self, num):
        if num % 5 != 0:
            return ' '
        if num < 10:
            return ' ' + str(num)
        return str(num)

    def print(self):
        self.clear()
        for y in range(self._y):
            print(self.formatAxisNumber(y) + ' '.join([col[y] for col in self._canvas]))

        print(' '.join([self.formatAxisNumber(x) for x in range(self._x)]))



class TerminalScribe:
    def __init__(self, canvas, color="red", mark="*", trail=".", pos=(0,0), framerate=0.05, direction=[0,1]):
        self.canvas = canvas
        self.pos = pos
        self.mark = mark
        self.trail = trail
        self.direction = direction
        self.color = color
        self.framerate = framerate



    def draw(self, pos):
        self.canvas.setPosition(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPosition(self.pos, colored(self.mark, self.color))
        self.canvas.print()
        time.sleep(self.framerate)


    def setDegrees(self, degrees):
        radians = math.radians(degrees)
        self.direction = [math.sin(radians), -math.cos(radians)]


    def bounce(self, pos):
        reflection = self.canvas.getReflection(pos)
        self.direction = [self.direction[0] * reflection[0], self.direction[1] * reflection[1]]
        


    def forward(self, distance):
        for i in range(distance):
            pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
            if self.canvas.hitswall(pos):
                self.bounce(pos)
                pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
            self.draw(pos)


class PlotScribe(TerminalScribe):
    def plotX(self, function):
        for x in range(self.canvas._x):
            pos = [x, function(x)]
            if pos[1] and not self.canvas.hitswall(pos):
                self.draw(pos)



class RobotScribe(TerminalScribe):
    def right(self, distance):
        self.direction = [1, 0]
        self.forward(distance)

    def down(self, distance = 1):
        self.direction = [0, 1]
        self.forward(distance)

    def left(self, distance = 1):
        self.direction = [-1, 0]
        self.forward(distance)

    def up(self, distance = 1):
        self.direction = [0, -1]
        self.forward(distance)

    def drawSquare(self, size):
        self.right(size)
        self.down(size)
        self.left(size)
        self.up(size)


class RandomWalkScribe(TerminalScribe):
    def __init__(self, canvas, degrees = 135, **kwargs):
        super().__init__(canvas, **kwargs)
        self.degrees = degrees

    def randomizeDegreeOrientation(self):
        self.degrees = random.randint(self.degrees-10, self.degrees+10)
        self.setDegrees(self.degrees)

    def bounce(self, pos):
        reflection = self.canvas.getReflection(pos)
        if reflection[0] == -1:
            self.degrees = 360 - self.degrees
        if reflection[1] == -1:
            self.degrees = 180 - self.degrees
        self.direction = [self.direction[0] * reflection[0], self.direction[1] * reflection[1]]

    def forward(self, distance):
        for i in range(distance):
            self.randomizeDegreeOrientation()
            super().forward(1)




'''class RandomWalkScribe(TerminalScribe):
    def __init__(self, degrees = 135, **kwargs):
        super().__init__(canvas, **kwargs)
        self.degrees = degrees
    
    def randomizeDegreeOrientation(self):
        self.degrees = random.randint(self.degrees-10, self.degrees+10)
        self.setDegrees(self.degrees)
 
    def bounce(self, pos):
        reflection = self.canvas.getReflection(pos)
        if reflection[0] == -1:
            self.degrees = 360 - self.degrees
        if reflection[1] == -1:
            self.degrees = 180 - self.degrees
        self.direction = [self.direction[0] * reflection[0], self.direction[1] * reflection[1]]

    def forward(self, distance):
        for i in range(distance):
            self.randomizeDegreeOrientation()
            super().forward(1)

'''


def sine(x):
    return 5 * math.sin(x/4) +10

def cosine(x):
    return 5 * math.cos(x) + 10 



canvas = CanvasAxis(30, 30)
plotscribe = PlotScribe(canvas)
plotscribe.plotX(sine)
#plotscribe.plotX(cosine)

robotscribe = RobotScribe(canvas, color="blue")
robotscribe.drawSquare(10)

randomScribe = RandomWalkScribe(canvas, color="green")
randomScribe.forward(200)

#scribe = TerminalScribe(canvas)
#scribe.setDegrees(120)
#scribe.forward(100)

#randomScribe = RandomWalkScribe(canvas)
#randomScribe.forward(1000)

