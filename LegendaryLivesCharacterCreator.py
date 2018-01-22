# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

#roll a d6
def d6():
    roll = random.randint(1,6)
    return roll

#roll a d10
def d10():
    roll = random.randint(1,10)
    return roll

#roll a d100
def d100():
    roll = random.randint(1,100)
    return roll

#randomally determine character race
def getRace():
    roll = d100()
    if roll <= 4:
        race = 'Avian'
    elif roll <= 8:
        race = 'Barbarian'
    elif roll <= 12:
        race = 'Brownie'
    elif roll <= 15:
        race = 'Bush Person'
    elif roll <= 19:
        race = 'Carsair'
    elif roll <= 23:
        race = 'Draconian'
    elif roll <= 27:
        race = 'Dwarf'
    elif roll <= 31:
        race = 'Easterling'
    elif roll <= 35:
        race = 'Elf'
    elif roll <= 38:
        race = 'Elfin'
    elif roll <= 42:
        race = 'Entomolian'
    elif roll <= 46:
        race = 'Feral'
    elif roll <= 50:
        race = 'Firbolg'
    elif roll <= 54:
        race = 'Forester'
    elif roll <= 58:
        race = 'Goblin'
    elif roll <= 62:
        race = 'Gypsy'
    elif roll <= 65:
        race = 'Hill Folk'
    elif roll <= 69:
        race = 'Hob'
    elif roll <= 73:
        race = 'Netherman'
    elif roll <= 77:
        race = 'Nomad'
    elif roll <= 81:
        race = 'Ratling'
    elif roll <= 85:
        race = 'Serpentine'
    elif roll <= 88:
        race = 'Sidhe'
    elif roll <= 92:
        race = 'Spriggan'
    elif roll <= 96:
        race = 'Viking'
    elif roll <= 100:
        race = 'Wolfling'
    return race






                 
#print out results to be transferred to character sheet
print ("Your race is {}".format(getRace()) )
print("Agility: {}".format(Agility))
print("Alertness: {}".format(Alertness))
print("Charm: {}".format(Charm))
print("Cunning: {}".format(Cunning))
print("Dexterity: {}".format(Dexterity))
print("Fate: {}".format(Fate))
print("Intelligence: {}".format(Intelligence))
print("Knowledge: {}".format(Knlowedge))
print("Mechanical: {}".format(Mecahnical))
print("Nature: {}".format(Nature))
print("Stamina: {}".format(Stamina))
print("Strength: {}".format(Strength))
    

