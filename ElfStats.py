# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:19:46 2018

@author: Sherry
Done
"""


def CorsairStats():
    #Get base stats
    Agility = 9 + d6()
    Alertness =67 + d6()
    Charm = 13 + d6()
    Cunning = 3 + d6()
    Dexterity = 11 + d6()
    Fate = 10 + d6()
    Intelligence = 8 + d6()
    Knowledge = 7 + d6()
    Mechanical = 2 + d6()
    Nature = 12 + d6()
    Stamina = 4 + d6()
    Strength = 5 + d6()
    
    #get speciality list started
    Specialties = ['Bow', 'Plants', 'Quickness', 'Stealth']
    
    #determine Age, Night Vision, Racial Benefits
    Age = Intelligence + Knowledge -1
    Night_Vision = "Yes"
    Racial_Ability = "Speed"
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
    if Weight <= 9:
        Weight = "Very Thin"
    elif Weight <= 12:
        Weight = "Thin"
    elif Weight <= 15:
        Weight = "Average"
    elif Weight <= 16:
        Weight = "Heavy"
        
    #get family background
    Background = Fate + d6()
    if Background == 12:
        Background = "Gatherer"
        Bronze = 10
        Free = 8
        new_specs = ["Forage", "Search"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 13:
        Background = "Farmer"
        Bronze = 110
        Free = 7
        new_specs = ["Tame", "Pole Arm"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 14:
        Background = "Innkeeper"
        Bronze = 110
        Free = 7
        new_specs = ["Business", "Languages"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 15:
        Background = "Story-teller"
        Bronze = 210
        Free = 6
        new_specs = ["Legends", "Entertain"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 16:
        Background = "Merchant"
        Bronze = 210
        Free = 6
        new_specs = ["Business", "Customs"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 17:
        Background = "Craftsman"
        Bronze = 310
        Free = 5
        new_specs = ["Artistry", "Bargain"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1        
    elif Background == 18:
        Background = "Animal Trainer"
        Bronze = 310
        Free = 5
        new_specs = ["Tame", "Ride"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 19:
        Background = "Artist"
        Bronze = 410
        Free = 4
        new_specs = ["Intuition", "Artistry"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 20:
        Background = "Herbalist"
        Bronze = 410
        Free = 4
        new_specs = ["Poison", "Medical"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 21:
        Background = "Councillor"
        Bronze = 510
        Free = 3
        new_specs = ["Empathy", "Customs"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 22:
        Background = "Noble"
        Bronze = 610
        Free = 2
        new_specs = ["Plant Mastery", "Literacy"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1