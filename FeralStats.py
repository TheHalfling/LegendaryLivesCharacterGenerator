# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:19:46 2018

@author: Sherry
Done
"""


def CorsairStats():
    #Get base stats
    Agility = 10 + d6()
    Alertness = 11 + d6()
    Charm = 4 + d6()
    Cunning = 7 + d6()
    Dexterity = 8 + d6()
    Fate = 6 + d6()
    Intelligence = 3 + d6()
    Knowledge = 2 + d6()
    Mechanical = 5 + d6()
    Nature = 13 + d6()
    Stamina = 12 + d6()
    Strength = 9 + d6()
    
    #get speciality list started
    Specialties = ['Intuition', 'Listen', 'Plants', 'Quickness']
    
    #determine Age, Night Vision, Racial Benefits
    Age = Intelligence + Knowledge + 9
    Night_Vision = "No"
    Racial_Ability = "Howl"
    Uses_Per_Day = 2
    
    #Get physical stats
    Height = Strength + d6()
    if Height <= 12:
        Height = "Very Short"
    elif Height <= 14:
        Height = "Short"
    elif Height <= 17:
        Height = "Average"
    elif Height <= 19:
        Height = "Tall"
    elif Height <= 21:
        Height = "Very Tall"
    Weight = Stamina + d6()
    if Weight <= 15:
        Weight = "Very Thin"
    elif Weight <= 17:
        Weight = "Thin"
    elif Weight <= 20:
        Weight = "Average"
    elif Weight <= 22:
        Weight = "Heavy"
    elif Weight <= 24:
        Weight = "Very Heavy"
        
    #get family background
    Background = Fate + d6()
    if Background == 8:
        Background = "Bush People"
        Bronze = 10
        Free = 8
        new_specs = ["Forage", "Track"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 9:
        Background = "Nethermen"
        Bronze = 10
        Free = 8
        new_specs = ["Arcane Lore", "Caves"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 10:
        Background = "Wolfling"
        Bronze = 10
        Free = 8
        new_specs = ["Track", "Direction"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 11:
        Background = "Barbarian"
        Bronze = 110
        Free = 7
        new_specs = ["Hafted", "Bully"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 12:
        Background = "Viking"
        Bronze = 110
        Free = 7
        new_specs = ["Boating", "Will"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 13:
        Background = "Gypsy"
        Bronze = 110
        Free = 7
        new_specs = ["Legends", "Arcane Lore"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1        
    elif Background == 14:
        Background = "Forester"
        Bronze = 210
        Free = 6
        new_specs = ["Forage", "Tame"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 15:
        Background = "Hill Folk"
        Bronze = 210
        Free = 6
        new_specs = ["Ride", "Wagoning"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 16:
        Background = "Firbolg"
        Bronze = 210
        Free = 6
        new_specs = ["Customs", "Preach"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 17:
        Background = "Nomad"
        Bronze = 310
        Free = 5
        new_specs = ["Languages", "Bargain"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 18:
        Background = "Easterling"
        Bronze = 310
        Free = 5
        new_specs = ["Literacy", "Legends"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1