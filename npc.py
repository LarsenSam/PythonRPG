import json

class Npc:
    def __init__(self,name,max_hp,max_mp,hp,mp,inventory,moveset):
        self.name = name
        self.max_hp = max_hp
        self.max_mp = max_mp
        self.hp = hp
        self.mp = mp
        self.inventory = inventory
        self.moveset = moveset

    def save(self):
        x = {
            "name": self.name,
            "max_hp": self.max_hp,
            "max_mp": self.max_mp,
            "hp": self.hp,
            "mp": self.mp,
            "inventory": self.inventory,
            "moves": self.moveset
        }
        return json.dumps(x)

    def load(self, x):
        y = json.loads(x)
        return Npc(y["name","max_hp","max_mp","hp","mp","inventory","moves"])

