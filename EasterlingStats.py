# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:19:46 2018

@author: Sherry
Done
"""


def CorsairStats():
    #Get base stats
    Agility = 5 + d6()
    Alertness = 7 + d6()
    Charm = 8 + d6()
    Cunning = 10 + d6()
    Dexterity = 6 + d6()
    Fate = 11 + d6()
    Intelligence = 13 + d6()
    Knowledge = 12 + d6()
    Mechanical = 9 + d6()
    Nature = 2 + d6()
    Stamina = 4 + d6()
    Strength = 3 + d6()
    
    #get speciality list started
    Specialties = ['Legends', 'Literacy', 'Poison', 'Theology']
    
    #determine Age, Night Vision, Racial Benefits
    Age = Intelligence + Knowledge -11
    Night_Vision = "No"
    Racial_Ability = "Psychometry"
    Uses_Per_Day = 2
    
    #Get physical stats
    Height = Strength + d6()
    if Height <= 6:
        Height = "Very Short"
    elif Height <= 9:
        Height = "Short"
    elif Height <= 12:
        Height = "Average"
    elif Height <= 15:
        Height = "Tall"

    Weight = Stamina + d6()
    if Weight <= 7:
        Weight = "Very Thin"
    elif Weight <= 9:
        Weight = "Thin"
    elif Weight <= 12:
        Weight = "Average"
    elif Weight <= 14:
        Weight = "Heavy"
    elif Weight <= 16:
        Weight = "Very Heavy"
        
    #get family background
    Background = Fate + d6()
    if Background == 13:
        Background = "Farmer"
        Bronze = 10
        Free = 8
        new_specs = ["Plants", "Forage"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 14:
        Background = "Herder"
        Bronze = 110
        Free = 7
        new_specs = ["Tame", "Track"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 15:
        Background = "Scribe"
        Bronze = 110
        Free = 7
        new_specs = ["Memory", "Forgery"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 16:
        Background = "Curator"
        Bronze = 210
        Free = 6
        new_specs = ["Contacts", "Interrogate"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 17:
        Background = "Inventor"
        Bronze = 210
        Free = 6
        new_specs = ["Build", "Repair"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 18:
        Background = "Craftsman"
        Bronze = 310
        Free = 5
        new_specs = ["Artistry", "Business"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1        
    elif Background == 19:
        Background = "Inventor"
        Bronze = 210
        Free = 6
        new_specs = ["Build", "Repair"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 20:
        Background = "Scientist"
        Bronze = 410
        Free = 4
        new_specs = ["Medical", "Interrogate"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 21:
        Background = "Diplomat"
        Bronze = 410
        Free = 4
        new_specs = ["Languages", "Customs"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 22:
        Background = "Philosopher"
        Bronze = 510
        Free = 3
        new_specs = ["Sanity", "Interrogate"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 23:
        Background = "Enchanter"
        Bronze = 610
        Free = 2
        new_specs = ["Arcane Lore", "Enchant"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1