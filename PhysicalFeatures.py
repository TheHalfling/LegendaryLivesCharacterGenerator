# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 22:50:06 2018

@author: Sherry
Physical Features

Still need to fix mixed eyes
"""
import random

def d100():
    roll = random.randint(1,100)
    return roll

def d99():
    roll = random.randint(1,99)
    return roll

def mixedEyes(roll1, roll2):
    left = eyeColor(roll1)
    right = eyeColor(roll2)
    return left, right

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
        mixedEyes(d99(), d99())
        result = "Left eye: {}".format(left), " Right eye: {}".format(right)    
    print (result)
    
eyeColor(d100())


