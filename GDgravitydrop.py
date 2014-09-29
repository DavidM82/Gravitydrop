"""
filename: gravitydrop.py
description: This program finds out the amount of energy released by objects dropped
language: Python 2.7.8
date created: September 27, 2014
"""

from GDitems import *

def Intro():
    #Introduces the user to this program, explains what to do.
    print "This program is designed to find the amount of energy an object has right before hitting the ground when dropped from another object."

def Interface():
    #This program provides the options the user can do.
    
    a = True;    
    #This is run as a loop until a becomes false.
    while  a == True:
        print ""
        print "What would you like to do now?"
        print "[1] Run program"
        print "[2] Change unit system"
        print "[3] Make new item"
        print "[4] Change constants"
        print "[5] Show all items in database"
        print "[6] Exit program "
        b = input("")
        print ""
        
        if b == 1:
            #This moves to another function that runs the actual 'simulation', in theory.
            Simulation()
            
        if b == 2:
            #This moves to a function that changes the unit system shown in the simulation and new items.
            print "I lied, you don't get to change it. Metric for life!"

        if b == 3:
            #This calls the itemMaker() and adds it to the database.
            print "In order to make an item, it needs three things, name, mass and height."

            print "Type each on seperate lines."
            na = raw_input("Name (string): ")
            #Checks that it doesn't already use a name in the database. If it does, returns to menu.
            checker = True
            for i in items:
                i = i.name
                if na == i:
                    print "That name is already being used."
                    checker = False

            if checker == False:
                pass
            else:
                ma = input("Mass (integer) [m]: ")
                he = input("Height (integer) [kg]: ")
                ni = itemMaker(na,ma,he)
                items.append(ni)
                print ""
                print "Item has been added."

        if b == 4:
            #This changes the pre-existing constants in the simulation.
            print "It needs to exist before you can change it."

        if b == 5:
            #This prints out the name of every item in the database with an option of going into any item's stats.

            for i in items:
                print i.name
            data = True
            while data == True:
                print ""
                print "Type [1] to see all items again, [2] to select an item and view its data, or [3] to return to menu."
                datainput = raw_input("")
                
                if datainput == "1":
                    for i in items:
                        print i.name
                        
                elif datainput == "2":
                    print ""
                    print "Type the position it appears in the list, with the topmost being 1."
                    n = input("")
                    n = n-1
                    
                    print ""
                    print "Name: " + items[n].name
                    print "Mass: " + str(items[n].mass)
                    print "Height: " + str(items[n].height)
                
                elif datainput == "3":
                    data = False
                    
                else:
                    print "Not a valid input, try again."
        
        if b == 6:
            #This exits the program.
            print "Exiting gravitydrop.py... "
            a = False
            
        if b == 7:
            #Prints the first item's name in the list, to show that variables carry over between programs.
            print items[1].name


def Simulation():
    #This program runs the actual simulation.
    #Inputs: None
    #Return: Two print statements.

    #Prints out the list.
    print "List of items:"
    for i in items:
        print i.name
        
    print "What would you like to drop?"
    falling_input = raw_input()
    falling_input = falling_input.lower
    
    falling_in_items = False
    while falling_in_items == False:
        if falling_input not in items:
            print "That item is not presently in the system"
            falling_input = raw_input()
        else:
            falling = items[falling_input]
            falling_in_items = True

    print "What would you like to drop it from?"
    #I'd like this print statement to include the falling object name
    notfalling_input = raw_input()
    notfalling_input = notfalling_input.lower
    notfalling_in_items = False
    
    while not_falling_in_items == False:
        if notfalling_input not in items:
            print "That item is not presently in the system"
            notfalling_input = raw_input()
        else:
            notfalling = items[notfalling_input]
            notfalling_in_items = True

    Energy = ImpactEnergy(falling,notfalling)
    Time = ImpactTime(falling, notfalling)
    print "It took "  + str(Time) + " seconds to hit the ground."
    print "A total of " + str(Energy) + " Joules were released."


#Constants
g = 9.81 #gravitation acceleration [m/s^2]

def ImpactEnergy(falling, notfalling):
    #This function calculates the amount of kinetic energy the falling object has just before impact
    #This function uses the mass of the falling object and the height of the notfalling object.
    #Inputs: falling (item), nonfalling (item)
    #Return: Energy (int)

    g = 9.81
    h= notfalling.height #[m]
    m= falling.mass      #[kg]

    Energy = m*g*h       #[J]
    return Energy

def ImpactTime(falling, notfalling):
    #This function measures the time it takes the falling object to hit the ground.
    #Inputs: falling (item), nonfalling (item)
    #Return: Time (int)

    # The equation used for this is Velcoity (final) / acceleration = time (seconds)
    # Velcoity is obtained by getting the square root of 2*acceleration*height of nonfalling
    g = 9.81

    Vel = (2*g*notfalling.height)**.5
    Time = Vel / g
    return Time

def Master():
    "Runs all the other functions in this program."
    Intro()
    Interface()

Master()
