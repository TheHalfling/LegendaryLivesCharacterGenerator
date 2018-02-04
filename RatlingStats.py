# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:19:46 2018

@author: Sherry
Done
"""


def CorsairStats():
    #Get base stats
    Agility = 9 + d6()
    Alertness = 8 + d6()
    Charm = 4 + d6()
    Cunning = 12 + d6()
    Dexterity = 10 + d6()
    Fate = 7 + d6()
    Intelligence = 5 + d6()
    Knowledge = 6 + d6()
    Mechanical = 11 + d6()
    Nature = 3 + d6()
    Stamina = 13 + d6()
    Strength = 2 + d6()
    
    #get speciality list started
    Specialties = ['Disguise', 'Mimic', 'Quickness', 'Traps']
    
    #determine Age, Night Vision, Racial Benefits
    Age = Intelligence + Knowledge + 3
    Night_Vision = "Yes"
    Racial_Ability = "Disease"
    Uses_Per_Day = 2
    
    #Get physical stats
    Height = Strength + d6()
    if Height <= 7:
        Height = "Tiny"
    elif Height <= 11:
        Height = "Very Short"
    elif Height <= 14:
        Height = "Short"
    
    Weight = Stamina + d6()
    if Weight <= 16:
        Weight = "Very Thin"
    elif Weight <= 18:
        Weight = "Thin"
    elif Weight <= 21:
        Weight = "Average"
    elif Weight <= 23:
        Weight = "Heavy"
    elif Weight <= 25:
        Weight = "Very Heavy"
        
    #get family background
    Background = Fate + d6()
    if Background == 9:
        Background = "Scavenger"
        Bronze = 10
        Free = 8
        new_specs = ["Search", "Conceal"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 10:
        Background = "Slave"
        Bronze = 10
        Free = 8
        new_specs = ["Dodge", "Run"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 11:
        Background = "Beggar"
        Bronze = 10
        Free = 8
        new_specs = ["Lie", "Preach"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 12:
        Background = "Mime"
        Bronze = 110
        Free = 7
        new_specs = ["Entertain", "Memory"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 13:
        Background = "Jester"
        Bronze = 110
        Free = 7
        new_specs = ["Entertain", "Empathy"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 14:
        Background = "Townsman"
        Bronze = 110
        Free = 7
        new_specs = ["Customs", "Literacy"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1        
    elif Background == 15:
        Background = "Artist"
        Bronze = 210
        Free = 6
        new_specs = ["Intuition", "Legends"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 16:
        Background = "Craftsman"
        Bronze = 210
        Free = 6
        new_specs = ["Business", "Bargain"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 17:
        Background = "Merchant"
        Bronze = 210
        Free = 6
        new_specs = ["Business", "Customs"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 18:
        Background = "Entertainer"
        Bronze = 310
        Free = 5
        new_specs = ["Entertain", "Artistry"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 19:
        Background = "King Rat"
        Bronze = 310
        Free = 5
        new_specs = ["Will", "Bully"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1