import pygame as pg
from random import randint
import numpy as np 
import argparse 

def draw_rectangle(screen, i, j, size, color):
    rect=pg.Rect(i*size, j*size, size, size)
    pg.draw.rect(screen, color, rect)


pg.init()

clock = pg.time.Clock()
game = np.array([['MUR','MUR','SALLE'],[1,'MUR',0],[0,1,0]])
ny, nx = game.shape
size = 50
tick = 10
screen = pg.display.set_mode((nx*size, ny*size))


#rogue = rogue()
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
                dir = 0
                
            elif event.key == pg.K_DOWN:
                dir = 0
            elif event.key == pg.K_LEFT:
                dir = 0
            elif event.key == pg.K_RIGHT:
                dir = 0

    #vérifier != mur
        #rogue.move(dir)      
              
    #SECTION 2 : affichage

    pg.display.update()

    screen.fill((0,0,0)) #fond noir
    for i in range(nx):
        for j in range(ny):
            if game[j,i] == 'MUR' :
                draw_rectangle(screen, i, j, size, (255,255,255))
            elif game[j,i] == 'SALLE' :
                draw_rectangle(screen, i, j, size, (50,50,50))          
    
    pg.display.update()

