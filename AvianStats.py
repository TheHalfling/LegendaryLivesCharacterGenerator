# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:17:56 2018

@author: Sherry
Done
"""

#get Avian stats
def AvainStats():
    #Get base stats
    Agility = 11 + d6()
    Alertness = 13 + d6()
    Charm = 12 + d6()
    Cunning = 3 + d6()
    Dexterity = 9 + d6()
    Fate = 8 + d6()
    Intelligence = 10 + d6()
    Knowledge = 2 + d6()
    Mechanical = 4 + d6()
    Nature = 5 + d6()
    Stamina = 6 + d6()
    Strength = 7 + d6()
    
    #get speciality list started
    Specialties = ['Crossbow', 'Dodge', 'Quickness', 'Search']
    
    #determine Age, Night Vision, Racial Benefits
    Age = Intelligence + Knowledge + 2
    Night_Vision = "No"
    Racial_Ability = "Fly"
    Uses_Per_Day = 5
    
    #Get physical stats
    Height = Strength + d6()
    if Height <= 11:
        Height = "Very Short"
    elif Height <= 14:
        Height = "Short"
    elif Height <= 17:
        Height = "Average"
    elif Height <= 19:
        Height = "Tall"
    Weight = Stamina + d6()
    if Weight <= 11:
        Weight = "Very Thin"
    elif Weight <= 14:
        Weight = "Thin"
    elif Weight <= 17:
        Weight = "Average"
    elif Weight == 18:
        Weight = "Heavy"
        
    #get family background
    Background = Fate + d6()
    if Background == 10:
        Background = "Gatherer"
        Bronze = 10
        Free = 8
        new_specs = ["Plants", "Forage"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 11:
        Background = "Fisher"
        Bronze = 10
        Free = 8
        new_specs = ["Swim", "Quickness"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 12:
        Background = "Hunter"
        Bronze = 10
        Free = 8
        new_specs = ["Forage", "Track"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 13:
        Background = "Weaver"
        Bronze = 110
        Free = 7
        new_specs = ["Build", "Business"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 14:
        Background = "Scout"
        Bronze = 110
        Free = 7
        new_specs = ["Stealth", "Direction"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 15:
        Background = "Messenger"
        Bronze = 110
        Free = 7
        new_specs = ["Languages", "Memory"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1        
    elif Background == 16:
        Background = "Entertainer"
        Bronze = 210
        Free = 6
        new_specs = ["Entertain", "Mimic"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 17:
        Background = "Story-Teller"
        Bronze = 210
        Free = 6
        new_specs = ["Legends", "Memory"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 18:
        Background = "Craftsman"
        Bronze = 210
        Free = 6
        new_specs = ["Build", "Artistry"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 19:
        Background = "Herbalist"
        Bronze = 310
        Free = 5
        new_specs = ["Plants", "Medical"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 20:
        Background = "Voice of Ler"
        Bronze = 310
        Free = 5
        new_specs = ["Air Mastery", "Customs"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1