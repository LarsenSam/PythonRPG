import random
import units
import time
import moves
from moves import Heal, Resurrect


class Battle:
    turn_order = []
    def __init__(self, party1, party2):
        self.turn_order = party1.members + party2.members
        self.current = self.turn_order[0]
        self.assignEnemies(party1, party2)
        self.assignEnemies(party2, party1)
        self.current.takeTurn()
    def assignEnemies(self,party1,party2):
        for unit in party1.members:
            unit.enemy_party = party2
            unit.battle = self

    def next(self):
        time.sleep(1)
        self.current = self.turn_order[(self.turn_order.index(self.current) + 1) % len(self.turn_order)]
        if(self.current.isDead):
            self.next()
        else:
            self.current.takeTurn()



class Party:
    def __init__(self,members):
        self.members = members
        for unit in self.members:
            unit.party = self
    player_lead = False

    def get_random(self):
        x = random.randint(0,len(self.members)-1)
        return self.members[x]

class Move:
    def __init__(self, name, dmg):
        self.name = name
        self.dmg = dmg

def create_player(name):
    return create_unit(name,20)


def create_unit(name,hp):
    unit = units.Unit(name, hp)
    return unit

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print('Input your name.')
    name = "Max"
    player = create_player(name)
    trey = create_unit("Trey",25)
    goblin = create_unit('Goblin',15)
    mosquito = create_unit("Mosquito",15)
    siren = create_unit("Siren",30)
    player_party = Party([player.addMoves([Heal(),Resurrect()]),trey])
    player_party.player_lead = True
    enemy_party  = Party([goblin,mosquito,siren])
    battle = Battle(player_party,enemy_party)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
