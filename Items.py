class Item:
    def __init__(self,name):
        self.name = name
    def use(self,target):
        pass

class Food(Item):
    def __init__(self,name,hp):
        super().__init__(name)
        self.hp = hp
        self.mp = 0
    def use(self,target):
        target.heal(self.hp)
        print("%s ate %s and restored %s hp!" % (target.name,self.name,self.hp))


class Weapon(Item):
    def __init__(self,name,dmg):
        super.__init__(name)
        self.dmg = dmg