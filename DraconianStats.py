# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:19:46 2018

@author: Sherry
Done
"""


def CorsairStats():
    #Get base stats
    Agility = 3 + d6()
    Alertness = 4 + d6()
    Charm = 2 + d6()
    Cunning = 8 + d6()
    Dexterity = 5 + d6()
    Fate = 12 + d6()
    Intelligence = 13 + d6()
    Knowledge = 9 + d6()
    Mechanical = 10 + d6()
    Nature = 6 + d6()
    Stamina = 7 + d6()
    Strength = 11 + d6()
    
    #get speciality list started
    Specialties = ['Aim', 'Arcane Lore', 'Bully', 'Literacy']
    
    #determine Age, Night Vision, Racial Benefits
    Age = Intelligence + Knowledge + -8
    Night_Vision = "No"
    Racial_Ability = "Breathe Fire"
    Uses_Per_Day = 3
    
    #Get physical stats
    Height = Strength + d6()
    if Height <= 15:
        Height = "Average"
    elif Height <= 17:
        Height = "Tall"
    elif Height <= 20:
        Height = "Very Tall"
    elif Height <= 23:
        Height = "Enormous"
    Weight = Stamina + d6()
    if Weight <= 10:
        Weight = "Very Thin"
    elif Weight <= 12:
        Weight = "Thin"
    elif Weight <= 15:
        Weight = "Average"
    elif Weight <= 17:
        Weight = "Heavy"
    elif Weight <= 19:
        Weight = "Very Heavy"
        
    #get family background
    Background = Fate + d6()
    if Background == 14:
        Background = "Farmer"
        Bronze = 10
        Free = 8
        new_specs = ["Plants", "Tame"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 15:
        Background = "Fisher"
        Bronze = 110
        Free = 7
        new_specs = ["Forage", "Swim"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 16:
        Background = "Hunter"
        Bronze = 110
        Free = 7
        new_specs = ["Bow", "Stealth"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 17:
        Background = "Herbalist"
        Bronze = 210
        Free = 6
        new_specs = ["Plants", "Poison"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 18:
        Background = "Warrior"
        Bronze = 210
        Free = 6
        new_specs = ["Sword", "Brawling"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 19:
        Background = "Craftsman"
        Bronze = 310
        Free = 5
        new_specs = ["Build", "Bargain"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1        
    elif Background == 20:
        Background = "Merchant"
        Bronze = 310
        Free = 5
        new_specs = ["Bargain", "Business"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 21:
        Background = "Slaver"
        Bronze = 410
        Free = 4
        new_specs = ["Flexible", "Customs"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 22:
        Background = "Priest"
        Bronze = 410
        Free = 4
        new_specs = ["Theology", "Legends"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 23:
        Background = "Alchemist"
        Bronze = 510
        Free = 3
        new_specs = ["Poison", "Transmute"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 24:
        Background = "Conjurer"
        Bronze = 610
        Free = 2
        new_specs = ["Conjure", "Fire Mastery"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
                    
    return [Agility, Alertness, Charm, Cunning, Dexterity, Fate, Intelligence,
    Knowledge, Mechanical, Nature, Stamina, Strength, Age, Night_Vision, Height, Weight, 
    Background, Bronze, Free, Specialties, Racial_Ability, Uses_Per_Day]