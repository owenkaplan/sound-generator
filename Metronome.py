import os, time
import pygame, sys
from pygame.locals import *

pygame.mixer.pre_init()
pygame.init()
fil = "/Users/Baxter/Desktop/gman.ogg"
sound = pygame.mixer.Sound(fil)
print fil

# set window size
width = 246
height = 49

# initilaise pygame

windowSurfaceObj = pygame.display.set_mode((width,height),1,16)
redColor = pygame.Color(100,0,0)
blackColor = pygame.Color(0,0,0)

#starting position
x = 120
pygame.draw.rect(windowSurfaceObj,redColor,Rect(x,2.5,10,45))
pygame.display.update(pygame.Rect(0,0,width,height))


start_time = time.time()
s = 0
while s == 0:
    elapsed_time = time.time() - start_time
    sound.play()
    print elapsed_time
    button = pygame.mouse.get_pressed()
    if button[0] != 0:
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        a = x - 5
        if a < 0:
           a = 0
        pygame.draw.rect(windowSurfaceObj,blackColor,Rect(0,0,width,height))
        #pygame.display.update(pygame.Rect(0,0,width,height))
        pygame.draw.rect(windowSurfaceObj,redColor,Rect(a,2.5,10,45))
        pygame.display.update(pygame.Rect(0,0,width,height))
        print a

   # check for ESC key pressed, or pygame window closed, to quit
    for event in pygame.event.get():
       if event.type == QUIT:
          pygame.quit()
          sys.exit()
       elif event.type == KEYDOWN:
          if event.key == K_ESCAPE:
             pygame.quit()
             sys.exit()

