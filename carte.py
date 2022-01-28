import random as rd
import numpy as np

class Map:

    def __init__(self, longueur, hauteur):
        self.hauteur = hauteur
        self.longueur = longueur
        self.salles = []
        self.doors = []

    def room_size(self):
        return rd.randint(4, 8), rd.randint(4, 8)

    def grid(self):
        nb_div_x, nb_div_y = rd.randint(1,5), rd.randint(1,5)
        line_x = np.sort([0, rd.randint(0, self.longueur) for k in range(nb_div_x), self.longueur])
        line_y = np.sort([0, rd.randint(0, self.hauteur) for k in range(nb_div_y), self.hauteur])
        salles = []
        for i, x in enumerate(line_x[:-1]):
            for j, y in enumerate(line_y[:-1]):
                salles.append([x,line_x[i+1], y, line_y(j+1)])
        salles.shuffle()
        salles = salles[rd.randint(int((nb_div_x*nb_div_y)/2)):]
        self.salles = salles
        return salles

    def door(self):
        self.salles = self.grid()
        for salle in self.salles:
            nb_door = rd.randint(1,4)
            for door in nb_door:
                k = rd.randint(0,3)
                self.doors.append([[rd.randint(salle[0]+1, salle[1]-1),salle[2]],[rd.randint(salle[0]+1, salle[1]-1),salle[3]],[salle[0],rd.randint(salle[2]+1, salle[3]-1)],[salle[0],rd.randint(salle[2]+1, salle[3]-1)]][k])

    
                


    
    








