import pygame as pg
from pygame.locals import *
from random import randint

pg.init()

#Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
r = (255, 255,   0,   0, 140,   0, 200, 255)
g = (  0, 140, 255,   0,   0, 140, 200, 140)
b = (  0,   0,   0, 255, 255, 255,   0,   0)

#maps
alien = [(5,4),(1,6),(3,3),(3,4),(2,5),(4,2),(4,4),(5,1),(5,1),(5,2),(5,3),(5,4),(4,5),(6,5),(6,2),(6,4),(7,3),(7,4),(8,5),(9,6)]
rainbow = [(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(2,0),(2,1),(3,0),(6,0),(7,0),(7,1),(8,0),(8,1),(8,2),(9,0),(9,1),(9,2),(9,3),(2,7),(3,7),(3,6),(4,5),(4,6),(4,7),(5,5),(5,6),(5,7),(6,6),(6,7),(7,7)]

#Class
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 5
        self.vx = self.vel
        self.vy = -self.vel

        n = randint(0,1)
        if n == 0: self.vx = -self.vx 

    def Update(self):
        self.CheckCollider()
        self.x += self.vx
        self.y += self.vy
        
        pg.draw.circle(screen, white,(self.x, self.y), 10)

    def CheckCollider(self):
        global width, height
        if self.y <= 0:
            self.vy = -self.vy
            self.y = 10
        if self.x >= width:
            self.vx = -self.vx
            self.x = width - 10
        if self.x < 0:
            self.vx = -self.vx
            self.x = 10

class Player:
    def __init__(self, initX, initY):
        self.vel = 7
        self.width = 120
        self.height = 20
        self.collider = pg.Rect(initX, initY, self.width, self.height)
        
    def Update(self):
        self.CheckControl()
        pg.draw.rect(screen, red, self.collider)

    def CheckControl(self):
        global keys, width, clock
        if keys[K_LEFT] and self.collider.x > 0:
            self.collider = self.collider.move(-self.vel,0)
        if keys[K_RIGHT] and self.collider.x + self.width < width:
            self.collider = self.collider.move(self.vel,0)
        if keys[K_SPACE] and self.collider.x + self.width < width:
            self.vel = 15
        else:
            self.vel = 7

    def CheckCollider(self, ball):
        if self.collider.collidepoint(ball.x, ball.y):
            ball.vy = -ball.vy
            ball.y = self.collider.y
            if ball.y < self.collider.y + self.height - ball.vel and ball.y > self.collider.y:
                    ball.vx = -ball.vx

class Brick:
    def __init__(self, x, y, c, random = False):
        global r, g, b
        self.active = True
        self.hp = 2
        self.x = x
        self.y = y
        self.width = 80
        self.height = 30
        self.collider = pg.Rect(x, y, self.width, self.height)
        self.r = r[c]
        self.g = g[c]
        self.b = b[c]

        n = randint(0,5)
        if n == 0 and random == True: self.active = False

    def Update(self, ball):
        global screen
        if self.active:
            if self.collider.collidepoint(ball.x, ball.y):
                
                self.hp -= 1
                
                if self.r > 70: self.r -= 70
                if self.g > 70: self.g -= 70
                if self.b > 70: self.b -= 70
                
                #ball.vy = -ball.vy
                if ball.y < self.collider.y + self.height - ball.vel and ball.y > self.collider.y:
                    ball.vx = -ball.vx
                else: ball.vy = -ball.vy

            if self.hp <= 0: self.active = False        
            pg.draw.rect(screen, (self.r, self.g, self.b), (self.x, self.y, self.width, self.height))
            

#Setup
while 1:
    print("\n\nBem vindo ao Breakout! Você deseja jogar em um mapa customizado? ")
    escolha = input("[y/n]: -> ")
    if escolha == "y" or escolha == "n":
        break
    else:
        print("\nComando Invalida!\n")
if escolha == "y":
    while 1:
        escolha = input("\n Qual mapa você deseja jogar?\n+alien\n+raibow\n+alien dark\n+alien color\n+chess\n-> ")
        if escolha == "alien" or escolha == "rainbow" or escolha == "alien dark" or escolha == "chess" or escolha == "alien color": break
        else: print("\nMapa Invalido!\n")

#escolha = "n"
         
size = width, height = 800, 600
screen = pg.display.set_mode(size)
pg.display.set_caption("Breakout")
clock = pg.time.Clock()

player = Player(400, 550)
ball = Ball(400, 540)
bricks = []

#testBrick = Brick(100, 285, 1)

for y in range(8):
    for x in range(10):
        if escolha == "n":
            bricks.append(Brick(x*80,y*30+25,y, True))
        else:
            if escolha == "alien dark":
                if alien.count((x,y)) == 0:
                    bricks.append(Brick(x*80,y*30,y % 2+2))
            if escolha == "alien color":
                if alien.count((x,y)) == 0:
                    bricks.append(Brick(x*80,y*30,5))
                else:
                    bricks.append(Brick(x*80,y*30,2))
            elif escolha == "alien":
                if alien.count((x,y)) > 0:
                    bricks.append(Brick(x*80,y*30,2))
            elif escolha == "rainbow":
                if rainbow.count((x,y)) == 0:
                    bricks.append(Brick(x*80,y*30,y))
            elif escolha == "chess":
                if x % 2 == 0 and y % 2 == 0 or x % 2 != 0 and y % 2 != 0:
                    bricks.append(Brick(x*80,y*30,y))

#Loop
wait = True
waitTime = 0
gameplay = True
while gameplay:
    keys = pg.key.get_pressed()
    events = pg.event.get()
    for e in events:
          if e.type == pg.QUIT: gameplay = False
    screen.fill(black)
    
    if wait == False:
        ball.Update()
    player.Update()
    player.CheckCollider(ball)
    active = 0
    for brick in bricks:
        brick.Update(ball)
        if brick.active == False: active += 1
    if active == len(bricks):
        break

    #testBrick.Update(ball)

    if wait == True:
        waitTime += 1
        if waitTime >= 240: wait = False
    
    clock.tick(60)
    pg.display.flip()
      
pg.quit()
