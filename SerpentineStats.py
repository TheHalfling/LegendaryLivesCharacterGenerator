# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:19:46 2018

@author: Sherry
Done
"""


def CorsairStats():
    #Get base stats
    Agility = 8 + d6()
    Alertness = 5 + d6()
    Charm = 12 + d6()
    Cunning = 13 + d6()
    Dexterity = 2 + d6()
    Fate = 9 + d6()
    Intelligence = 10 + d6()
    Knowledge = 7 + d6()
    Mechanical = 11 + d6()
    Nature = 4 + d6()
    Stamina = 3 + d6()
    Strength = 6 + d6()
    
    #get speciality list started
    Specialties = ['Bargain', 'Business', 'Contacts', 'Lie']
    
    #determine Age, Night Vision, Racial Benefits
    Age = Intelligence + Knowledge - 3
    Night_Vision = "No"
    Racial_Ability = "Hypnotize"
    Uses_Per_Day = 2
    
    #Get physical stats
    Height = Strength + d6()
    if Height <= 19:
        Height = "Short"
    elif Height <= 12:
        Height = "Average"
    elif Height <= 15:
        Height = "Tall"
    elif Height <= 17:
        Height = "Very Tall"
    elif Height <= 18:
        Height = "Enormous:
            
    Weight = Stamina + d6()
    if Weight <= 8:
        Weight = "Very Thin"
    elif Weight <= 11:
        Weight = "Thin"
    elif Weight <= 14:
        Weight = "Average"
    elif Weight <= 15:
        Weight = "Heavy"
        
    #get family background
    Background = Fate + d6()
    if Background == 11:
        Background = "Servant"
        Bronze = 10
        Free = 8
        new_specs = ["Sincerity", "Quickness"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 12:
        Background = "Sycophant"
        Bronze = 110
        Free = 7
        new_specs = ["Sincerity", "Empathy"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 13:
        Background = "Thief"
        Bronze = 110
        Free = 7
        new_specs = ["Filch", "Unlock"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 14:
        Background = "Innkeeper"
        Bronze = 210
        Free = 6
        new_specs = ["Poison", "Languages"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 15:
        Background = "Shopkeeper"
        Bronze = 210
        Free = 6
        new_specs = ["Customs", "Empathy"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 16:
        Background = "Salesman"
        Bronze = 310
        Free = 5
        new_specs = ["Filch", "Sincerity"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1        
    elif Background == 17:
        Background = "Merchant"
        Bronze = 310
        Free = 5
        new_specs = ["Customs", "Languages"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 18:
        Background = "Councilor"
        Bronze = 410
        Free = 4
        new_specs = ["Intuition", "Forgery"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 19:
        Background = "Noble"
        Bronze = 410
        Free = 4
        new_specs = ["Literacy", "Interrogate"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 20:
        Background = "Gang Lord"
        Bronze = 510
        Free = 3
        new_specs = ["Interrogate", "Preach"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 21:
        Background = "Enchanter"
        Bronze = 610
        Free = 2
        new_specs = ["Arcane Lore", "Enchant"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1