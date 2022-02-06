import pygame as pg
from random import randint

pg.init()

#cores
black = (  0,   0,   0)
white = (255, 255, 255)
gray  = (180, 180, 180)
red   = (255,   0,   0)
green = (  0, 180,   0)
brown = (80, 40,   0)

gridSize = 65


class Hexagono:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.polygon = ((x,y),(x+size/2,y-size/3),(x+size,y),(x+size,y+size/3*2),(x+size/2,y+size),(x,y+size/3*2))
        self.rect = pg.Rect(x,y,size,size/3*2)
        self.color = gray
        self.border = 4

        self.open = False
        self.bomb = False
        self.count = 0
        self.selected = False
        
        self.iY = int((y/size)-0.5)
        if self.iY % 2 != 0:
            self.iX = int((x/size)-1)
        else:
            self.iX = int(x/size)

        
    def Update(self):
        global win
        if self.bomb and win:
            pg.draw.polygon(screen, green, self.polygon)
        else:
            if self.selected and self.open == False:
                pg.draw.polygon(screen, red, self.polygon)
            else:   
                pg.draw.polygon(screen, self.color, self.polygon)
        pg.draw.polygon(screen, black, self.polygon, self.border)
        if self.open:
            self.WriteNumber(self.iX)
            self.Open()

    def CheckClick(self, mousePos, mouseBtn, campo, draw):
        global gameplay, wait
        if self.rect.collidepoint(mousePos) and mouseBtn[0] and wait >= 10 and self.selected == False:
            if self.bomb:
                gameplay = False
            else:
                self.Open()
                if self.count == 0: self.OpenCells(campo)
            wait = 0
                
        if self.rect.collidepoint(mousePos) and mouseBtn[2] and wait >= 10:
            if self.selected:
                self.selected = False
            else:
                self.selected = True
            wait = 0

    def Open(self):
        self.color = white
        self.border = 1
        self.open = True

    def WriteNumber(self,n):
        global font
        if self.bomb == False:
            text = font.render(str(self.count), True, (0, 0, 0))
            screen.blit(text,(self.x+self.size/2-7,self.y+self.size/6+2))

    def addBomb(self):
        self.bomb = True

    def CountBombs(self,campo):
        global row, col
        if self.bomb == False:
            if self.iY % 2 != 0: offset = 1
            else: offset = 0
            count = 0
            for y in range(self.iY - 1, self.iY + 2):
                if y == self.iY:
                    for x in range(self.iX -1, self.iX + 2):
                        if x < col and x >= 0 and y < row and y >= 0:
                            if campo[x][y] != 0:
                                if campo[x][y].bomb == True :
                                    count += 1
                else:
                    for x in range(self.iX - 1 + offset, self.iX + 1 + offset):
                        if x < col and x >= 0 and y < row and y >= 0:
                            if campo[x][y] != 0:
                                if campo[x][y].bomb == True:
                                    count += 1
            self.count = count
            
    def OpenCells(self, campo):
        global row, col
        if self.iY % 2 != 0: offset = 1
        else: offset = 0
        
        for y in range(self.iY - 1, self.iY + 2):
            if y == self.iY:
                for x in range(self.iX -1, self.iX + 2):
                    if x < col and x >= 0 and y < row and y >= 0:
                        if campo[x][y] != 0:
                            if campo[x][y].bomb == False and campo[x][y].open == False:  
                                campo[x][y].open = True
                                if campo[x][y].count == 0:
                                    campo[x][y].OpenCells(campo)

            else:
                for x in range(self.iX - 1 + offset, self.iX + 1 + offset):
                    if x < col and x >= 0 and y < row and y >= 0:
                        if campo[x][y] != 0:
                            if campo[x][y].bomb == False and campo[x][y].open == False:  
                                campo[x][y].open = True
                                if campo[x][y].count == 0:
                                    campo[x][y].OpenCells(campo)
                        
                                      

size = width, height = 800, 800
screen = pg.display.set_mode(size)
pg.display.set_caption("Hexagono Minado")
clock = pg.time.Clock()
font = pg.font.SysFont(None , 40)

row = int(height/gridSize)-1
col = int(width/gridSize)-1

campo   = []
maxBombs = 12

draw0 = [(5, 0), (4, 1), (5, 1), (4, 2), (5, 2), (6, 2), (3, 3), (4, 3), (5, 3), (6, 3), (7, 2), (7, 3), (7, 4), (8, 4), (7, 5), (8, 5), (8, 6), (9, 6), (8, 7), (8, 7), (8, 7), (7, 7), (8, 8), (6, 7), (7, 8), (6, 8), (5, 7), (5, 6), (4, 5), (4, 4), (3, 4), (3, 5), (4, 6), (4, 7), (5, 8), (4, 8), (3, 7), (3, 6), (2, 5), (2, 6), (2, 7), (3, 8), (2, 8), (1, 7)]
draw1 = [(1, 7), (2, 8), (2, 9), (3, 8), (2, 7), (2, 6), (1, 5), (2, 5), (3, 6), (3, 7), (2, 4), (4, 6), (3, 5), (3, 4), (2, 3), (3, 2), (3, 3), (4, 4), (4, 5), (5, 4), (4, 3), (4, 2), (3, 1), (4, 1), (5, 2), (5, 3), (6, 4), (6, 5), (7, 6), (7, 7), (8, 6), (7, 5), (7, 4), (6, 3), (6, 2), (5, 1), (6, 1), (7, 2), (7, 3), (8, 4), (8, 5), (9, 6), (8, 7), (8, 8), (9, 7), (9, 8), (8, 9), (9, 4), (8, 3), (8, 2), (7, 1), (9, 5), (5, 8), (5, 7), (6, 8), (5, 9), (4, 9), (6, 9), (5, 10), (6, 10), (7, 10), (4, 10), (3, 9), (7, 9), (2, 10), (1, 9), (1, 8), (10, 8), (9, 9), (9, 10), (0, 5), (1, 4), (1, 3), (2, 1), (2, 2), (8, 1), (9, 2), (9, 3), (10, 4), (10, 5)]
draw2 = [(0, 5), (1, 4), (1, 6), (1, 5), (2, 6), (2, 4), (2, 5), (3, 4), (3, 6), (3, 5), (4, 4), (4, 6), (4, 5), (5, 4), (5, 6), (5, 5), (6, 4), (6, 5), (6, 6), (7, 4), (7, 6), (7, 5), (8, 4), (8, 6), (8, 5), (9, 4), (9, 5), (9, 6), (4, 3), (5, 3), (5, 2), (4, 2), (6, 2), (6, 2), (4, 1), (5, 0), (5, 1), (4, 7), (4, 8), (4, 9), (5, 8), (5, 7), (6, 8), (5, 9), (5, 10)]
draw3 = [(1, 1), (2, 2), (2, 1), (3, 2), (2, 3), (3, 1), (4, 2), (3, 3), (4, 1), (5, 2), (4, 3), (4, 4), (3, 4), (3, 5), (5, 4), (5, 3), (6, 2), (5, 1), (6, 1), (4, 5), (4, 6), (7, 2), (6, 3), (6, 4), (5, 5), (5, 6), (4, 7), (3, 7), (4, 8), (5, 8), (4, 9), (5, 7), (6, 6), (6, 5), (7, 4), (7, 3), (7, 6), (6, 7), (7, 7), (8, 6), (9, 6), (7, 1), (8, 1), (9, 2), (8, 3), (9, 5), (10, 4), (9, 3), (2, 7), (2, 6), (1, 5), (2, 4), (5, 10), (6, 10), (7, 9), (7, 10), (8, 8), (3, 10), (4, 10), (2, 9), (2, 8)]
draw4 = [(3, 2), (2, 3), (3, 4), (2, 4), (4, 2), (3, 3), (3, 1), (4, 1), (5, 1), (5, 0), (4, 0), (6, 0), (6, 1), (6, 2), (7, 2), (6, 3), (7, 3), (7, 4), (8, 4), (7, 5), (8, 5), (2, 5), (1, 5), (0, 5), (1, 4), (1, 3), (2, 2), (2, 1), (3, 0), (7, 0), (7, 1), (8, 2), (8, 3), (9, 4), (9, 5), (1, 6), (2, 6), (3, 6), (1, 7), (2, 7), (3, 7), (2, 8), (3, 8), (4, 8), (2, 9), (4, 9), (3, 9), (7, 6), (8, 6), (9, 6), (6, 7), (7, 7), (8, 7), (6, 8), (7, 8), (8, 8), (5, 9), (6, 9), (7, 9), (3, 10), (4, 10), (5, 10), (6, 10), (7, 10)]
draw5 = [(0, 0), (0, 1), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 3), (1, 4), (2, 4), (2, 3), (0, 5), (1, 6), (2, 6), (2, 5), (0, 7), (1, 8), (2, 8), (2, 7), (0, 9), (1, 10), (2, 10), (2, 9), (0, 10), (3, 8), (3, 8), (4, 8), (4, 9), (4, 10), (3, 10), (3, 6), (4, 6), (4, 7), (4, 5), (4, 4), (3, 4), (4, 3), (4, 2), (3, 2), (4, 1), (4, 0), (3, 0), (5, 10), (6, 10), (6, 9), (6, 8), (5, 8), (6, 7), (6, 6), (5, 6), (6, 5), (6, 4), (5, 4), (6, 3), (6, 2), (5, 2), (6, 1), (6, 0), (5, 0), (7, 10), (8, 10), (8, 9), (8, 8), (7, 8), (8, 7), (8, 6), (7, 6), (8, 5), (8, 4), (7, 4), (8, 3), (8, 2), (7, 2), (8, 1), (8, 0), (7, 0), (9, 10), (10, 10), (10, 9), (10, 8), (9, 8), (10, 7), (10, 6), (9, 6), (10, 5), (10, 4), (9, 4), (10, 3), (10, 2), (9, 2), (10, 1), (10, 0), (9, 0)]
draws = [draw0,draw1,draw2,draw3,draw4,draw5]
draw = draws[randint(0,len(draws)-1)]
#draw = draws[5]

winCond = 0

for x in range(col):
    rowX = []
    for y in range(row):
        d = False
        for cell in draw:
            if (x,y) == cell:
                d = True
        if d == True:
            if y % 2 == 0:
                last = Hexagono(x*gridSize+gridSize/2,y*gridSize+gridSize/2, gridSize)
                rowX.append(last)
            else:
                last = Hexagono(x*gridSize+gridSize/2*2,y*gridSize+gridSize/2, gridSize)
                rowX.append(last)
            winCond += 1
        else: rowX.append(0)
    campo.append(rowX)

for i in range(0,maxBombs):
    while 1:
        x = randint(0,col-1)
        y = randint(0,row-1)
        if campo[x][y] != 0:
            campo[x][y].addBomb()
            break

for campoY in campo:
    for hexagono in campoY:
        if hexagono != 0:
            hexagono.CountBombs(campo)

win = False
wait = 0
gameplay = True
while gameplay:

    mousePos = pg.mouse.get_pos()
    mouseBtn = pg.mouse.get_pressed()
    events   = pg.event.get()
    for e in events:
          if e.type == pg.QUIT: gameplay = False

    screen.fill(white)

    winCount = 0
    for campoY in campo:
        for hexagono in campoY:
            if hexagono != 0:
                hexagono.Update()
                if win == False:
                    hexagono.CheckClick(mousePos,mouseBtn, campo, draw)
                    if hexagono.bomb or hexagono.open or hexagono == 0:
                        winCount += 1
                
    if winCount >= winCond and win == False:
        win = True

    wait += 1  
    clock.tick(60)
    pg.display.flip()
      
pg.quit()


