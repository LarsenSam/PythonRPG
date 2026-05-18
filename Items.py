class Item:
    def __init__(self,name):
        self.name = name

class Food(Item):
    def __init__(self,name,hp,mp):
        super().__init__(name)
        self.hp = hp
        self.mp = mp


class Weapon(Item):
    def __init__(self,name,dmg):
        super.__init__(name)
        self.dmg = dmg