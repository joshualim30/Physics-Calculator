# newtonsLaws.py - Newtons Laws Equations File
# By: Joshua Lim
# Date: 10/04/2022
# Version 0 Optimized

# Newton's Laws of Motion
# 1. An object at rest will stay at rest unless acted upon by an unbalanced force.
# 2. An object in motion will stay in motion unless acted upon by an unbalanced force.
# -  a = F / m
# -  a = Vf - Vi / t
# -  a = (Vf^2 - Vi^2) / 2d
# 3. For every action there is an equal and opposite reaction.

# imports
import math
import sys
import decimal

# global variables
gravity = 9.81

# function to ask what the user is trying to find
def findWhat():
    print("----------------------------------------")
    print("What are you trying to find?")
    print("0.1) Choose a different section (back)")
    print("0.2) List of all equations")
    print("0.3) What are Newton's Laws of Motion?")
    print("---")
    print("1) Magnitude of Acceleration Equilibrium")
    print("2) Magnitude of Acceleration on an Incline Plane")
    print("3) Magnitude of Exerted Force")
    print("4) How Long it Takes for an Object to Stop")
    print("5) How Far an Object Will Travel When You Stopped Pushing It")
    print("6) Speed of Object after Time")
    print("7) Speed of Object after Experiencing an External Force")
    print("8) Velocity of Object after Experiencing an External Force")
    print("9) Velocity of Object after Exerting an External Force")
    print("10) Magnitude of Force Given Mass and Acceleration")
    print("11) Force of Friction Between Two Objects Given Mass, Acceleration and Static Friction")
    print("12) Spring Constant")
    print("13) Tension Compared to Weight")
    print("14) Magnitude of Tension when You Let Go of an Object")
    print("14) Magnitude of Acceleration both Objects Experience")
    print("15) Magnitude of Force Exerted from Object1 on Object2")
    print("16) How Much Force is Required to Separate Two Objects Given Tenstion, Force and Mass")
    choice = float(input("Enter the number of the variable you are trying to find: "))
    if choice == 0.1:
        sys.exit()
    elif choice == 0.2:
        print("List of all equations")
        print("1) Magnitude of Acceleration Equilibrium: ")

    elif choice == 0.3:
        print("Newton's Laws of Motion are:")
        print("1. An object at rest will stay at rest unless acted upon by an unbalanced force.")
        print("2. An object in motion will stay in motion unless acted upon by an unbalanced force.")
        print("3. For every action there is an equal and opposite reaction.")
        print("Press enter to continue")
        input()
        findWhat()
    elif choice >= 1 and choice <= 16:
        return choice
    else:
        print("Please enter a valid number.")
        findWhat()

# function to ask what variables are given
def givenVariables(finding):
    print("----------------------------------------")
    print("What variables are given? (enter '-' if it is not given)")
    if finding != "force":
        force = float(input("Enter the force: "))
    else:
        force = "-"
    if finding != "mass":
        mass = float(input("Enter the mass: "))
    else:
        mass = "-"
    if finding != "acceleration":
        acceleration = float(input("Enter the acceleration: "))
    else:
        acceleration = "-"
    if finding != "net force":
        netForce = float(input("Enter the net force: "))
    else:
        netForce = "-"
    if finding != "weight":
        weight = float(input("Enter the weight: "))
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
if solvingFor == "force": # needs mass and acceleration (0, 2)
    if given[1] == "-":
        print("Sorry, Python Calculator cannot solve for force without mass. Please try again.")
    elif given[2] == "-":
        print("Sorry, Python Calculator cannot solve for force without acceleration. Please try again.")
    else:
        print("Force = " + str(force(given[1], given[2])) + " by using the equation F = ma")
elif solvingFor == "mass": # needs force and acceleration (0, 2)
    if given[0] == "-":
        print("Sorry, Python Calculator cannot solve for mass without force. Please try again.")
    elif given[2] == "-":
        print("Sorry, Python Calculator cannot solve for mass without acceleration. Please try again.")
    else:
        print("Mass = " + str(mass(given[0], given[2])) + " by using the equation m = F/a")
elif solvingFor == "acceleration": # needs force and mass (0, 1)
    if given[0] == "-":
        print("Sorry, Python Calculator cannot solve for acceleration without force. Please try again.")
    elif given[1] == "-":
        print("Sorry, Python Calculator cannot solve for acceleration without mass. Please try again.")
    else:
        print("Acceleration = " + str(acceleration(given[0], given[1])) + " by using the equation a = F/m")
elif solvingFor == "net force": # needs force1 and force2 (0, 3)
    if given[0] == "-":
        print("Sorry, Python Calculator cannot solve for net force without force1. Please try again.")
    elif given[3] == "-":
        print("Sorry, Python Calculator cannot solve for net force without force2. Please try again.")
    else:
        print("Net Force = " + str(netForce(given[0], given[3])) + " by using the equation Fnet = F1 + F2")
elif solvingFor == "weight": # needs mass and gravity (1, 4)
    if given[1] == "-":
        print("Sorry, Python Calculator cannot solve for weight without mass. Please try again.")
    elif given[4] == "-":
        print("Sorry, Python Calculator cannot solve for weight without gravity. Please try again.")
    else:
        print("Weight = " + str(weight(given[1], given[4])) + " by using the equation W = mg")
print("----------------------------------------")
# end of code



