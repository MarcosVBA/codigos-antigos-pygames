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

    def CheckClick(self, mousePos, mouseBtn, campo):
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
        '''font = pg.font.SysFont(None , 20)
        text = font.render(str(n), True, (0, 0, 0))
        screen.blit(text,(self.x+15,self.y+6))'''
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
                            if campo[x][y].bomb == True :
                                count += 1
                else:
                    for x in range(self.iX - 1 + offset, self.iX + 1 + offset):
                        if x < col and x >= 0 and y < row and y >= 0:
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
                        if campo[x][y].bomb == False and campo[x][y].open == False:  
                            campo[x][y].open = True
                            if campo[x][y].count == 0:
                                campo[x][y].OpenCells(campo)

            else:
                for x in range(self.iX - 1 + offset, self.iX + 1 + offset):
                    if x < col and x >= 0 and y < row and y >= 0:
                        if campo[x][y].bomb == False and campo[x][y].open == False:  
                            campo[x][y].open = True
                            if campo[x][y].count == 0:
                                campo[x][y].OpenCells(campo)
                        
                                      

size = width, height = 800, 700
screen = pg.display.set_mode(size)
pg.display.set_caption("Hexagono Minado")
clock = pg.time.Clock()
font = pg.font.SysFont(None , 40)

row = int(height/gridSize)-1
col = int(width/gridSize)-1

campo   = []
maxBombs = 20

for x in range(col):
    rowX = []
    for y in range(row):
        if y % 2 == 0:
            last = Hexagono(x*gridSize+gridSize/2,y*gridSize+gridSize/2, gridSize)
            rowX.append(last)
        else:
            last = Hexagono(x*gridSize+gridSize/2*2,y*gridSize+gridSize/2, gridSize)
            rowX.append(last)
        '''if randint(0,30) <= 7 and maxBombs > 0:
            last.addBomb()
            maxBombs -= 1'''
    campo.append(rowX)

for i in range(0,maxBombs):
    x = randint(0,col-1)
    y = randint(0,row-1)
    campo[x][y].addBomb()

for campoY in campo:
    for hexagono in campoY:
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
            hexagono.Update()
            if win == False:
                hexagono.CheckClick(mousePos,mouseBtn, campo)
                if hexagono.bomb or hexagono.open:
                    winCount += 1
                
    if winCount >= col * row and win == False:
        win = True

    wait += 1  
    clock.tick(60)
    pg.display.flip()
      
pg.quit()


