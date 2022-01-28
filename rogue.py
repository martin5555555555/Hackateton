import pygame as pg
from random import randint
import numpy as np 
import argparse 

def draw_rectangle(screen, i, j, size, color):
    rect=pg.Rect(i*size, j*size, size, size)
    pg.draw.rect(screen, color, rect)


pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
size = 5
tick = 10
salles = [(10,60,10,60)]

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
    for salle in salles :
        x0, x1, y0, y1 = salle
        for i in range (x0, x1+1):
            draw_rectangle(screen, i, y0, size, (255,0,0))
            draw_rectangle(screen, i, y1, size, (255,0,0))
        for j in range (y0+1, y1):
            draw_rectangle(screen, x0, j, size, (255,0,0))
            draw_rectangle(screen, x1, j, size, (255,0,0))
    
    
    pg.display.update()












class move_rogue:

    # le constructeur
    def __init__(position, direction):
        # un objet User a deux attributs
        # name et age
        self.position = position
        self.direction = direction

    # l'afficheur
    def __repr__(self):
        ...
    

# # -*- coding: utf-8 -*-
# import pygame as pg
# from random import randint
# WHITE=(0,0,0)
# BLACK=(255,255,255)
# ROUGE=(255,0,0)
# SIZE=30
# PIXEL_SIZE=20
# nb_cases = 30
# pg.init()
# screen = pg.display.set_mode((SIZE*PIXEL_SIZE, SIZE*PIXEL_SIZE))


# fruit=(10,10)

# direction=(0,1)

# def draw_rectangle(screen, i, j, size, color):
#     rect=pg.Rect(i*size, j*size, size, size)
#     pg.draw.rect(screen, color, rect)


# def draw_snake(screen, snake, color, size):
#     for a,b in snake:
#         draw_rectangle(screen, a, b, size, color)

# def generate_fruit(snake , nb_cases):
#     while True:
#         fruit= (randint(0, nb_cases), randint(0, nb_cases))
#         if fruit not in snake:
#             return fruit

# def move_snake(snake, direction):
#     dx, dy = direction
#     x,y = snake[-1]
#     new_head = (x+dx, y+dy)
#     snake.append(new_head)
#     if new_head == fruit:
#         return generate_fruit(snake, nb_cases), True 
#     if any(coord in (-1, nb_cases) for coord in new_head):
#         return fruit, False 
#     snake.pop(0)
#     return fruit, True 

    


# up= (0,-1)
# down= (0,1)
# left=(-1,0)
# right=(1,0)

# snake = [
#     (10, 15),
#     (11, 15),
#     (12, 15),
# ]

# # on crée aussi un objet "horloge"
# clock = pg.time.Clock()

# running = True
# while running is True:
#     clock.tick(5)

#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             running = False
#     # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
#         elif event.type == pg.KEYDOWN:
#             if event.key == pg.K_q:
#                 running = False
#             elif event.key == pg.K_UP:
#                 direction= up
#             elif event.key == pg.K_DOWN:
#                 direction= down
#             elif event.key == pg.K_RIGHT:
#                 direction= right
#             elif event.key == pg.K_LEFT:
#                 direction= left

#     pg.display.update()
#     screen.fill(WHITE)
#     fruit, running=move_snake(snake, direction)
#     draw_snake(screen, snake, BLACK, PIXEL_SIZE)
#     draw_rectangle(screen, *fruit, PIXEL_SIZE, ROUGE)
#     pg.display.update()