# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:18:35 2018

@author: Sherry
Done
"""

def BarbarianStats():
    #Get base stats
    Agility = 8 + d6()
    Alertness = 11 + d6()
    Charm = 5 + d6()
    Cunning = 9 + d6()
    Dexterity = 7 + d6()
    Fate = 2 + d6()
    Intelligence = 3 + d6()
    Knowledge = 6 + d6()
    Mechanical = 4 + d6()
    Nature = 10 + d6()
    Stamina = 12 + d6()
    Strength = 13 + d6()
    
    #get speciality list started
    Specialties = ['Bully', 'Climb', 'Hafted', 'Brawling']
    
    #determine Age, Night Vision, Racial Benefits
    Age = Intelligence + Knowledge + 5
    Night_Vision = "No"
    Racial_Ability = "Berserk"
    Uses_Per_Day = 4
    
    #Get physical stats
    Height = Strength + d6()
    if Height <= 15:
        Height = "Average"
    elif Height <= 20:
        Height = "Tall"
    elif Height <= 23:
        Height = "Very Tall"
    elif Height <= 24:
        Height = "Barbaria"
    elif Height == 25:
        Height = "Enormous"
    Weight = Stamina + d6()
    if Weight <= 14:
        Weight = "Thin"
    elif Weight <= 17:
        Weight = "Average"
    elif Weight <= 20:
        Weight = "Heavy"
    elif Weight <= 24:
        Weight = "Very Heavy"
        
    #get family background
    Background = Fate + d6()
    if Background == 4:
        Background = "Farmer"
        Bronze = 10
        Free = 8
        new_specs = ["Plants", "Forage"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 5:
        Background = "Herder"
        Bronze = 10
        Free = 8
        new_specs = ["Track", "Tame"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 6:
        Background = "Fisher"
        Bronze = 10
        Free = 8
        new_specs = ["Forage", "Swim"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 7:
        Background = "Trapper"
        Bronze = 110
        Free = 7
        new_specs = ["Track", "Traps"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 8:
        Background = "Hunter"
        Bronze = 110
        Free = 7
        new_specs = ["Stealth", "Run"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 9:
        Background = "Warrior"
        Bronze = 110
        Free = 7
        new_specs = ["Bow", "Flexible"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1        
    elif Background == 10:
        Background = "Story-Teller"
        Bronze = 210
        Free = 6
        new_specs = ["Entertain", "Legends"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 11:
        Background = "Weapon Maker"
        Bronze = 210
        Free = 6
        new_specs = ["Build", "Repair"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 12:
        Background = "Shaman"
        Bronze = 210
        Free = 6
        new_specs = ["Plants", "Medical"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 13:
        Background = "Councillor"
        Bronze = 310
        Free = 5
        new_specs = ["Customs", "Empathy"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 14:
        Background = "Tribal Leader"
        Bronze = 310
        Free = 5
        new_specs = ["Sword", "Preach"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1