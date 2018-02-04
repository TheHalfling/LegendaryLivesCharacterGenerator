# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:19:46 2018

@author: Sherry
Done
"""


def CorsairStats():
    #Get base stats
    Agility = 10 d6()
    Alertness = 11+ d6()
    Charm = 2 + d6()
    Cunning = 12 + d6()
    Dexterity = 13 + d6()
    Fate = 9 + d6()
    Intelligence = 7 + d6()
    Knowledge = 8 + d6()
    Mechanical = 6 + d6()
    Nature = 4 + d6()
    Stamina = 3 + d6()
    Strength = 5 + d6()
    
    #get speciality list started
    Specialties = ['Lie', 'Filch', 'Forgery', 'Search']
    
    #determine Age, Night Vision, Racial Benefits
    Age = Intelligence + Knowledge - 1
    Night_Vision = "Yes"
    Racial_Ability = "Darkness"
    Uses_Per_Day = 3
    
    #Get physical stats
    Height = Strength + d6()
    if Height <= 10:
        Height = "Tiny"
    elif Height <= 15:
        Height = "Very Short"
    elif Height <= 17:
        Height = "Short"
    Weight = Stamina + d6()
    if Weight <= 6:
        Weight = "Very Thin"
    elif Weight <= 8:
        Weight = "Thin"
    elif Weight <= 11:
        Weight = "Average"
    elif Weight <= 13:
        Weight = "Heavy"
    elif Weight <= 15:
        Weight = "Very Heavy"
        
    #get family background
    Background = Fate + d6()
    if Background == 11:
        Background = "Orphan"
        Bronze = 10
        Free = 8
        new_specs = ["Contacts", "Run"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 12:
        Background = "Drunkard"
        Bronze = 10
        Free = 8
        new_specs = ["Dodge", "Conceal"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 13:
        Background = "Beggar"
        Bronze = 10
        Free = 8
        new_specs = ["Disguise", "Empathy"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 14:
        Background = "Janitor"
        Bronze = 110
        Free = 7
        new_specs = ["Forage", "Repair"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 15:
        Background = "Cutpurse"
        Bronze = 110
        Free = 7
        new_specs = ["Run", "Quickness"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 16:
        Background = "Bandit"
        Bronze = 110
        Free = 7
        new_specs = ["Sword", "Ride"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1        
    elif Background == 17:
        Background = "Thief"
        Bronze = 210
        Free = 6
        new_specs = ["Traps", "Stealth"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 18:
        Background = "Burglar"
        Bronze = 210
        Free = 6
        new_specs = ["Stealth", "Unlock"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 19:
        Background = "Merchant"
        Bronze = 210
        Free = 6
        new_specs = ["Business", "Bargain"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 20:
        Background = "Craftsman"
        Bronze = 310
        Free = 5
        new_specs = ["Build", "Artistry"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 21:
        Background = "Sorcerer"
        Bronze = 310
        Free = 5
        new_specs = ["Arcane Lore", "Shapeshift"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1