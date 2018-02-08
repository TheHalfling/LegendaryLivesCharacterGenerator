# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
Determines Religious Lifeline
"""
import random

def d100():
    roll = random.randint(1,100)
    return roll

def pursuedByFaith():
    roll = d100()
    if roll <= 15:
        result = "Desecrated temple or shrine."
    elif roll <= 30:
        result = "Stole HOLY RELIC."
    elif roll <= 50:
        result = "Lured members away from the faith."
    elif roll <= 70:
        result = "Accused temple leaders of crimes"
    elif roll <= 90:
        result = "Mocked religious leaders and/or gods."
    elif roll <= 100:
        result = "Declared a heretic and condemned to death."
    return result


def holyRelic():
    roll = d100()
    if roll <= 8:
        result = "Weapon"
    elif roll <= 16:
        result = "Garment"
    elif roll <= 23:
        result = "Wand"
    elif roll <= 30:
        result = "Staff"
    elif roll <= 38:
        result = "Book"
    elif roll <= 45:
        result = "Icon"
    elif roll <= 52:
        result = "Statuette"
    elif roll <= 58:
        result = "Musical Instrument"
    elif roll <= 64:
        result = "Jewelry"
    elif roll <= 70:
        result = "Letter"
    elif roll <= 76:
        result = "Flag or Banner"
    elif roll <= 83:
        result = "Cup or Bowl"
    elif roll <= 89:
        result = "Bottle"
    elif roll <= 95:
        result = "Animal"
    elif roll <= 100:
        result = "Magical. Roll again for type"
    return result
        

def excommunicated():
    roll = d100()
    if roll <= 10:
        result = "Promiscuity"
    elif roll <= 20:
        result = "Avarice"
    elif roll <= 30:
        result = "Greed"
    elif roll <= 40:
        result = "Pride"
    elif roll <= 50:
        result = "Broken sacred vow"
    elif roll <= 60:
        result = "Refused to obey temple law"
    elif roll <= 70:
        result = "Mocked leaders and/or gods"
    elif roll <= 80:
        result = "Theft of temple goods"
    elif roll <= 90:
        result = "Tried to buy favors"
    elif roll <= 100:
        result = "Declared a heretic. Banished from homeland"
    return result


def religiousTimeLine():
    roll = d100()
    if roll <= 2:
        result = "Dedicated to religion at birth, +2 Devotion"
    elif roll <= 4:
        result = "Lived/worked in temple, +1 Devotion"
    elif roll <= 6:
        result = "Religious fanatic, +1 Preach"
    elif roll <= 8:
        result = "Served church for d6 years, +1 Theology"
    elif roll <= 10:
        result = "Trained as scribe, +1 Literacy, +1 Theology"
    elif roll <= 12:
        result = "Hermit for d6 years, +1 Devotion"
    elif roll <= 15:
        result = "Sworn to celibacy until quest completed"
    elif roll <= 17:
        result = "Missionary, spreading the faith through persuasion"
    elif roll <= 19:
        result = "Crusader, spreading the faith through force"
    elif roll <= 21:
        result = "Currently on holy mission"
    elif roll <= 23:
        result = "Keeper of {}".format(holyRelic())
    elif roll <= 29:
        result = "Searching for {}".format(holyRelic())
    elif roll <= 32:
        result = "Delivering {}".format(holyRelic())
    elif roll <= 37:
        result = "Subject to religious visions"
    elif roll <= 40:
        result = "Know deep, dark secret about faith"
    elif roll <= 43:
        result = "Parents are of radically different faith"
    elif roll <= 45:
        result = "Fought in holy war, +1 to one Weapon skill"
    elif roll <= 46:
        result = "Creator of own religious sect, +1 Preach"
    elif roll <= 47:
        result = "Doubtful about faith"
    elif roll <= 52:
        result = "{} on true charges".format(pursuedByFaith())
    elif roll <= 56:
        result = "{} on false charges".format(pursuedByFaith())
    elif roll <= 58:
        result = "Relative of famous religious leader"
    elif roll <= 60:
        result = "Bound by a religious oath"
    elif roll <= 63:
        result = "Believe self to be reincarnation of famous prophet or religious leader"
    elif roll <= 65:
        result = "Blessed by holy person, +1 Devotion"
    elif roll <= 67:
        result = "Cursed by holy person, —1 Fate"
    elif roll <= 70:
        result = "{} on true charges".format(excommunicated())
    elif roll <= 73:
        result = "{} on false charges".format(excommunicated())
    elif roll <= 76:
        result = "Currently on pilgrimage"
    elif roll <= 78:
        result = "d6 characters look to you as religious leader"
    elif roll <= 79:
        result = "Faith persecuted, shunned by community"
    elif roll <= 80:
        result = "Persecuted for faith. No open meetings by order of law."
    elif roll <= 81:
        result = "Persecuted for faith. Forced to live in ghetto."
    elif roll <= 82:
        result = "Persecuted. Must carry ID or identifying mark."
    elif roll <= 83:
        result = "Imprisoned if found-practicing faith"
    elif roll <= 84:
        result = "Executed if found practicing faith."
    elif roll <= 85:
        result = "Persecuted for faith. Most jobs and businesses are off limits."
    elif roll <= 86:
        result = "Persecuted. Temples commonly desecrated."
    elif roll <= 87:
        result = "Join radical sect to fight religious oppression."
    elif roll <= 88:
        result = "Relative/friend killed for practicing faith."
    elif roll <= 89:
        result = "Scouting for place to settle without persecution."
    elif roll <= 92:
        result = "Wish to build temple or shrine worth $5,000."
    elif roll <= 94:
        result = "Member of secret sect plotting to take over world."
    elif roll <= 97:
        result = "Romantically involved with religious leader."
    elif roll <= 100:
        result = "Disowned by family after joining foreign faith."
    return result
