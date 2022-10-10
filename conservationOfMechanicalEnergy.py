# conservationOfMechanicalEnergy.py - Conservation of Mechanical Energy Equations File
# By: Joshua Lim
# Date: 10/05/2022
# Version 0 Optimized

# imports
import math
import sys
import decimal

# EQUATIONS
# work
# - work = force * distance
# force
# - force = work / distance
# distance
# - distance = work / force
# kinetic energy
# - kinetic energy = 0.5 * mass * (velocity ** 2)
# mass
# - mass = kinetic energy / (0.5 * (velocity ** 2))
# velocity
# - velocity = math.sqrt(2 * kinetic energy / mass)

# function to ask what the user is trying to find
def findWhat():
    print("----------------------------------------")
    print("What are you trying to find?")
    print("1) Velocity")
    print("2) Distance")
    print("3) Height")
    print("4) Time")

# function to ask what variables are given
def givenVariables(finding):
    print("----------------------------------------")
    print("What variables are given? (enter '-' if it is not given)")
    if finding != "work":
        work = float(input("Enter the work: "))
    else:
        work = "-"
    if finding != "force":
        force = float(input("Enter the force: "))
    else:
        force = "-"
    if finding != "distance":
        distance = float(input("Enter the distance: "))
    else:
        distance = "-"
    if finding != "kinetic energy":
        kineticEnergy = float(input("Enter the kinetic energy: "))
    else:
        kineticEnergy = "-"
    if finding != "mass":
        mass = float(input("Enter the mass: "))
    else:
        mass = "-"
    if finding != "velocity":
        velocity = float(input("Enter the velocity: "))
    else:
        velocity = "-"
    return [work, force, distance, kineticEnergy, mass, velocity]

# function to calculate work
def calculateWork(force, distance):
    work = force * distance
    return work

# function to calculate force
def calculateForce(work, distance):
    force = work / distance
    return force

# function to calculate distance
def calculateDistance(work, force):
    distance = work / force
    return distance

# function to calculate kinetic energy
def calculateKineticEnergy(mass, velocity):
    kineticEnergy = 0.5 * mass * velocity ** 2
    return kineticEnergy

# function to calculate mass
def calculateMass(kineticEnergy, velocity):
    mass = kineticEnergy / (0.5 * velocity ** 2)
    return mass

# function to calculate velocity
def calculateVelocity(kineticEnergy, mass):
    velocity = math.sqrt(2 * kineticEnergy / mass)
    return velocity

# run the code
# given list structure: [work, force, distance, kineticEnergy, mass, velocity]
#                          0     1        2           3          4       5
solvingFor = findWhat()
given = givenVariables(solvingFor)
print("----------------------------------------")
if solvingFor == "work": # needs force and distance (1, 2)
    if given[1] == "-":
        print("Sorry, Python Calulator cannot solve for work without force. Please try again.")
    elif given[2] == "-":
        print("Sorry, Python Calulator cannot solve for work without distance. Please try again.")
    else:
        print("Work = ", calculateWork(given[1], given[2]) + " by using the equation work = force * distance.")
elif solvingFor == "force": # needs work and distance (1, 3)
    if given[0] == "-":
        print("Sorry, Python Calulator cannot solve for force without work. Please try again.")
    elif given[2] == "-":
        print("Sorry, Python Calulator cannot solve for force without distance. Please try again.")
    else:
        print("Force = ", calculateForce(given[0], given[2]) + " by using the equation force = work / distance.")
elif solvingFor == "distance": # needs work and force (1, 2)
    if given[0] == "-":
        print("Sorry, Python Calulator cannot solve for distance without work. Please try again.")
    elif given[1] == "-":
        print("Sorry, Python Calulator cannot solve for distance without force. Please try again.")
    else:
        print("Distance = ", calculateDistance(given[0], given[1]) + " by using the equation distance = work / force.")
elif solvingFor == "kinetic energy": # needs mass and velocity (4, 5)
    if given[4] == "-":
        print("Sorry, Python Calulator cannot solve for kinetic energy without mass. Please try again.")
    elif given[5] == "-":
        print("Sorry, Python Calulator cannot solve for kinetic energy without velocity. Please try again.")
    else:
        print("Kinetic Energy = ", calculateKineticEnergy(given[4], given[5]) + " by using the equation kinetic energy = 0.5 * mass * velocity ** 2.")
elif solvingFor == "mass": # needs kinetic energy and velocity (3, 4)
    if given[3] == "-":
        print("Sorry, Python Calulator cannot solve for mass without kinetic energy. Please try again.")
    elif given[5] == "-":
        print("Sorry, Python Calulator cannot solve for mass without velocity. Please try again.")
    else:
        print("Mass = ", calculateMass(given[3], given[5]) + " by using the equation mass = kinetic energy / (0.5 * velocity ** 2).")
elif solvingFor == "velocity": # needs kinetic energy and mass (3, 4)
    if given[3] == "-":
        print("Sorry, Python Calulator cannot solve for velocity without kinetic energy. Please try again.")
    elif given[4] == "-":
        print("Sorry, Python Calulator cannot solve for velocity without mass. Please try again.")
    else:
        print("Velocity = ", calculateVelocity(given[3], given[4]) + " by using the equation velocity = sqrt(2 * kinetic energy / mass).")
print("----------------------------------------")
# end of code