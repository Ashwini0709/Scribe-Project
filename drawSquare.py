import time
import os


class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        #making cartesian cordinates x and y axis from top to bottom
        self._canvas = [[" " for y in range(self._y)] for x in range(self._x)]


    def setPosition(self, pos, mark):
        #setting the position of canvas from where it will start
        self._canvas[pos[0]][pos[1]] = mark

    def hitswall(self, point):
        #returns True if given point hits the boundaries of the canvas
        return point[0] < 0 or point[0] >= self._x or point[1] < 0 or point[1] >= self._y


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
        pos = [self.pos[0]+1,self.pos[1]]
        if not self.canvas.hitswall(pos):
            self.draw(pos)

    def down(self):
        pos = [self.pos[0],self.pos[1]+1]
        if not self.canvas.hitswall(pos):
            self.draw(pos)

    def left(self):
        pos = [self.pos[0]-1,self.pos[1]]
        if not self.canvas.hitswall(pos):
            self.draw(pos)

    def up(self):
        pos = [self.pos[0],self.pos[1]-1]
        if not self.canvas.hitswall(pos):
            self.draw(pos)









canvas = Canvas(30, 30)
scribe = TerminalScribe(canvas)
scribe.drawSquare(10)
