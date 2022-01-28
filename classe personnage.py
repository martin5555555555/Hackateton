class personnage:
    
    def _init_(self, posx, posy, materiel, vie, puissance, portee, place, argent):
        self.posx = posx
        self.posy = posy
        self.materiel = materiel # listes d'objet
        self.vie = vie
        self.puissance = puissance
        self.portee = portee
        self.place = place
        self.argent = argent

    def pick_objet(self, vie, puissance, portee, place, objet, utilisable):
        self.vie += vie
        self.puissance += puissance
        self.portee += portee
        self.place += place
        if utilisable:
            self.materiel.append(objet)
    
    def degats_subis(self, degats):
        self.vie -= degats
    
    def pick_argent(self, argent):
        self.argent += argent
    
    def use_objet(self, objet):
        

