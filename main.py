# This is a sample Python script.
from contextlib import nullcontext
import random


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Battle:
    units = []
    def __init__(self, party1, party2):
        self.units = party1.members + party2.members
        current = self.units[0]
        current.takeTurn()
        self.assignEnemies(party1,party2)
        self.assignEnemies(party2,party1)
    def assignEnemies(self,party1,party2):
        for unit in party1.members:
            for enemy in party2.members:
                unit.enemies.append(enemy)

    def next(self):
        current = self.units[(self.units.index(self.current)+1)%len(self.units)]

class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.max_hp = hp
        self.hp = self.max_hp
        self.party = nullcontext
    moves = []
    enemies = []

    def attack(self,unit):
        print(self.name + " attacks " + unit.name+" for %s hp!"%3)
        print()
        unit.hp -= 3

    def stats(self):
        print(self.name)
        print("HP: %s/%s"%(self.hp,self.max_hp))
        print()

    def takeTurn(self):
        if(self.party.player_lead):
            player_input()
        else:
            self.attack(enemy_party.get_random())

class Party:
    def __init__(self,members):
        self.members = members
        for unit in self.members:
            unit.party = self
    player_lead = False

    def get_random(self):
        random.randint(0,len(self.members))


class Move:
    def __init__(self, name, dmg):
        self.name = name
        self.dmg = dmg

def create_player(name):
    return create_unit(name,20)

def select_unit(party):
    i = 0
    for unit in party:
        print()

def player_input():
    print('What will you do?')
    print("1) Attack")
    print("2) Use Item")
    print("3) Use Spell")
    print("4) Escape")
    act = input()
    if(act == 1):
        print("attack!")


def create_unit(name,hp):
    unit = Unit(name, hp)
    return unit

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print('Input your name.')
    name = "Sam"
    player = create_player(name)
    enemy = create_unit('Goblin',15)
    player_party = Party([player])
    player_party.player_lead = True
    enemy_party  = Party([enemy])
    enemy.stats()
    battle = Battle(player_party,enemy_party)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
