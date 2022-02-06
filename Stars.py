import pygame as pg
from pygame.locals import *
from random import randint

pg.init()

black = (0, 0, 0)
white = (255, 255, 255)

class Star:
    def __init__(self):
        self.x = randint(-width/2,width/2)
        self.y = randint(-height/2,height/2)
        self.z = randint(1,height)

        self.speed = 0
        self.cSpeed = 0
        self.wait = 0

    def Update(self):
        self.wait += 1
        if keys[K_SPACE]:
            self.speed += 1
            if self.speed > 60: self.speed = 60
        else: self.speed = self.cSpeed
            
        if keys[K_UP] and self.wait > 10:
            self.cSpeed += 1
            if self.cSpeed > 50: self.cSpeed = 50
            self.wait = 0
            
        elif keys[K_DOWN] and self.wait > 10:
            self.cSpeed -= 1
            if self.cSpeed <= 0: self.cSpeed = 0
            self.wait = 0
        
        
        sx = (self.x / self.z)
        sy = (self.y / self.z)
        sx = int(width/2+sx * width/2)
        sy = int(height/2+sy * height/2)
        
        self.z -= 1 + self.speed
        
        if self.z < 1:
            self.x = randint(-width/2,width/2)
            self.y = randint(-height/2,height/2)
            self.z = height

            
        r = 6 - round(self.z / height * 6)
        #pg.draw.circle(screen,white,(sx, sy),r)
        pg.draw.line(screen,white,(sx, sy),(sx,sy))

size = width, height = 1000, 600
screen = pg.display.set_mode(size)
pg.display.set_caption("Space")
clock = pg.time.Clock()

stars = []

for i in range(200):
    stars.append(Star())

gameplay = True
while gameplay:
    keys = pg.key.get_pressed()
    events = pg.event.get()
    for e in events:
          if e.type == pg.QUIT: gameplay = False
    screen.fill(black)
    
    for star in stars:
        star.Update()
    
    
    clock.tick(60)
    pg.display.flip()
      
pg.quit()