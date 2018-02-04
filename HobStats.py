# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:19:46 2018

@author: Sherry
Done
"""


def CorsairStats():
    #Get base stats
    Agility = 7 + d6()
    Alertness = 5 + d6()
    Charm = 3 + d6()
    Cunning = 11 + d6()
    Dexterity = 9 + d6()
    Fate = 6 + d6()
    Intelligence = 2 + d6()
    Knowledge = 4 + d6()
    Mechanical = 10 + d6()
    Nature = 8 + d6()
    Stamina = 13 + d6()
    Strength = 12 + d6()
    
    #get speciality list started
    Specialties = ['Bully', 'Contacts', 'Flexible', 'Lie']
    
    #determine Age, Night Vision, Racial Benefits
    Age = Intelligence + Knowledge + 8
    Night_Vision = "Yes"
    Racial_Ability = "Revulsion"
    Uses_Per_Day = 3
    
    #Get physical stats
    Height = Strength + d6()
    if Height <= 16:
        Height = "Average"
    elif Height <= 18:
        Height = "Tall"
    elif Height <= 21:
        Height = "Very Tall"
    elif Height <= 25:
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
    if Background == 8:
        Background = "Slave"
        Bronze = 10
        Free = 8
        new_specs = ["Dodge", "Run"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 9:
        Background = "Servant"
        Bronze = 10
        Free = 8
        new_specs = ["Sincerity", "Conceal"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 10:
        Background = "Outlaw"
        Bronze = 10
        Free = 8
        new_specs = ["Stealth", "Ride"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 11:
        Background = "Miner"
        Bronze = 110
        Free = 7
        new_specs = ["Caves", "Search"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 12:
        Background = "Laborer"
        Bronze = 110
        Free = 7
        new_specs = ["Build", "Seige"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 13:
        Background = "Bouncer"
        Bronze = 110
        Free = 7
        new_specs = ["Hafted", "Intuition"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1        
    elif Background == 14:
        Background = "Bodyguard"
        Bronze = 210
        Free = 6
        new_specs = ["Quickness", "Brawling"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 15:
        Background = "Militia"
        Bronze = 210
        Free = 6
        new_specs = ["Pole Arm", "Customs"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 16:
        Background = "Guard"
        Bronze = 210
        Free = 6
        new_specs = ["Sword", "Brawling"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 17:
        Background = "Mercenary"
        Bronze = 310
        Free = 5
        new_specs = ["Sword", "Languages"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 18:
        Background = "Assassin"
        Bronze = 310
        Free = 5
        new_specs = ["Stealth", "Aim"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1