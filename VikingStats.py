# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:19:46 2018

@author: Sherry
Done
"""


def CorsairStats():
    #Get base stats
    Agility = 3 + d6()
    Alertness = 2 + d6()
    Charm = 6 + d6()
    Cunning = 7 + d6()
    Dexterity = 9 + d6()
    Fate = 5 + d6()
    Intelligence = 8 + d6()
    Knowledge = 10 + d6()
    Mechanical = 12 + d6()
    Nature = 4 + d6()
    Stamina = 13 + d6()
    Strength = 11 + d6()
    
    #get speciality list started
    Specialties = ['Boating', 'Hafted', 'Swim', 'Will']
    
    #determine Age, Night Vision, Racial Benefits
    Age = Intelligence + Knowledge - 4
    Night_Vision = "No"
    Racial_Ability = "Fear"
    Uses_Per_Day = 4
    
    #Get physical stats
    Height = Strength + d6()
    if Height <= 15:
        Height = "Average"
    elif Height <= 18:
        Height = "Tall"
    elif Height <= 21:
        Height = "Very Tall"
    elif Height <= 23:
        Height = "Enormous"
        
    Weight = Stamina + d6()
    if Weight <= 15:
        Weight = "Thin"
    elif Weight <= 18:
        Weight = "Average"
    elif Weight <= 21:
        Weight = "Heavy"
    elif Weight <= 25:
        Weight = "Very Heavy"
        
    #get family background
    Background = Fate + d6()
    if Background == 7:
        Background = "Drunk"
        Bronze = 10
        Free = 8
        new_specs = ["Lie", "Conceal"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 8:
        Background = "Story-Teller"
        Bronze = 110
        Free = 7
        new_specs = ["Legends", "Entertain"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 9:
        Background = "Hunter"
        Bronze = 110
        Free = 7
        new_specs = ["Stealth", "Track"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 10:
        Background = "Trapper"
        Bronze = 210
        Free = 6
        new_specs = ["Track", "Traps"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 11:
        Background = "Fisher"
        Bronze = 210
        Free = 6
        new_specs = ["Forage", "Flexible"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 12:
        Background = "Warrior"
        Bronze = 310
        Free = 5
        new_specs = ["Brawling", "Medical"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1        
    elif Background == 13:
        Background = "Raider"
        Bronze = 310
        Free = 5
        new_specs = ["Bully", "Brawling"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 14:
        Background = "Weapon Maker"
        Bronze = 410
        Free = 4
        new_specs = ["Bargain", "Build"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 15:
        Background = "Leather Worker"
        Bronze = 410
        Free = 4
        new_specs = ["Business", "Bargain"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 16:
        Background = "Ship Builder"
        Bronze = 510
        Free = 3
        new_specs = ["Build", "Repair"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 17:
        Background = "Lawmaker"
        Bronze = 610
        Free = 2
        new_specs = ["Sanity", "Literacy"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1