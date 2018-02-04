# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:19:46 2018

@author: Sherry
Done
"""


def CorsairStats():
    #Get base stats
    Agility = 6 + d6()
    Alertness = 9 + d6()
    Charm = 12 + d6()
    Cunning = 7 + d6()
    Dexterity = 4 + d6()
    Fate = 13 + d6()
    Intelligence = 8 + d6()
    Knowledge = 11 + d6()
    Mechanical = 5 + d6()
    Nature = 10 + d6()
    Stamina = 2 + d6()
    Strength = 3 + d6()
    
    #get speciality list started
    Specialties = ['Arcane Lore', 'Artistry', 'Legends', 'Preach']
    
    #determine Age, Night Vision, Racial Benefits
    Age = Intelligence + Knowledge - 5
    Night_Vision = "No"
    Racial_Ability = "Heal"
    Uses_Per_Day = 4
    
    #Get physical stats
    Height = Strength + d6()
    if Height <= 7:
        Height = "Very Short"
    elif Height <= 10:
        Height = "Short"
    elif Height <= 13:
        Height = "Average"
    elif Height <= 15:
        Height = "Tall"
    
    Weight = Stamina + d6()
    if Weight <= 7:
        Weight = "Very Thin"
    elif Weight <= 10:
        Weight = "Thin"
    elif Weight <= 13:
        Weight = "Average"
    elif Weight <= 14:
        Weight = "Heavy"
    
    #get family background
    Background = Fate + d6()
    if Background == 15:
        Background = "Story-Teller"
        Bronze = 10
        Free = 8
        new_specs = ["Entertain", "Languages"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 16:
        Background = "Musician"
        Bronze = 110
        Free = 7
        new_specs = ["Entertain", "Quickness"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 17:
        Background = "Scribe"
        Bronze = 110
        Free = 7
        new_specs = ["Literacy", "Languages"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 18:
        Background = "Artist"
        Bronze = 210
        Free = 6
        new_specs = ["Sincerity", "Forgery"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 19:
        Background = "Warrior"
        Bronze = 210
        Free = 6
        new_specs = ["Sword", "Bow"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 20:
        Background = "Gentry"
        Bronze = 310
        Free = 5
        new_specs = ["Customs", "Literacy"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1        
    elif Background == 21:
        Background = "Minstrel"
        Bronze = 310
        Free = 5
        new_specs = ["Entertain", "Memory"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 22:
        Background = "Concubine"
        Bronze = 410
        Free = 4
        new_specs = ["Entertain", "Sincerity"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 23:
        Background = "Earl of Elves"
        Bronze = 410
        Free = 4
        new_specs = ["Interrogate", "Literacy"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 24:
        Background = "Duke of Elves"
        Bronze = 510
        Free = 3
        new_specs = ["Sincerity", "Customs"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 25:
        Background = "Royalty"
        Bronze = 610
        Free = 2
        new_specs = ["Languages", "Bewitch"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1