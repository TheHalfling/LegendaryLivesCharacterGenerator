# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 22:50:06 2018

@author: Sherry
Physical Features

Still need to fix mixed eyes
"""
import diceRolls



def eyeColor(roll):
    if roll <= 10:
        result = "Light blue"
    elif roll <= 20:
        result = "Black"
    elif roll <= 30:
        result = "Gray"
    elif roll <= 40:
        result = "Green"
    elif roll <= 50:
        result = "Hazel"
    elif roll <= 60:
        result = "Violet"
    elif roll <= 70:
        result = "Dark blue"
    elif roll <= 80:
        result = "Dark brown"
    elif roll <= 97:
        result = "Amber"
    elif roll == 98:
        result = "Silver"
    elif roll == 99:
        result = "Golden"
    elif roll == 100:
        result = "Left eye: {}".format(LEFT), " Right eye: {}".format(RIGHT)    
    return result

LEFT = eyeColor(diceRolls.d99())
RIGHT = eyeColor(diceRolls.d99())
 
print (eyeColor(diceRolls.d100()))


