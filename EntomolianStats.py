# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:19:46 2018

@author: Sherry
Done
"""


def CorsairStats():
    #Get base stats
    Agility = 12 + d6()
    Alertness = 8 + d6()
    Charm = 2 + d6()
    Cunning = 3 + d6()
    Dexterity = 4 + d6()
    Fate = 6 + d6()
    Intelligence = 9 + d6()
    Knowledge = 5 + d6()
    Mechanical = 10 + d6()
    Nature = 7 + d6()
    Stamina = 11 + d6()
    Strength = 13 + d6()
    
    #get speciality list started
    Specialties = ['Dodge', 'Jump', 'Sword', 'Will']
    
    #determine Age, Night Vision, Racial Benefits
    Age = Intelligence + Knowledge
    Night_Vision = "No"
    Racial_Ability = "Leaping"
    Uses_Per_Day = 4
    
    #Get physical stats
    Height = Strength + d6()
    if Height <= 17:
        Height = "Average"
    elif Height <= 19:
        Height = "Tall"
    elif Height <= 22:
        Height = "Very Tall"
    elif Height <= 25:
        Height = "Enormous"
    Weight = Stamina + d6()
    if Weight <= 14:
        Weight = "Very Thin"
    elif Weight <= 16:
        Weight = "Thin"
    elif Weight <= 19:
        Weight = "Average"
    elif Weight <= 21:
        Weight = "Heavy"
    elif Weight <= 23:
        Weight = "Very Heavy"
        
    #get family background
    Background = Fate + d6()
    if Background == 8:
        Background = "Tunneler"
        Bronze = 10
        Free = 8
        new_specs = ["Caves", "Siege"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 9:
        Background = "Worker"
        Bronze = 10
        Free = 8
        new_specs = ["Repair", "Mimic"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 10:
        Background = "Gatherer"
        Bronze = 10
        Free = 8
        new_specs = ["Forage", "Direction"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 11:
        Background = "Herder"
        Bronze = 110
        Free = 7
        new_specs = ["Tame", "Quickness"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 12:
        Background = "Hunter"
        Bronze = 110
        Free = 7
        new_specs = ["Crossbow", "Track"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 13:
        Background = "Soldier"
        Bronze = 110
        Free = 7
        new_specs = ["Aim", "Run"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1        
    elif Background == 14:
        Background = "Scout"
        Bronze = 210
        Free = 6
        new_specs = ["Track", "Stealth"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 15:
        Background = "Slaver"
        Bronze = 210
        Free = 6
        new_specs = ["Bully", "Bargain"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 16:
        Background = "Toolmaker"
        Bronze = 210
        Free = 6
        new_specs = ["Traps", "Repair"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 17:
        Background = "Guard"
        Bronze = 310
        Free = 5
        new_specs = ["Crossbow", "Bully"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 18:
        Background = "Nursemaid"
        Bronze = 310
        Free = 5
        new_specs = ["Will", "Medical"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1