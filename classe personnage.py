class personnage:
    
    def _init_(self, posx, posy, materiel, vie, puissance, portee, place):
        self.posx = posx
        self.posy = posy
        self.materiel = materiel # listes d'objet
        self.vie = vie
        self.puissance = puissance
        self.portee = portee
        self.place = place

    def pick_objet(self, vie, puissance, portee, place, objet, utilisable):
        self.vie += vie
        self.puissance += puissance
        self.portee += portee
        self.place += place
        if utilisable:
            self.materiel.append(objet)

