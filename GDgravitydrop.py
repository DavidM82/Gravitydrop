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

    #This checks to see if new items were added during the session.
    changed = False
    
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
        print "[6] Show Disclaimer"
        print "[7] Exit program "
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
            print""
            print "Type 'menu' at any point to stop and return to menu."
            print ""
            print "In order to make an item, it needs three things, name, mass and height."
            print "Type each on seperate lines."
            
            na = raw_input("Name (string): ")
            #Checks that it doesn't already use a name in the database. If it does, returns to menu.
            checker = True
            ba = na.lower().strip().replace(" ", "")
            for i in items:
                i = i.callname
                if ba == i:
                    print "That name is already being used."
                    checker = False

            if checker == False:
                pass
            if ba == 'menu':
                pass
            else:
                ma = raw_input("Mass (integer) [kg]: ")
                if ma == 'menu':
                    pass
                else:
                    he = raw_input("Height (integer) [m]: ")
                    if he == 'menu':
                        pass
                    else:
                        ni = itemMaker(na,float(ma),float(he))
                        items.append(ni)
                        changed = True
                        print ""
                        print "Item has been added."

        if b == 4:
            #This changes the pre-existing constants in the simulation.
            print "It needs to exist before you can change it."

        if b == 5:
            #This prints out the name of every item in the database with an option of going into any item's stats.

            counter = 1
            for i in items:
                print "[" + str(counter) + "]" + i.name
                counter = counter + 1
                
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
                    print "Type its position in the list."
                    n = input("")
                    n = n-1
                    
                    print ""
                    print "Name: " + items[n].name
                    print "Mass: " + str(items[n].mass) + " kilograms"
                    print "Height: " + str(items[n].height) + " meters"
                
                elif datainput == "3":
                    data = False
                    
                else:
                    print "Not a valid input, try again."

        if b == 6:
            #Where the author attempts to show his skills at making a mult-line print statement.
            disclaimer()
        
        if b == 7:
            #This exits the program but if user wants to save changes, goes to Savefile().
            if changed == True:
                print "Database has changed, would you like to save changes? [Yes] or [No]"

                exiting = False
                while exiting == False:
                    save = raw_input("")
                    save = save.strip().lower()
                    if  save == "no":
                        exiting = True
                        pass
                    elif save == "yes":
                        SaveFile()
                        exiting = True
                    else:
                        print "Not a valid answer, please type [Yes] or [No]."

            print "Exiting gravitydrop.py... "
            a = False
            
        if b == 8:
            #Prints the first item's name in the list, to show that variables carry over between programs.
            print items[0].name


def Simulation():
    #This program runs the actual simulation.
    #Inputs: None
    #Return: Two print statements.

    #Prints out the list.
    print "List of items:"
    for i in items:
        print i.name
    print ""

    print "Type 'menu' to stop at any point and return to menu."        
    print "What would you like to drop?"
    
    falling_in_items = False
    while falling_in_items == False:
        falling_input = str(raw_input())
        #Converts the input to the callname syntax. This makes it so that I can call up the cat item by typing Cat, CAT, c at, C A T and of course, cat.
        falling_input = falling_input.lower().strip().replace(" ","")

        if falling_input == 'menu':
            return None

        for i in items:
            if falling_input == i.callname:
                falling = i
                falling_in_items = True        

        if falling_in_items == False:
            print "That item is not presently in the system, please enter another item"
                    
    print "What would you like to drop the " + falling.name + " from?"
    #I'd like this print statement to include the falling object name
    notfalling_in_items = False
    while notfalling_in_items == False:
        notfalling_input = str(raw_input())
        notfalling_input = notfalling_input.lower().strip().replace(" ", "")

        if notfalling_input == 'menu':
            return None
            
        for i in items:
            if notfalling_input == i.callname:
                notfalling = i
                notfalling_in_items = True        

        if notfalling_in_items == False:
            print "That item is not presently in the system, please enter another item"

    Energy = ImpactEnergy(falling,notfalling)
    Time = ImpactTime(falling, notfalling)

    print ""
    print "You are dropping a " + falling.name + " from a " + notfalling.name
    print "It took "  + str(Time) + " seconds to hit the ground."
    if Energy < 1:
        print "A total of " + str(Energy//(10**-3)) + " mJ were released." 
    elif Energy >= 0 and Energy < 1000:
        print "A total of " + str(Energy) + " J were released."
    elif Energy >= 1000 and Energy < 1000000:
        print "A total of " + str(Energy/(10**3)) + " kJ were released."
    else:
        print "A total of " + str(Energy/(10**6)) + " MJ were released."


def disclaimer():
    #A very important warning to all those who might take this simulator seriously. Formatted to fit the default console screen.
    d1 = "Disclaimer: this program was developed my an inexperienced mechanical engineer  and his programmer friend."
    d2 = "This program does not account for air resistance or changes Earth's             gravitational field. (yet) "
    d3 = "All pre-set data came from Google. The data obtained from this program should   not be used in any serious application."
    d4 = "All experiments performed with this simulation's data should be videotaped and  uploaded to YouTube as quickly as possible."
    d5 = "This is the end of the disclaimer, it will cease to disclaim at the end of this sentence."
    
    print d1
    print d2
    print d3
    print d4
    print d5

def SaveFile():
    #This saves the database, keeping changes for future sessions.
    data = open('GDdatabase.txt', 'w')

    for i in items:
        data.write("Item ")
        data.write(i.name + " ")
        data.write(str(i.mass) + " ")
        data.write(str(i.height) + " ")
    
    print "Database has been saved."
    print ""


#Constants and physics functions to run the equations used in Simulation()
g = 9.81 #gravitationial acceleration [m/s^2]

def ImpactEnergy(falling, notfalling):
    #This function calculates the amount of kinetic energy the falling object has just before impact
    #This function uses the mass of the falling object and the height of the notfalling object.
    #Inputs: falling (item), nonfalling (item)
    #Return: Energy (int)

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

    Vel = (2*g*notfalling.height)**.5
    Time = notfalling.height/Vel
    return Time


def Master():
    "Runs all the other functions in this program."
    Intro()
    Interface()

Master()
