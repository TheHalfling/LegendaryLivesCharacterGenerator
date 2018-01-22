# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:19:46 2018

@author: Sherry
Done
"""


def CorsairStats():
    #Get base stats
    Agility = 2 + d6()
    Alertness = 6 + d6()
    Charm = 5 + d6()
    Cunning = 7 + d6()
    Dexterity = 9 + d6()
    Fate = 3 + d6()
    Intelligence = 11 + d6()
    Knowledge = 10 + d6()
    Mechanical = 13 + d6()
    Nature = 4 + d6()
    Stamina = 12 + d6()
    Strength = 8 + d6()
    
    #get speciality list started
    Specialties = ['Business', 'Caves', 'Hafted', 'Repair']
    
    #determine Age, Night Vision, Racial Benefits
    Age = Intelligence + Knowledge -7
    Night_Vision = "Yes"
    Racial_Ability = "Smell Treasure"
    Uses_Per_Day = 4
    
    #Get physical stats
    Height = Strength + d6()
    if Height <= 12:
        Height = "Tiny"
    elif Height <= 17:
        Height = "Very Short"
    elif Height <= 20:
        Height = "Short"

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
    if Background == 5:
        Background = "Derelict"
        Bronze = 10
        Free = 8
        new_specs = ["Contacts", "Lie"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 6:
        Background = "Laborer"
        Bronze = 110
        Free = 7
        new_specs = ["Will", "Filch"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 7:
        Background = "Foreman"
        Bronze = 110
        Free = 7
        new_specs = ["Build", "Bully"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 8:
        Background = "Tinker"
        Bronze = 210
        Free = 6
        new_specs = ["Build", "Bargain"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 9:
        Background = "Craftsman"
        Bronze = 210
        Free = 6
        new_specs = ["Build", "Artistry"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 10:
        Background = "Merchant"
        Bronze = 310
        Free = 5
        new_specs = ["Bargain", "Customs"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1        
    elif Background == 11:
        Background = "Constable"
        Bronze = 310
        Free = 5
        new_specs = ["Customs", "Brawling"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 12:
        Background = "Engineer"
        Bronze = 410
        Free = 4
        new_specs = ["Build", "Siege"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 13:
        Background = "Banker"
        Bronze = 410
        Free = 4
        new_specs = ["Business", "Customs"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 14:
        Background = "Gentry"
        Bronze = 510
        Free = 3
        new_specs = ["Customs", "Literacy"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 15:
        Background = "Noble"
        Bronze = 610
        Free = 2
        new_specs = ["Bargain", "Earth Mastery"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1