# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:19:46 2018

@author: Sherry
Done
"""


def CorsairStats():
    #Get base stats
    Agility = 12 + d6()
    Alertness = 7 + d6()
    Charm = 10 + d6()
    Cunning = 8 + d6()
    Dexterity = 11 + d6()
    Fate = 3 + d6()
    Intelligence = 5 + d6()
    Knowledge = 4 + d6()
    Mechanical = 13 + d6()
    Nature = 2 + d6()
    Stamina = 6 + d6()
    Strength = 9 + d6()
    
    #get speciality list started
    Specialties = ['Boating', 'Climb', 'Contacts', 'Swim']
    
    #determine Age, Night Vision, Racial Benefits
    Age = Intelligence + Knowledge + 5
    Night_Vision = "No"
    Racial_Ability = "Monkey Climb"
    Uses_Per_Day = 4
    
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
    if Weight <= 9:
        Weight = "Very Thin"
    elif Weight <= 11:
        Weight = "Thin"
    elif Weight <= 14:
        Weight = "Average"
    elif Weight <= 16:
        Weight = "Heavy"
    elif Weight <= 18:
        Weight = "Very Heavy"
        
    #get family background
    Background = Fate + d6()
    if Background == 5:
        Background = "Drunk"
        Bronze = 10
        Free = 8
        new_specs = ["Lie", "Conceal"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 6:
        Background = "Fisher"
        Bronze = 110
        Free = 7
        new_specs = ["Forage", "Quickness"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 7:
        Background = "Entertainer"
        Bronze = 110
        Free = 7
        new_specs = ["Entertain", "Disguise"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 8:
        Background = "Mercenary"
        Bronze = 110
        Free = 7
        new_specs = ["Sword", "Brawling"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 9:
        Background = "Sailor"
        Bronze = 110
        Free = 7
        new_specs = ["Bully", "Direction"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 10:
        Background = "Pirate"
        Bronze = 110
        Free = 7
        new_specs = ["Sword", "Languages"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1        
    elif Background == 11:
        Background = "Inventor"
        Bronze = 210
        Free = 6
        new_specs = ["Build", "Repair"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 12:
        Background = "Fence"
        Bronze = 210
        Free = 6
        new_specs = ["Bargain", "Lie"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 13:
        Background = "Boat Maker"
        Bronze = 210
        Free = 6
        new_specs = ["Build", "Repair"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 14:
        Background = "Merchant"
        Bronze = 310
        Free = 5
        new_specs = ["Bargain", "Business"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 15:
        Background = "Town Leader"
        Bronze = 310
        Free = 5
        new_specs = ["Customs", "Preach"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1