# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:19:46 2018

@author: Sherry
Done
"""


def CorsairStats():
    #Get base stats
    Agility = 13 + d6()
    Alertness = 11 + d6()
    Charm = 7 + d6()
    Cunning = 4 + d6()
    Dexterity = 10 + d6()
    Fate = 5 + d6()
    Intelligence = 12 + d6()
    Knowledge = 8 + d6()
    Mechanical = 9 + d6()
    Nature = 2 + d6()
    Stamina = 3 + d6()
    Strength = 6 + d6()
    
    #get speciality list started
    Specialties = ['Empathy', 'Memory', 'Jump', 'Stealth']
    
    #determine Age, Night Vision, Racial Benefits
    Age = Intelligence + Knowledge - 6
    Night_Vision = "No"
    Racial_Ability = "True Sight"
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
    if Weight <= 6:
        Weight = "Very Thin"
    elif Weight <= 8:
        Weight = "Thin"
    elif Weight <= 11:
        Weight = "Average"
    elif Weight <= 13:
        Weight = "Heavy"
    elif Weight <= 15:
        Weight = "Very Heavy"
        
    #get family background
    Background = Fate + d6()
    if Background == 7:
        Background = "Beggar"
        Bronze = 10
        Free = 8
        new_specs = ["Sincerity", "Lie"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 8:
        Background = "Hermit"
        Bronze = 10
        Free = 8
        new_specs = ["Forage", "Caves"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 9:
        Background = "Criminal"
        Bronze = 10
        Free = 8
        new_specs = ["Filch", "Contacts"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 10:
        Background = "Laborer"
        Bronze = 110
        Free = 7
        new_specs = ["Will", "Build"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 11:
        Background = "Clerk"
        Bronze = 110
        Free = 7
        new_specs = ["Customs", "Literacy"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 12:
        Background = "Merchant"
        Bronze = 110
        Free = 7
        new_specs = ["Business", "Bargain"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1        
    elif Background == 13:
        Background = "Scribe"
        Bronze = 210
        Free = 6
        new_specs = ["Literacy", "Legends"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 14:
        Background = "Craftsman"
        Bronze = 210
        Free = 6
        new_specs = ["Build", "Repair"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 15:
        Background = "Philosopher"
        Bronze = 210
        Free = 6
        new_specs = ["Theology", "Preach"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 16:
        Background = "Artist"
        Bronze = 310
        Free = 5
        new_specs = ["Intuition", "Artistry"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 17:
        Background = "Sage"
        Bronze = 310
        Free = 5
        new_specs = ["Memory", "Legends"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1