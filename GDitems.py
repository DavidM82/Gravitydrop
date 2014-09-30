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

#The items is a list of items read off a file called GDdatabase.txt. It's important that the file exists, even if it's blank.
items = []

#This takes all the words out of the file and puts it into a list.
data = open('GDdatabase.txt', 'r')
allwords = data.read()
eachword = allwords.split()
data.close()

#This for loop scans each word to see if it matches 'Item', if it does it takes the next three words and puts it into an item (item) and adds it to items (List)
pointer = 0
for i in eachword:
    if i == 'Item':
        a = eachword[pointer+1]
        b = eachword[pointer+2]
        c = eachword[pointer+3]
        new = itemMaker(a,b,c)
        items.append(new)
    pointer = pointer + 1
