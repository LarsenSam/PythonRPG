class Npc:
    def __init__(self,name,hp,mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.inventory = []
        self.moveset = []