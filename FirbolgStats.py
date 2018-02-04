# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:19:46 2018

@author: Sherry
Done
"""


def CorsairStats():
    #Get base stats
    Agility = 5 + d6()
    Alertness = 3 + d6()
    Charm = 11 + d6()
    Cunning = 2 + d6()
    Dexterity = 6 + d6()
    Fate = 12 + d6()
    Intelligence = 10 + d6()
    Knowledge = 13 + d6()
    Mechanical = 4 + d6()
    Nature = 8 + d6()
    Stamina = 7 + d6()
    Strength = 9 + d6()
    
    #get speciality list started
    Specialties = ['Customs', 'Legends', 'Preach', 'Sincerity']
    
    #determine Age, Night Vision, Racial Benefits
    Age = Intelligence + Knowledge - 9
    Night_Vision = "Yes"
    Racial_Ability = "Far Sight"
    Uses_Per_Day = 2
    
    #Get physical stats
    Height = Strength + d6()
    if Height <= 12:
        Height = "Short"
    elif Height <= 15:
        Height = "Average"
    elif Height <= 18:
        Height = "Tall"
    elif Height <= 20:
        Height = "Very Tall"
    elif Height <= 21:
        Height = "Enormous"
    Weight = Stamina + d6()
    if Weight <= 10:
        Weight = "Very Thin"
    elif Weight <= 12:
        Weight = "Thin"
    elif Weight <= 15:
        Weight = "Average"
    elif Weight <= 17:
        Weight = "Heavy"
    elif Weight <= 19:
        Weight = "Very Heavy"
        
    #get family background
    Background = Fate + d6()
    if Background == 14:
        Background = "Snitch"
        Bronze = 10
        Free = 8
        new_specs = ["Bargain", "Contacts"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 15:
        Background = "Activist"
        Bronze = 110
        Free = 7
        new_specs = ["Literacy", "Interrogate"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 16:
        Background = "Clerk"
        Bronze = 110
        Free = 7
        new_specs = ["Memory", "Business"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 17:
        Background = "Interpreter"
        Bronze = 210
        Free = 6
        new_specs = ["Languages", "Empathy"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 18:
        Background = "Guide"
        Bronze = 210
        Free = 6
        new_specs = ["Forage", "Track"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 19:
        Background = "Constable"
        Bronze = 310
        Free = 5
        new_specs = ["Ride", "Brawling"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1        
    elif Background == 20:
        Background = "Spy"
        Bronze = 310
        Free = 5
        new_specs = ["Stealth", "Mimic"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 21:
        Background = "Lawyer"
        Bronze = 410
        Free = 4
        new_specs = ["Interrogate", "Literacy"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 22:
        Background = "Judge"
        Bronze = 410
        Free = 4
        new_specs = ["Languages", "Inuition"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 23:
        Background = "Knight"
        Bronze = 510
        Free = 3
        new_specs = ["Sword", "Ride"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 24:
        Background = "Noble"
        Bronze = 610
        Free = 2
        new_specs = ["Protection", "Literacy"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1