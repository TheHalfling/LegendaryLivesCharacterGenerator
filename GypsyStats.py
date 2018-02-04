# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:19:46 2018

@author: Sherry
Done
"""


def CorsairStats():
    #Get base stats
    Agility = 7 + d6()
    Alertness = 9 + d6()
    Charm = 6 + d6()
    Cunning = 13 + d6()
    Dexterity = 12 + d6()
    Fate = 11 + d6()
    Intelligence = 3 + d6()
    Knowledge = 10 + d6()
    Mechanical = 2 + d6()
    Nature = 8 + d6()
    Stamina = 4 + d6()
    Strength = 5 + d6()
    
    #get speciality list started
    Specialties = ['Arcane Lore', 'Contacts', 'Legends', 'Poison']
    
    #determine Age, Night Vision, Racial Benefits
    Age = Intelligence + Knowledge + 1
    Night_Vision = "No"
    Racial_Ability = "Fortune Telling"
    Uses_Per_Day = 3
    
    #Get physical stats
    Height = Strength + d6()
    if Height <= 8:
        Height = "Very Short"
    elif Height <= 10:
        Height = "Short"
    elif Height <= 13:
        Height = "Average"
    elif Height <= 15:
        Height = "Tall"
    elif Height <= 17:
        Height = "Very Tall"
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
        Background = "Beggar"
        Bronze = 10
        Free = 8
        new_specs = ["Lie", "Disguise"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 14:
        Background = "Cutpurse"
        Bronze = 10
        Free = 8
        new_specs = ["Filch", "Quickness"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 15:
        Background = "Wheelwright"
        Bronze = 10
        Free = 8
        new_specs = ["Business", "Repair"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 16:
        Background = "Horse Trader"
        Bronze = 110
        Free = 7
        new_specs = ["Bargain", "Ride"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 17:
        Background = "Blacksmith"
        Bronze = 110
        Free = 7
        new_specs = ["Build", "Repair"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 18:
        Background = "Entertainer"
        Bronze = 110
        Free = 7
        new_specs = ["Entertain", "Mimic"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1        
    elif Background == 19:
        Background = "Seer"
        Bronze = 210
        Free = 6
        new_specs = ["Inuition", "Empathy"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 20:
        Background = "Animal Trainer"
        Bronze = 210
        Free = 6
        new_specs = ["Tame", "Ride"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 21:
        Background = "Craftsman"
        Bronze = 210
        Free = 6
        new_specs = ["Business", "Bargain"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 22:
        Background = "Healer"
        Bronze = 310
        Free = 5
        new_specs = ["Plants", "Medical"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 23:
        Background = "Spiritualist"
        Bronze = 310
        Free = 5
        new_specs = ["Divination", "Intuition"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1