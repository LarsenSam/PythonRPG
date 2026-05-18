import time

from Items import Food, Weapon, Item
from main import Party, Battle


class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.max_hp = hp
        self.hp = self.max_hp
        self.mp = 20
        self.max_mp = 20
        self.party = Party
        self.enemy_party = Party
        self.battle = Battle
        self.isDead = False
        self.moves = []
        self.main_hand = Weapon
        self.inventory = [Food("Cup Noodles",15)]
        self.ailment = None

    def equip(self, weapon):
        self.main_hand = weapon

    def heal(self, hp):
        self.hp += hp
        healed = hp
        if self.hp > self.max_hp:
            healed = self.hp - self.max_hp
            self.hp = self.max_hp
        return healed


    def attack(self,unit):
        unit.takeDmg(3)
        print(self.name + " attacks " + unit.name+" for %s hp! (%s/%s)"%(3,unit.hp,unit.max_hp))
        print()
        self.battle.next()

    def addMoves(self, moves):
        for move in moves:
            self.moves.append(move)
        return self

    def player_input(self):
        print('What will %s do?'%(self.name))
        print("1) Attack")
        print("2) Use Item")
        print("3) Use Spell")
        print("4) Tactics")
        print("5) Escape")
        print()
        act = int(input())
        if (act == 1):
            self.attack(select_unit(self, self.enemy_party,True))
        elif (act == 2):
            self.show_inv()
        elif(act==3):
            self.show_moves()
        elif(act==4):
            for unit in self.party.members:
                print("%s:"%(unit.name))
                print("HP: %s/%s"%(unit.hp,unit.max_hp))
                print("MP: %s/%s"%(unit.mp,unit.max_mp))
                print()
            self.player_input()
        elif (act == 5):
            print("You can't escape!")
            print()
            time.sleep(1)
            self.player_input()
        else:
            self.player_input()
    def show_inv(self):
        i = 1
        for item in self.inventory:
            print("%s) %s"%(i,item.name))
            i+=1
        print("0) Exit")

        print()
        inp = int(input())
        if(inp==0):
            self.player_input()
        elif(inp<len(self.inventory)+1):
            self.use_item(self.inventory[inp-1],self)
            self.battle.next()
        else:self.player_input()



    def show_moves(self):
        i = 1
        for move in self.moves:
            print("%s) %s" %(i,move.name))
            i+=1
        print("0) Exit")
        print()
        inp = int(input())
        if(inp<len(self.moves)+1):
            self.use_move(self.moves[inp-1])
        else:
            self.player_input()



    def use_move(self, move):
        move.execute(self, select_unit(self, self.party, True))
        self.battle.next()

    def stats(self):
        print(self.name)
        print("HP: %s/%s"%(self.hp,self.max_hp))
        print()

    def takeTurn(self):
        if(self.party.player_lead):
            self.player_input()
        else:
            self.attack(self.enemy_party.get_random())
    def takeDmg(self,dmg):
        self.hp -= dmg
        if(self.hp<1):
            self.hp = 0
            self.isDead = True
            print(self.name + " is dead!")

    def use_item(self,item,target):
        item.use(target)
        self.inventory.remove(item)

def select_unit(user, party,alive):
    i = 0
    print()
    print("Select unit")
    print()
    for unit in party.members:
        if (unit.isDead!=alive):
            print("%s) %s (%s/%s)" % (i+1, unit.name,unit.hp,unit.max_hp))
            i+=1
    print("0) Nevermind")
    print()
    num = int(input())

    if(num>len(party.members) or num<0):
        return select_unit(user, party,True)
    elif(num==0):
        user.player_input()
    else:
        return party.members[num-1]