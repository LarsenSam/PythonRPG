from main import Party, Battle


class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.max_hp = hp
        self.hp = self.max_hp
        self.party = Party
        self.enemy_party = Party
        self.battle = Battle
        self.isDead = False
    moves = []
    enemies = []

    def attack(self,unit):
        unit.takeDmg(3)
        print(self.name + " attacks " + unit.name+" for %s hp! (%s/%s)"%(3,unit.hp,unit.max_hp))
        print()
        self.battle.next()

    def player_input(self):
        print('What will you do?')
        print("1) Attack")
        print("2) Use Item")
        print("3) Use Spell")
        print("4) Escape")
        print()
        act = int(input())
        if (act == 1):
            self.attack(select_unit(self, self.enemy_party))
        elif (act == 2):
            self.show_inv()
        elif (act == 4):
            print("You can't escape!")
            print()
            self.player_input()
        else:
            self.player_input()
    def show_inv(self):
        print("1) Red Bull")
        print("0) Exit")
        print()
        if(int(input())==0):
            self.player_input()
        else:self.player_input()
    def show_moves(self):
        for move in self.moves:
            print(move.name)
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

def select_unit(unit, party):
    i = 0
    print()
    print("Select unit")
    print()
    for unit in party.members:
        print("%s) %s" % (i+1, unit.name))
        i+=1
    print("0) Nevermind")
    print()
    num = int(input())

    if(num>len(party.members) or num<0):
        return select_unit(unit, party)
    elif(num==0):
        unit.player_input(unit)
    else:
        return party.members[num-1]
