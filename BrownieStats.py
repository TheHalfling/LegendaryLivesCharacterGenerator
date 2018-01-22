# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:19:10 2018

@author: Sherry
Done
"""

def BrownieStats():
    #Get base stats
    Agility = 9 + d6()
    Alertness = 12 + d6()
    Charm = 13 + d6()
    Cunning = 11 + d6()
    Dexterity = 4 + d6()
    Fate = 7 + d6()
    Intelligence = 6 + d6()
    Knowledge = 5 + d6()
    Mechanical = 10 + d6()
    Nature = 8 + d6()
    Stamina = 3 + d6()
    Strength = 2 + d6()
    
    #get speciality list started
    Specialties = ['Conceal', 'Entertain', 'Listen', 'Sincerity']
    
    #determine Age, Night Vision, Racial Benefits
    Age = Intelligence + Knowledge + 3
    Night_Vision = "No"
    Racial_Ability = "Friends"
    Uses_Per_Day = 3
    
    #Get physical stats
    Height = Strength + d6()
    if Height <= 9:
        Height = "Tiny"
    elif Height <= 13:
        Height = "Very Short"
    elif Height <= 14:
        Height = "Short"
    Weight = Stamina + d6()
    if Weight <= 5:
        Weight = "Thin"
    elif Weight <= 8:
        Weight = "Average"
    elif Weight <= 11:
        Weight = "Heavy"
    elif Weight <= 15:
        Weight = "Very Heavy"
        
    #get family background
    Background = Fate + d6()
    if Background == 9:
        Background = "Pet"
        Bronze = 10
        Free = 8
        new_specs = ["Filch", "Intuition"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 10:
        Background = "Servant"
        Bronze = 10
        Free = 8
        new_specs = ["Lie", "Run"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 11:
        Background = "Cook"
        Bronze = 10
        Free = 8
        new_specs = ["Poison", "Business"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 12:
        Background = "Farmer"
        Bronze = 110
        Free = 7
        new_specs = ["Plants", "Forage"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 13:
        Background = "Herder"
        Bronze = 110
        Free = 7
        new_specs = ["Tame", "Ride"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 14:
        Background = "Entertainer"
        Bronze = 110
        Free = 7
        new_specs = ["Disguise", "Mimic"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1        
    elif Background == 15:
        Background = "Gardener"
        Bronze = 210
        Free = 6
        new_specs = ["Plants", "Poison"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 16:
        Background = "Craftsman"
        Bronze = 210
        Free = 6
        new_specs = ["Build", "Artistry"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 17:
        Background = "Guildsman"
        Bronze = 210
        Free = 6
        new_specs = ["Business", "Repair"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 18:
        Background = "Merchant"
        Bronze = 310
        Free = 5
        new_specs = ["Business", "Bargain"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 19:
        Background = "Mayor"
        Bronze = 310
        Free = 5
        new_specs = ["Customs", "Preach"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1