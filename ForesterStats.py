# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:19:46 2018

@author: Sherry
Done
"""


def CorsairStats():
    #Get base stats
    Agility = 6 + d6()
    Alertness = 8 + d6()
    Charm = 11 + d6()
    Cunning = 2 + d6()
    Dexterity = 7 + d6()
    Fate = 4 + d6()
    Intelligence = 5 + d6()
    Knowledge = 3 + d6()
    Mechanical = 9 + d6()
    Nature = 13 + d6()
    Stamina = 10 + d6()
    Strength = 12 + d6()
    
    #get speciality list started
    Specialties = ['Direction', 'Forage', 'Plants', 'Tame']
    
    #determine Age, Night Vision, Racial Benefits
    Age = Intelligence + Knowledge + 6
    Night_Vision = "No"
    Racial_Ability = "Summon Animal"
    Uses_Per_Day = 3
    
    #Get physical stats
    Height = Strength + d6()
    if Height <= 15:
        Height = "Very Short"
    elif Height <= 17:
        Height = "Short"
    elif Height <= 20:
        Height = "Average"
    elif Height <= 22:
        Height = "Tall"
    elif Height <= 24:
        Height = "Very Tall"
    Weight = Stamina + d6()
    if Weight <= 13:
        Weight = "Very Thin"
    elif Weight <= 15:
        Weight = "Thin"
    elif Weight <= 18:
        Weight = "Average"
    elif Weight <= 20:
        Weight = "Heavy"
    elif Weight <= 22:
        Weight = "Very Heavy"
        
    #get family background
    Background = Fate + d6()
    if Background == 6:
        Background = "Farmer"
        Bronze = 10
        Free = 8
        new_specs = ["Pole Arm", "Build"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 7:
        Background = "Poacher"
        Bronze = 10
        Free = 8
        new_specs = ["Track", "Bow"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 8:
        Background = "Fisher"
        Bronze = 10
        Free = 8
        new_specs = ["Boating", "Swim"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 9:
        Background = "Hunter"
        Bronze = 110
        Free = 7
        new_specs = ["Track", "Stealth"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 10:
        Background = "Trapper"
        Bronze = 110
        Free = 7
        new_specs = ["Traps", "Track"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 11:
        Background = "Logger"
        Bronze = 110
        Free = 7
        new_specs = ["Build", "Hafted"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1        
    elif Background == 12:
        Background = "Guide"
        Bronze = 210
        Free = 6
        new_specs = ["Languages", "Track"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 13:
        Background = "Tanner"
        Bronze = 210
        Free = 6
        new_specs = ["Bargain", "Business"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 14:
        Background = "Craftsman"
        Bronze = 210
        Free = 6
        new_specs = ["Build", "Repair"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 15:
        Background = "Herbalist"
        Bronze = 310
        Free = 5
        new_specs = ["Legends", "Medical"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 16:
        Background = "Innkeeper"
        Bronze = 310
        Free = 5
        new_specs = ["Business", "Customs"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1