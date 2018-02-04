# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:19:46 2018

@author: Sherry
Done
"""


def CorsairStats():
    #Get base stats
    Agility = 11 + d6()
    Alertness = 13 + d6()
    Charm = 5 + d6()
    Cunning = 4 + d6()
    Dexterity = 3 + d6()
    Fate = 2 + d6()
    Intelligence = 8 + d6()
    Knowledge = 7 + d6()
    Mechanical = 6 + d6()
    Nature = 12 + d6()
    Stamina = 9 + d6()
    Strength = 10 + d6()
    
    #get speciality list started
    Specialties = ['Direction', 'Forage', 'Search', 'Track']
    
    #determine Age, Night Vision, Racial Benefits
    Age = Intelligence + Knowledge - 1
    Night_Vision = "No"
    Racial_Ability = "Transform"
    Uses_Per_Day = 2
    
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
    if Background == 4:
        Background = "Vagrant"
        Bronze = 10
        Free = 8
        new_specs = ["Lie", "Languages"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 5:
        Background = "Outlaw"
        Bronze = 10
        Free = 8
        new_specs = ["Bully", "Sword"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 6:
        Background = "Herder"
        Bronze = 10
        Free = 8
        new_specs = ["Tame", "Ride"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 7:
        Background = "Hunter"
        Bronze = 110
        Free = 7
        new_specs = ["Stealth", "Bow"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 8:
        Background = "Tanner"
        Bronze = 110
        Free = 7
        new_specs = ["Business", "Bargain"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 9:
        Background = "Woodcutter"
        Bronze = 110
        Free = 7
        new_specs = ["Climb", "Hafted"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1        
    elif Background == 10:
        Background = "Trapper"
        Bronze = 210
        Free = 6
        new_specs = ["Traps", "Stealth"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 11:
        Background = "Stonemason"
        Bronze = 210
        Free = 6
        new_specs = ["Build", "Business"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 12:
        Background = "Poacher"
        Bronze = 210
        Free = 6
        new_specs = ["Crossbow", "Stealth"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 13:
        Background = "Guide"
        Bronze = 310
        Free = 5
        new_specs = ["Languages", "Bargain"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 14:
        Background = "Mercenary"
        Bronze = 310
        Free = 5
        new_specs = ["Sword", "Ride"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
                    
    return [Agility, Alertness, Charm, Cunning, Dexterity, Fate, Intelligence,
    Knowledge, Mechanical, Nature, Stamina, Strength, Age, Night_Vision, Height, Weight, 
    Background, Bronze, Free, Specialties, Racial_Ability, Uses_Per_Day]