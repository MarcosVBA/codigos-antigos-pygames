import pygame as pg
from pygame.locals import *
from random import randint

pg.init()

#Colors
black = (0, 0, 0)
white = (255, 255, 255)

gridSize = 30

class Cell:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.ix = int(x / size)
        self.iy = int(y / size)
        self.size = size
        self.visited = False
        self.walls = [True, True, True, True]
        
    def Draw(self):
        if self.visited:
            pg.draw.rect(screen,(100,0,100), (self.x,self.y,self.size,self.size))
        if self.walls[0]:
            pg.draw.line(screen, white, (self.x,self.y),(self.x + self.size, self.y))
        if self.walls[1]:
            pg.draw.line(screen, white, (self.x + self.size, self.y),(self.x + self.size, self.y + self.size))
        if self.walls[2]:
            pg.draw.line(screen, white, (self.x + self.size, self.y + self.size),(self.x, self.y + self.size))
        if self.walls[3]:
            pg.draw.line(screen, white, (self.x,self.y + self.size),(self.x, self.y))

    def FindWay(self, grid):
        global col, row
        
        top = self.ix + (self.iy-1) * col
        right = self.ix + self.iy * col + 1
        botton = self.ix + (self.iy+1) * col
        left = self.ix + self.iy * col - 1
        
        avaliableWays = []
        if top >= 0:
            if grid[top].visited == False:
                avaliableWays.append(grid[top])
        if right < col*row and right < (self.iy+1) * col:
            if grid[right].visited == False:
                avaliableWays.append(grid[right])
        if botton < row*col:
            if grid[botton].visited == False:
                avaliableWays.append(grid[botton])
        if left >= 0 and left >= self.iy * col:
            if grid[left].visited == False:
                avaliableWays.append(grid[left])

        if len(avaliableWays) > 0:
            i = randint(0,len(avaliableWays)-1)
        elif len(avaliableWays) == 0: i = 0

        if avaliableWays == []: return False

        if index(avaliableWays[i]) == top:
            avaliableWays[i].walls[2] = False
            grid[index(self)].walls[0] = False
            
        elif index(avaliableWays[i]) == right:
            avaliableWays[i].walls[3] = False
            grid[index(self)].walls[1] = False
            
        elif index(avaliableWays[i]) == botton:
            avaliableWays[i].walls[0] = False
            grid[index(self)].walls[2] = False
            
        elif index(avaliableWays[i]) == left:
            avaliableWays[i].walls[1] = False
            grid[index(self)].walls[3] = False
        
        return avaliableWays[i]
    
    def BackTrack(self):
        global way


def index(obj):
    return obj.ix + obj.iy * col

#Setup
size = width, height = 601, 601
screen = pg.display.set_mode(size)
pg.display.set_caption("Maze Generator")
clock = pg.time.Clock()

col = round(width / gridSize)
row = round(height / gridSize)

grid = []
way = []

for y in range(row):
    for x in range(col):
        grid.append(Cell(x * gridSize,y * gridSize, gridSize))

finder = grid[0]
finder.visited = True

rand1 = randint(0,len(grid)-1)
rand2 = randint(0,len(grid)-1)

stop = False
gameplay = True
while gameplay:
    keys = pg.key.get_pressed()
    events = pg.event.get()
    for e in events:
          if e.type == pg.QUIT: gameplay = False
    screen.fill(black)

    count = 0
    for cell in grid:
        cell.Draw()
        if cell.visited == True: count += 1
    if count == len(grid): stop = True

    if stop == False:

        finder = finder.FindWay(grid)
        if finder == False:
            finder = way[-1]
            way.pop()
        else: way.append(finder)
        finder.visited = True

        pg.draw.rect(screen,(0,255,0),(finder.x, finder.y, gridSize,gridSize))

    else:
        pg.draw.circle(screen,(255,255,255),(round(grid[rand1].x + gridSize/2), round(grid[rand1].y + gridSize/2)), round(gridSize/4))
        pg.draw.circle(screen,(255,255,255),(round(grid[rand2].x + gridSize/2), round(grid[rand2].y + gridSize/2)), round(gridSize/4))

    
    clock.tick(60)
    pg.display.flip()
      
pg.quit()
