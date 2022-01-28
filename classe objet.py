class objet:
    def _init_(self, place, proba ):
        self.place = place
        self.proba = proba
    
    class arme(objet):

        def _init_(self, puissance, portee ):
            self.puissance = puissance
            self.portee = portee

    class potion(objet):

        def _init_(self, vieajoutee ):
            self.vieajoutee = vieajoutee