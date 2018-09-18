import random

class Warrior:
    def __init__(self, health, attack, defense):
        self.health = health
        self.attack = attack
        self.defense = defense
    
    def attack2(self):
        attackScr = self.attack + random.randint(0,9)
        return attackScr

class Battle:
    def startBattle(self, warriorOne, warriorTwo):
        fight = True
        while fight == True:
            if self.getResult(warriorOne, warriorTwo) == "Done":
                print("Warrior Two is dead")
                break

    @staticmethod
    def getResult(warriorOne, warriorTwo):
        warriorOnePower = warriorOne.attack2()
        warriorTwo.health = warriorTwo.health- warriorOnePower 
        print(warriorTwo.health)

        if warriorTwo.health <= 0:
            return "Done"
        else:
            print("Warrior Two is still alive")
        #THIS WILL ALSO WORK, BUT IT ISN'T A STATIC METHOD
        # def getResult(self, warriorOne, warriorTwo):
        # warriorOnePower = warriorOne.attack2()
        # warriorTwo.health = warriorTwo.health - warriorOnePower 
        # print(warriorTwo.health)

        # if warriorTwo.health <= 0:
        #     return "Done"
        # else:
        #     print("Warrior Two is still alive")



def main():
    warrior1 = Warrior(20, 10, 13)
    warrior2 = Warrior(20, 10, 33)
    battle1 = Battle()
    battle1.startBattle(warrior1, warrior2)





main()
