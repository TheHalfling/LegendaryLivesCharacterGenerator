# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:19:46 2018

@author: Sherry
Done
"""


def BushPersonStats():
    #Get base stats
    Agility = 13 + d6()
    Alertness = 12 + d6()
    Charm = 6 + d6()
    Cunning = 4 + d6()
    Dexterity = 8 + d6()
    Fate = 7 + d6()
    Intelligence = 2 + d6()
    Knowledge = 5 + d6()
    Mechanical = 3 + d6()
    Nature = 11 + d6()
    Stamina = 9 + d6()
    Strength = 10 + d6()
    
    #get speciality list started
    Specialties = ['Forage', 'Plants', 'Stealth', 'Track']
    
    #determine Age, Night Vision, Racial Benefits
    Age = Intelligence + Knowledge + 7
    Night_Vision = "No"
    Racial_Ability = "Animal Vision"
    Uses_Per_Day = 4
    
    #Get physical stats
    Height = Strength + d6()
    if Height <= 13:
        Height = "Short"
    elif Height <= 16:
        Height = "Average"
    elif Height <= 19:
        Height = "Tall"
    elif Height <= 21:
        Height = "Very Tall"
    elif Height <= 22:
        Height = "Enormous"
    Weight = Stamina + d6()
    if Weight <= 12:
        Weight = "Very Thin"
    elif Weight <= 14:
        Weight = "Thin"
    elif Weight <= 17:
        Weight = "Average"
    elif Weight <= 19:
        Weight = "Heavy"
    elif Weight <= 21:
        Weight = "Very Heavy"
        
    #get family background
    Background = Fate + d6()
    if Background == 9:
        Background = "Gatherer"
        Bronze = 10
        Free = 8
        new_specs = ["Direction", "Search"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 10:
        Background = "Weaver"
        Bronze = 10
        Free = 8
        new_specs = ["Build", "Bargain"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 11:
        Background = "Herder"
        Bronze = 10
        Free = 8
        new_specs = ["Tame", "Ride"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 12:
        Background = "Fisher"
        Bronze = 110
        Free = 7
        new_specs = ["Boating", "Swim"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 13:
        Background = "Warrior"
        Bronze = 110
        Free = 7
        new_specs = ["Pole Arm", "Bow"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 14:
        Background = "Hunter"
        Bronze = 110
        Free = 7
        new_specs = ["Bow", "Run"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1        
    elif Background == 15:
        Background = "Leather Worker"
        Bronze = 210
        Free = 6
        new_specs = ["Build", "Will"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 16:
        Background = "Guide"
        Bronze = 210
        Free = 6
        new_specs = ["Direction", "Languages"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 17:
        Background = "Toolmaker"
        Bronze = 210
        Free = 6
        new_specs = ["Build", "Repair"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 18:
        Background = "Shaman"
        Bronze = 310
        Free = 5
        new_specs = ["Preach", "Legends"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 19:
        Background = "Tribal Leader"
        Bronze = 310
        Free = 5
        new_specs = ["Plant Mastery", "Bully"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1