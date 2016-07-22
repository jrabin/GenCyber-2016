# -*- coding: utf-8 -*-
"""
GenCyber 2016
Pokemon Go Attempt
Created on Fri Jul  8 13:14:36 2016
object oriented programming--> creation of objects with different properties and such
        for example diff. pokemon have diff. properties
classes!--> like cookie cutters
"""
from random import randint

class Pokemon:
    #Pokemon traits
    def __init__(self, oriName, oriType, orihp, oriMoves): #This is called a constructer
        self.name= oriName
        self.type= oriType
        self.hp= orihp 
        self.cp= randint(1, 600)
        self.moves= oriMoves
    #Fight
    def battle(self, myMove, opponent, opponentMove):
        #Make my move and announce it
        print(self.name +"USED" + myMove + "!!!")
        #opponent health = m attack damage
        opponent.hp -= (self.moves[myMove] * self.cp)
        print(opponent.name + "HAS" + str(opponent.hp) + "HP LEFT!!!")
        #Check if they are alive
        if opponent.hp <=0:
            print(opponent.name + " DIED!!!")
            return
        #Make their move
        print(opponent.name + "USED" + opponentMove + "!!!")
        self.hp -= (opponent.move[opponentMove] * opponent.cp)
        print(self.name + "HAS" + str(self.hp) + "HP LEFT!!!")
        #Check if I'm alive
        if self.hp <=0:
            print(Self.name + "DIED!!!")
            print("YOU LOSE!!!")
            return
        print("DRAW!!!")
        
         
eevee_moves = {"Swift":10, "Dig":20}        
vee = Pokemon("Eevee", "Normal", 5)

squirtle_moves={"Squirt":40, "Water Gun":100}
squats = Pokemon("Squirtle", "Water", 90)

print("Vee Cp:" + str(vee.cp))
print("Squats CP:" + str(squatas.cp))

vee.battle("Dig", squats, "Squirt")



"""
NUMBER 1, IM A GIRL IN A WORLD IN WHICH MY ONLY JOB IS TO MARRY RICH, MY FATHER 
HAS NO SONS WHO HAS TO SOCIAL CLIMB THE ONE SO IM THE OLDEST AND THE WITTIEST 
AND THE GOSSIP IN NEW YORK CITY IS InSIDIOUS AND ALEXANDER IS PENNILESS THAT 
DOESNT MEAN I WANT HIM ANY LESS
NUMBER 2, HES AFTER MY CAUSE IM A SCHUYLER SISTER WHO ELEVATES HIS STATUS
ID HAVE TO NAIVE TO SET THAT ASIDE, MAYBE THAT IS WHY I INTRODUCE HIM TO ELIZA
NOW THATS HIS BRIDE NICE GOING ANGELICA HE WAS RIGHT YOULL NEVER BE SATISFIED
NUMBER 3, I KNOW MY SISTER LIKE I KNOW MY OWN YOU WILL NEVER FIND ANYONE AS 
TRUSTING OR AS KIND 
"""