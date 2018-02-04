# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:19:46 2018

@author: Sherry
done
"""


def CorsairStats():
    #Get base stats
    Agility = 5 + d6()
    Alertness = 11 + d6()
    Charm = 7 + d6()
    Cunning = 6 + d6()
    Dexterity = 8 + d6()
    Fate = 4 + d6()
    Intelligence = 12 + d6()
    Knowledge = 2 + d6()
    Mechanical = 3 + d6()
    Nature = 13 + d6()
    Stamina = 10 + d6()
    Strength = 9 + d6()
    
    #get speciality list started
    Specialties = ['Pole Arm', 'Ride', 'Tame', 'Wagoning']
    
    #determine Age, Night Vision, Racial Benefits
    Age = Intelligence + Knowledge
    Night_Vision = "No"
    Racial_Ability = "Augury"
    Uses_Per_Day = 2
    
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
    if Weight <= 13:
        Weight = "Very Thin"
    elif Weight <= 15:
        Weight = "Thin"
    elif Weight <= 18:
        Weight = "Average"
    elif Weight <= 20:
        Weight = "Heavy"
    elif Weight <= 22:
        Weight = "Very Heavy"
        
    #get family background
    Background = Fate + d6()
    if Background == 6:
        Background = "Hobo"
        Bronze = 10
        Free = 8
        new_specs = ["Forage", "Lie"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 7:
        Background = "Farmer"
        Bronze = 110
        Free = 7
        new_specs = ["Plants", "Build"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 8:
        Background = "Rustler"
        Bronze = 110
        Free = 7
        new_specs = ["Stealth", "Lie"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 9:
        Background = "Preacher"
        Bronze = 210
        Free = 6
        new_specs = ["Theology", "Preach"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 10:
        Background = "Soldier"
        Bronze = 210
        Free = 6
        new_specs = ["Sword", "Bow"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 11:
        Background = "Herder"
        Bronze = 110
        Free = 7
        new_specs = ["Sword", "Languages"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1        
    elif Background == 12:
        Background = "Rancher"
        Bronze = 310
        Free = 5
        new_specs = ["Business", "Customs"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1
    elif Background == 13:
        Background = "Blacksmith"
        Bronze = 410
        Free = 4
        new_specs = ["Build", "Repair"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 14:
        Background = "Trail Boss"
        Bronze = 410
        Free = 4
        new_specs = ["Bully", "Medical"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 15:
        Background = "Craftsman"
        Bronze = 510
        Free = 3
        new_specs = ["Bargain", "Build"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1                    
    elif Background == 16:
        Background = "Merchant"
        Bronze = 610
        Free = 2
        new_specs = ["Business", "Literacy"]
        for ea in new_specs:
            if ea not in Specialties:
                Specialties.append(ea)
            else:
                Free += 1