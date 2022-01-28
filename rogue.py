import pygame as pg
from random import randint
import numpy as np 
import argparse 

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
clock = pg.time.Clock()


tick = 10

running = True
while running:
    clock.tick(tick)


    #SECTION 1 :
    #lecture des événements :

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP :
                
            elif event.key == pg.K_DOWN:
                
            elif event.key == pg.K_LEFT:
                
            elif event.key == pg.K_RIGHT:
                
    #SECTION 2 : affichage
    screen.fill((0,0,0)) #fond noir
    for pix in pixels :
            
        rect = pg.Rect(x*20, y*20, 20, 20)
        color = (0,0,0)
        pg.draw.rect(screen, color, rect)
    
    pg.display.set_caption(f"Score: {score}") #Affichage du score
    pg.display.update()
