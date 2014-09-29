"""
filename: itemdatabase.py
description: This program holds the class item and makes the data structure to hold all items.
language: Python 2.7.8
date created: September 27. 2014
"""

class item:
    #Defines the item object with three data points, name (str), mass (int) and height (int)
    #callname (str) added to allow displaying names with capitials and spaces without affecting calling them.
    def __init__(item, name, mass, height):
        item.name = name
        item.mass = mass
        item.height = height
        callname = item.name.strip().lower().replace(" ", "")
        item.callname = callname

# Test case showing how to use the class
#a = "Name"
#b = 1
#c = 3
#e = item(a,b,c,d)
#
#Print statements shows each part of the item.
#print e.name
#print e.mass
#print e.height
#If you were to print d itself, you get its location in your memory, which isn't what you want.

def itemMaker(name, mass, height):
    #Constructs new items.
    #Inputs: name (str), mass (int), height (int), call(str)
    #Return: newitem (item)
    newitem = item(name, mass, height)

    return newitem

#The database is displayed as a dictionary with item.name used as keys

#The database adds the items in the database.


#But for now, it's a list of items.

box = itemMaker("Box", .450, .3048)
man = itemMaker("Man", 78.5, 1.776)
cat = itemMaker("Cat", 4.5, .23)

items = [box, man, cat]

