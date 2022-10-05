# forces.py - Forces Equations File
# By: Joshua Lim
# Date: 10/04/2022
# Version 0 Optimized

# imports
# import math

# function to ask what the user is trying to find
def findWhat():
    print("----------------------------------------")
    print("What are you trying to find?")
    print("1. Force")
    print("2. Mass")
    print("3. Acceleration")
    print("4. Net Force")
    print("5. Weight")
    choice = int(input("Enter the number of the variable you are trying to find: "))
    if choice == 1:
        return "force"
    elif choice == 2:
        return "mass"
    elif choice == 3:
        return "acceleration"
    elif choice == 4:
        return "net force"
    elif choice == 5:
        return "weight"
    else:
        print("Please enter a valid number.")
        findWhat()

# function to ask what variables are given
def givenVariables(finding):
    print("----------------------------------------")
    print("What variables are given? (enter '-' if it is not given)")
    if finding != "force":
        force = int(input("Enter the force: "))
    else:
        force = "-"
    if finding != "mass":
        mass = int(input("Enter the mass: "))
    else:
        mass = "-"
    if finding != "acceleration":
        acceleration = int(input("Enter the acceleration: "))
    else:
        acceleration = "-"
    if finding != "net force":
        netForce = int(input("Enter the net force: "))
    else:
        netForce = "-"
    if finding != "weight":
        weight = int(input("Enter the weight: "))
    else:
        weight = "-"
    return [force, mass, acceleration, netForce, weight]

# function to solve for force
def force(mass, acceleration):
    return mass * acceleration

# function to solve for mass
def mass(force, acceleration):  
    return force / acceleration

# function to solve for acceleration
def acceleration(force, mass):
    return force / mass

# function to solve for net force
def netForce(force1, force2):
    return force1 + force2

# function to solve for weight
def weight(mass, gravity):
    return mass * gravity

# run code here
# given list structure [force, mass, acceleration, netForce, weight]
#                         0      1         2          3         4
solvingFor = findWhat()
given = givenVariables(solvingFor)
print("----------------------------------------")
if solvingFor == "force": # needs mass and acceleration (1, 2)
    if given[1] == "-":
        print("Sorry, Python Calculator cannot solve for mass without force. Please try again.")
    elif given[2] == "-":
        print("Sorry, Python Calculator cannot solve for acceleration without force. Please try again.")
    else:
        print("Force = " + str(force(given[1], given[2])) + " by using the equation F = m * a.")
elif solvingFor == "mass": # needs force and acceleration (0, 2)
    if given[0] == "-":
        print("Sorry, Python Calculator cannot solve for force without mass. Please try again.")
    elif given[2] == "-":
        print("Sorry, Python Calculator cannot solve for acceleration without mass. Please try again.")
    else:
        print("Mass = " + str(mass(given[0], given[2])) + " by using the equation m = F / a.")
elif solvingFor == "acceleration": # needs force and mass (0, 1)
    if given[0] == "-":
        print("Sorry, Python Calculator cannot solve for force without acceleration. Please try again.")
    elif given[1] == "-":
        print("Sorry, Python Calculator cannot solve for mass without acceleration. Please try again.")
    else:
        print("Acceleration = " + str(acceleration(given[0], given[1])) + " by using the equation a = F / m.")
elif solvingFor == "net force": # needs force1 and force2 (0, 0)
    if given[0] == "-":
        print("Sorry, Python Calculator cannot solve for force without net force. Please try again.")
    elif given[3] == "-":
        print("Sorry, Python Calculator cannot solve for force without net force. Please try again.")
    else:
        print("Net Force = " + str(netForce(given[0], given[3])) + " by using the equation F = F1 + F2.")
elif solvingFor == "weight": # needs mass and gravity (1, 5)
    if given[1] == "-":
        print("Sorry, Python Calculator cannot solve for mass without weight. Please try again.")
    elif given[4] == "-":
        print("Sorry, Python Calculator cannot solve for gravity without weight. Please try again.")
    else:
        print("Weight = " + str(weight(given[1], given[4])) + " by using the equation W = m * g.")
else:
    print("Please enter a valid number.")
print("----------------------------------------")
# end of code