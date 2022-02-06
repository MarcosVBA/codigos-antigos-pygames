import pygame as pg
from pygame.locals import *
from random import randint

#pygame init
pg.init()

#Colors
black = (0, 0, 0)
gray = (200,200,200)
white = (255, 255, 255)
red = (255, 0, 0)

#size o the field(square)
gridScale = 40

class Field:
    def __init__(self, x, y, size, bomb = False):
        self.size = size
        self.bomb = bomb
        self.countBomb = 10
        self.collider = pg.Rect(x,y,self.size,self.size)
        self.color = gray
        self.show = False
        self.find = False
        self.wait = 0

    def Update(self):
        #draw a rectangle on position
        pg.draw.rect(screen, self.color, (self.collider.x, self.collider.y, self.size, self.size))
        
        #if is marked or not, change color
        if self.find == True: self.color = (255,0,0)
        else: self.color = (200,200,200)

        #if is visible, do
        if self.show == True and self.bomb == False:
            self.color = (255,255,255)
            self.CheckBombs(True)
            self.WriteNumber()
        if self.show == True and self.bomb == True:
            self.color = (0,255,0)

        #Control the delay of the buttons 
        self.wait += 1
        
    def CheckMouse(self, mousePos, mouseBtn):
        global gameplay

        #Righ Click of the mouse
        if self.collider.collidepoint(mousePos) and mouseBtn[0] and self.find == False and self.wait > 10:
            if self.bomb == True: gameplay = False
            else:
                self.show = True
                self.CheckBombs(True)

        #Left Click of the mouse
        elif self.collider.collidepoint(mousePos) and mouseBtn[2] and self.wait > 10:
            if self.find == True: self.find = False
            else: self.find = True
            self.wait = 0

    def WriteNumber(self):
        global font
        #Make the text with the number of near bombs
        text = font.render(str(self.countBomb), True, (0, 0, 0))
        screen.blit(text,(self.collider.x+15,self.collider.y+6))

    def CheckBombs(self, click = False):
        global col, row, fields
        
        #Position of the field(square)
        pX = int(self.collider.x / self.size)
        pY = int(self.collider.y / self.size)
        
        count = 0

        #Discover the number of bombs near
        for x in range(pX-1,pX+2,1):
            for y in range(pY-1,pY+2,1):
                if x >= 0 and x < col and y >= 0 and y < row:
                    if fields[x][y].bomb == True: count += 1

        #Verify if this has no near bombs and turn visible others fields with out bombs
        if click == True and fields[pX][pY].countBomb == 0:
            for x in range(pX-1,pX+2,1):
                for y in range(pY-1,pY+2,1):
                    if x >= 0 and x < col and y >= 0 and y < row:
                        fields[x][y].show = True
                        
        #Register the number of near bombs              
        self.countBomb = count

            

#Setup
size = width, height = 400, 480
screen = pg.display.set_mode(size)
pg.display.set_caption("Campo Minado")
clock = pg.time.Clock()
font = pg.font.SysFont("comicsansms", 20)

row = int(height/gridScale)
col = int(width/gridScale)

fields = []
maxBomb = 15

#Instantiate all fields and make a control array(matrix) for control
for x in range(0,col):
    rowX = []
    for y in range(0,row):
        #Random bomb position and max bombs
        if randint(0,20) <= 3 and maxBomb > 0:
            rowX.append(Field(x*gridScale, y*gridScale, gridScale, True))
            maxBomb -= 1
        else: rowX.append(Field(x*gridScale, y*gridScale, gridScale))
    fields.append(rowX)

#Check the number of near bombs for all fields
for x in range(0,col):
    for y in range(0,row):
        fields[x][y].CheckBombs()
    
#Loop
showAll = False
gameplay = True
while gameplay:

    #Get keys
    keys = pg.key.get_pressed()
    events = pg.event.get()
    mousePos = pg.mouse.get_pos()
    mouseBtn = pg.mouse.get_pressed()
    for e in events:
          if e.type == pg.QUIT: gameplay = False

    screen.fill(white)

    #Update all fields and verify the end game
    count = 0
    for fieldRow in fields:
        for field in fieldRow:
            field.Update()
            field.CheckMouse(mousePos, mouseBtn)
            if showAll == True: field.show = True
            if field.show == True or field.bomb == True: count += 1
    if count >= col * row: showAll = True

    #Draw the Grid
    for y in range(row):
        for x in range(col):
            pg.draw.line(screen, black, (0,y*gridScale), (width,y*gridScale))
            pg.draw.line(screen, black, (x*gridScale,0), (x*gridScale,height))


    #Time control and update screen
    clock.tick(30)
    pg.display.flip()
      
pg.quit()
