# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:19:46 2018

@author: Sherry
Done
"""


def CorsairStats():
    #Get base stats
    Agility = 2 + d6()
    Alertness = 5 + d6()
    Charm = 9 + d6()
    Cunning = 11 + d6()
    Dexterity = 8 + d6()
    Fate = 7 + d6()
    Intelligence = 10 + d6()
    Knowledge = 12 + d6()
    Mechanical = 3 + d6()
    Nature = 4 + d6()
    Stamina = 13 + d6()
    Strength = 6 + d6()
    
    #get speciality list started
    Specialties = ['Bargain', 'Filch', 'Languages', 'Ride']
    
    #determine Age, Night Vision, Racial Benefits
    Age = Intelligence + Knowledge - 8
    Night_Vision = "No"
    Racial_Ability = "Adaptation"
    Uses_Per_Day = 2
    
    #Get physical stats
    Height = Strength + d6()
    if Height <= 9:
        Height = "Very Short"
    elif Height <= 11:
        Height = "Short"
    elif Height <= 14:
        Height = "Average"
    elif Height <= 16:
        Height = "Tall"
    elif Height <= 18:
        Height = "Very Tall"
    
    Weight = Stamina + d6()
    if Weight <= 16:
        Weight = "Very Thin"
    elif Weight <= 18:
        Weight = "Thin"
    elif Weight <= 21:
        Weight = "Average"
    elif Weight <= 23:
        Weight = "Heavy"
    elif Weight <= 25:
        Weight = "Very Heavy"
        
    #get family background
    Background = Fate + d6()
    if Background == 9:
        Background = "Outcast"
        Bronze = 10
        Free = 8
        new_specs = ["Dodge", "Stealth"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 10:
        Background = "Begger"
        Bronze = 110
        Free = 7
        new_specs = ["Lie", "Disguise"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 11:
        Background = "Thief"
        Bronze = 110
        Free = 7
        new_specs = ["Unlock", "Traps"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 12:
        Background = "Entertainer"
        Bronze = 210
        Free = 6
        new_specs = ["Entertain", "Mimic"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 13:
        Background = "Horse Trainer"
        Bronze = 210
        Free = 6
        new_specs = ["Tame", "Intuition"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 14:
        Background = "Trader"
        Bronze = 310
        Free = 5
        new_specs = ["Lie", "Customs"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1        
    elif Background == 15:
        Background = "Merchant"
        Bronze = 310
        Free = 5
        new_specs = ["Business", "Lie"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 16:
        Background = "Slaver"
        Bronze = 410
        Free = 4
        new_specs = ["Bully", "Flexible"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 17:
        Background = "Importer"
        Bronze = 410
        Free = 4
        new_specs = ["Customs", "Business"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 18:
        Background = "Caravan Owner"
        Bronze = 510
        Free = 3
        new_specs = ["Tame", "Business"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 19:
        Background = "High Priest"
        Bronze = 610
        Free = 2
        new_specs = ["Theology", "Literacy"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1