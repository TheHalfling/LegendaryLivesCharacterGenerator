# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:19:46 2018

@author: Sherry
Done
"""


def CorsairStats():
    #Get base stats
    Agility = 6 + d6()
    Alertness = 2 + d6()
    Charm = 7 + d6()
    Cunning = 9 + d6()
    Dexterity = 10 + d6()
    Fate = 13 + d6()
    Intelligence = 4 + d6()
    Knowledge = 12 + d6()
    Mechanical = 3 + d6()
    Nature = 11 + d6()
    Stamina = 5 + d6()
    Strength = 8 + d6()
    
    #get speciality list started
    Specialties = ['Arcane Lore', 'Caves', 'Inuition', 'Tame']
    
    #determine Age, Night Vision, Racial Benefits
    Age = Intelligence + Knowledge - 2
    Night_Vision = "Yes"
    Racial_Ability = "Speak with Animals"
    Uses_Per_Day = 4
    
    #Get physical stats
    Height = Strength + d6()
    if Height <= 11:
        Height = "Very Short"
    elif Height <= 13:
        Height = "Short"
    elif Height <= 16:
        Height = "Average"
    elif Height <= 18:
        Height = "Tall"
    elif Height <= 20:
        Height = "Very Tall"
    
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
    if Background == 15:
        Background = "Gatherer"
        Bronze = 10
        Free = 8
        new_specs = ["Direction", "Forage"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 16:
        Background = "Farmer"
        Bronze = 10
        Free = 8
        new_specs = ["Plants", "Forage"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 17:
        Background = "Weaver"
        Bronze = 10
        Free = 8
        new_specs = ["Bargain", "Quickness"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 18:
        Background = "Potter Maker"
        Bronze = 110
        Free = 7
        new_specs = ["Build", "Business"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 19:
        Background = "Fisher"
        Bronze = 110
        Free = 7
        new_specs = ["Swim", "Forage"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 20:
        Background = "Hunter"
        Bronze = 110
        Free = 7
        new_specs = ["Forage", "Bow"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1        
    elif Background == 21:
        Background = "Warrior"
        Bronze = 210
        Free = 6
        new_specs = ["Pole Arm", "Bow"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 22:
        Background = "Canoe Maker"
        Bronze = 210
        Free = 6
        new_specs = ["Build", "Boating"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 23:
        Background = "Toolmaker"
        Bronze = 210
        Free = 6
        new_specs = ["Build", "Repair"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 24:
        Background = "Shaman"
        Bronze = 310
        Free = 5
        new_specs = ["Will", "Heal"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 25:
        Background = "Chieftan"
        Bronze = 310
        Free = 5
        new_specs = ["Legends", "Shapeshift"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1