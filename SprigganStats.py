# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:19:46 2018

@author: Sherry
Done
"""


def CorsairStats():
    #Get base stats
    Agility = 7 + d6()
    Alertness = 3 + d6()
    Charm = 2 + d6()
    Cunning = 12 + d6()
    Dexterity = 13 + d6()
    Fate = 4 + d6()
    Intelligence = 10 + d6()
    Knowledge = 9 + d6()
    Mechanical = 11 + d6()
    Nature = 8 + d6()
    Stamina = 5 + d6()
    Strength = 6 + d6()
    
    #get speciality list started
    Specialties = ['Conceal', 'Filch', 'Forgery', 'Unlock']
    
    #determine Age, Night Vision, Racial Benefits
    Age = Intelligence + Knowledge - 5
    Night_Vision = "No"
    Racial_Ability = "Growth"
    Uses_Per_Day = 2
    
    #Get physical stats
    Height = Strength + d6()
    if Height <= 9:
        Height = "Tiny"
    elif Height <= 13:
        Height = "Very Short"
    elif Height <= 17:
        Height = "Short"
    elif Height <= 18:
        Height = "Average"
    
    Weight = Stamina + d6()
    if Weight <= 8:
        Weight = "Very Thin"
    elif Weight <= 10:
        Weight = "Thin"
    elif Weight <= 13:
        Weight = "Average"
    elif Weight <= 15:
        Weight = "Heavy"
    elif Weight <= 17:
        Weight = "Very Heavy"
        
    #get family background
    Background = Fate + d6()
    if Background == 6:
        Background = "Derelict"
        Bronze = 10
        Free = 8
        new_specs = ["Lie", "Search"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 7:
        Background = "Serf"
        Bronze = 10
        Free = 8
        new_specs = ["Plants", "Forage"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 8:
        Background = "Herder"
        Bronze = 10
        Free = 8
        new_specs = ["Tame", "Direction"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 9:
        Background = "Gatherer"
        Bronze = 110
        Free = 7
        new_specs = ["Plants", "Forage"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 10:
        Background = "Hunter"
        Bronze = 110
        Free = 7
        new_specs = ["Forage", "Track"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 11:
        Background = "Robber"
        Bronze = 110
        Free = 7
        new_specs = ["Sword", "Bully"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1        
    elif Background == 12:
        Background = "Counterfeiter"
        Bronze = 210
        Free = 6
        new_specs = ["Contacts", "Literacy"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 13:
        Background = "Burglar"
        Bronze = 210
        Free = 6
        new_specs = ["Unlock", "Stealth"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 14:
        Background = "Story-Teller"
        Bronze = 210
        Free = 6
        new_specs = ["Legends", "Entertain"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 15:
        Background = "Toolmaker"
        Bronze = 310
        Free = 5
        new_specs = ["Build", "Bargain"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 16:
        Background = "Healer"
        Bronze = 310
        Free = 5
        new_specs = ["Plants", "Medical"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1