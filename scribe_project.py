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
        time.sleep(0.2)


canvas = Canvas(30, 30)
scribe = TerminalScribe(canvas)

for i in range(0,10):
    for j in range(0, 10):
        scribe.draw((i,j))


