import random as rd
import numpy as np

class Map:

    def _init_(self, longueur, hauteur, matrice, anciennecase):
        self.hauteur = hauteur
        self.longueur = longueur
        self.matrice = matrice
        self.anciennecase = anciennecase
        
    def grid(self):
        nb_div_x, nb_div_y = rd.randint(1,5), rd.randint(1,5)
        line_x = [rd.randint(0, self.longueur) for k in range(nb_div_x)]
        line_y = [rd.randint(0, self.hauteur) for k in range(nb_div_y)]
        line_x = np.sort (line_x)
        line_y = np.sort (line_y) 
        salles = []
        for i in range (len((line_x[:-1]))):
            for j in range (len(line_y[:-1])):
                salles.append([line_x[i],line_x[i+1], line_y[j], line_y(j+1)])
        salles.shuffle()
        salles = salles[rd.randint(int((nb_div_x*nb_div_y)/2)):]
        return salles

    def door(self):
        salles = self.grid()
        doors = []
        for salle in self.salles:
            nb_door = rd.randint(1,4)
            for door in nb_door:
                k = rd.randint(0,3)
                doors.append([[rd.randint(salle[0]+1, salle[1]-1),salle[2]],[rd.randint(salle[0]+1, salle[1]-1),salle[3]],[salle[0],rd.randint(salle[2]+1, salle[3]-1)],[salle[0],rd.randint(salle[2]+1, salle[3]-1)]][k])
    
    """def remplir(self):
        liste_points_objet = []
        salles = self.grid()
        for k,rectangle in enumerate (salles) :
            P1 = rectangle[0], rectangle[1]
            P2 = rectangle[3], rectangle [1]
            P3 = rectangle[0], rectangle[2]
            P4 = rectangle[3], rectangle[2]
            for c,objets in enumerate liste_objets :
                nombre_objet = int ((cases.longueur) * proba_objets(c))
                n = np.random.randint(0, nombre_objet * 2)
                listespoints_objet_ = [(random.randint(rectangle[0], rectangle[2]), random.randint(rectangle[1], rectangle[3])) for k in range (nombre_objet)]
                liste_point_objet.append(listespoints_objet_)
       """

    def remplir_matrice_init(self):
        #remplissage des salles
        salles = self.grid()
        for l,salle in enumerate (salles):
            for x in range (salle[0], salle[1]):
                   for y in range (salle[2], salle[3]):
                       self.matrice[x,y] = 'SALLE'
        
        #remplissage des murs
        for l,s in enumerate (salles):
            for x in range (salle[0], salle[1]):
                self.matrice[x, salle[2]] = 'MUR'
                self.matrice[x, salle[3]] = 'MUR'

            for y in range (salle[1], salle[3]):
                self.matrice[salle[0], y] = 'MUR'
                self.matrice[salle[1], y] = 'MUR'
        #remplissage des portes
        doors = self.door()
        for d in doors:
            self.matrice[d[0], d[1]] = 'DOOR'

    def move_perso(self, direction, anciennecase, perso): #à appliquer avant de bouger le perso lui même
        self.matrice[peso.posx, perso.posy] = anciennecase
        self.anciennecase = self.matrice[perso.posx, perso.posy]
        self.matrice[perso.posx + dx, perso.posy + dy] = 'PERSO'

           

        

        