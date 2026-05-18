class Move:
    def __init__(self,name,cost):
        self.name = name
        self.cost = cost

    def execute(self,user,target):
        user.mp -= self.cost

class Attack(Move):
    def __init__(self,name,dmg,cost):
        super().__init__(name,cost)
        self.dmg = dmg

class Heal(Move):
    def __init__(self):
        super().__init__("Heal",3)
    def execute(self,user,target):
        super().execute(user,target)
        print("%s healed %s!" % (user.name,target.name))
        target.heal(20)

class Resurrect(Move):
    def __init__(self):
        super().__init__("Resurrect",8)
    def execute(self,user,target):
        super().execute(user,target)
        target.isDead = False
        target.hp = target.max_hp
        print("%s has been resurrected by %s!"%(target.name,user.name))


