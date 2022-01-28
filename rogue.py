import pygame as pg
from random import randint
import numpy as np 
import argparse 

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

tick = 10

#rogue = classe_rogue()
#background = classe_background()
#monstres = classe_monstre()

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
                #vérifier != mur
                #rogue.move(up/down/...)
            elif event.key == pg.K_DOWN:
                #vérifier != mur
                #rogue.move(up/down/...)
            elif event.key == pg.K_LEFT:
                #vérifier != mur
                #rogue.move(up/down/...)
            elif event.key == pg.K_RIGHT:
                #vérifier != mur
                #rogue.move(up/down/...)
                
    #SECTION 2 : affichage
    screen.fill((0,0,0)) #fond noir
    
    
    pg.display.set_caption(f"Score: {score}") #Affichage du score
    pg.display.update()
