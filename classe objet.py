class objet:
    def __init__(self, place, proba ):
        self.place = place
        self.proba = proba
    
    class arme(objet):

        def __init__(self, puissance, portee ):
            self.puissance = puissance
            self.portee = portee
            self.utilisable = False

    class potion(objet):

        def __init__(self, vieajoutee ):
            self.vieajoutee = vieajoutee
            self.utilisable = True
    

    class money(objet):

        def __init__(self, money):
            self.money = money