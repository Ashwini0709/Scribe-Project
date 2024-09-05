import time
import os
import math



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



class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.pos = [0,0]

        self.mark = "*"
        self.trail = "."

        self.direction = [0,1]



    def draw(self, pos):
        self.canvas.setPosition(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPosition(self.pos, self.mark)
        self.canvas.print()
        time.sleep(0.05)


    def drawSquare(self, size):

        for i in range(size):
            self.right()

        for i in range(size):
            self.down()

        for i in range(size):
            self.left()

        for i in range(size):
            self.up()

    
    def right(self):
        self.direction = [1, 0]
        self.forward(1)

    def down(self):
        self.direction = [0, 1]
        self.forward(1)

    def left(self):
        self.direction = [-1, 0]
        self.forward(1)

    def up(self):
        self.direction = [0, -1]
        self.forward(1)


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


    def plotX(self, function):
        for x in range(self.canvas._x):
            pos = [x, function(x)]
            if pos[1] and not self.canvas.hitswall(pos):
                self.draw(pos)


def sine(x):
    return 5 * math.sin(x/4) +10

def cosine(x):
    return 5 * math.cos(x) + 10 



canvas = Canvas(30, 30)
scribe = TerminalScribe(canvas)
scribe.plotX(sine)
scribe.plotX(cosine)


