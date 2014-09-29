"""
filename: itemdatabase.py
description: This program holds the class item and makes the data structure to hold all items.
language: Python 2.7.8
date created: September 27. 2014
"""

class item:
    #Defines the item object with three data points, name (str), mass (int) and height (int)
    def __init__(item, name, mass, height):
        item.name = name
        item.mass = mass
        item.height = height

# Test case showing how to use the class
#a = "Name"
#b = 1
#c = 3
#d = item(a,b,c)
#
#Print statements shows each part of the item.
#print d.name
#print d.mass
#print d.height
#If you were to print d itself, you get its location in your memory, which isn't what you want.

def itemMaker(name, mass, height):
    #Constructs new items.
    #Inputs: name (str), mass (int), height (int)
    #Return: newitem (item)
    newitem = item(name, mass, height)

    return newitem

#The database is displayed as a dictionary with item.name used as keys

#The database adds the items in the database.


#But for now, it's a list of items.

box = item("box", 4, 2)
man = item("man", 10, 2)
cat = item("cat", 2, 1)

items = [box, man, cat]
