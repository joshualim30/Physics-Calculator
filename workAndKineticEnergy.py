# workAndKineticEnergy.py - Work and Kinetic Energy Equations File
# By: Joshua Lim
# Date: 10/04/2022
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
    print("1. Work")
    print("2. Force")
    print("3. Distance")
    print("4. Kinetic Energy")
    print("5. Mass")
    print("6. Velocity")    
    choice = float(input("Enter the number of the variable you are trying to find: "))
    if choice == 1:
        return "work"
    elif choice == 2:
        return "force"
    elif choice == 3:
        return "distance"
    elif choice == 4:
        return "kinetic energy"
    elif choice == 5:
        return "mass"
    elif choice == 6:
        return "velocity"
    else:
        print("Please enter a valid number.")
        findWhat()

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

# function to solve for work
def work(force, distance):
    return force * distance

# function to solve for force
def force(work, distance):
    return work / distance

# function to solve for distance
def distance(work, force):
    return work / force

# function to solve for kinetic energy
def kineticEnergy(mass, velocity):
    return 0.5 * mass * (velocity ** 2)

# function to solve for mass
def mass(kineticEnergy, velocity):
    return kineticEnergy / (0.5 * (velocity ** 2))

# function to solve for velocity
def velocity(kineticEnergy, mass):
    return math.sqrt(2 * kineticEnergy / mass)

# run the code
# given list structure [work, force, distance, kineticEnergy, mass, velocity]
#                         0     1       2           3           4       5
solvingFor = findWhat()
given = givenVariables(solvingFor)
print("----------------------------------------")
if solvingFor == "work": # needs force and distance (1, 2)
    if given[1] == "-":
        print("Sorry, Python Calculator cannot solve for work without force. Please try again.")
    elif given[2] == "-":
        print("Sorry, Python Calculator cannot solve for work without distance. Please try again.")
    else:
        print("Work = ", str(work(given[1], given[2])) + " by using the equation work = force * distance.")
elif solvingFor == "force": # needs work and distance (1, 3)
    if given[0] == "-":
         print("Sorry, Python Calculator cannot solve for force without work. Please try again.")
    elif given[2] == "-":
        print("Sorry, Python Calculator cannot solve for force without distance. Please try again.")
    else:
        print("Force = ", str(force(given[0], given[2])) + " by using the equation force = work / distance.")
elif solvingFor == "distance": # needs work and force (1, 2)
    if given[0] == "-":
        print("Sorry, Python Calculator cannot solve for distance without work. Please try again.")
    elif given[1] == "-":
        print("Sorry, Python Calculator cannot solve for distance without force. Please try again.")
    else:
        print("Distance = ", str(distance(given[0], given[1])) + " by using the equation distance = work / force.")
elif solvingFor == "kinetic energy": # needs mass and velocity (4, 5)
    if given[4] == "-":
        print("Sorry, Python Calculator cannot solve for kinetic energy without mass. Please try again.")
    elif given[5] == "-":
        print("Sorry, Python Calculator cannot solve for kinetic energy without velocity. Please try again.")
    else:
        print("Kinetic Energy = ", str(kineticEnergy(given[4], given[5])) + " by using the equation kinetic energy = 0.5 * mass * velocity^2.")
elif solvingFor == "mass": # needs kinetic energy and velocity (4, 5)
    if given[3] == "-":
        print("Sorry, Python Calculator cannot solve for mass without kinetic energy. Please try again.")
    elif given[5] == "-":
        print("Sorry, Python Calculator cannot solve for mass without velocity. Please try again.")
    else:
        print("Mass = ", str(mass(given[3], given[5])) + " by using the equation mass = kinetic energy / (0.5 * velocity^2).")
elif solvingFor == "velocity": # needs kinetic energy and mass (4, 5)
    if given[3] == "-":
        print("Sorry, Python Calculator cannot solve for velocity without kinetic energy. Please try again.")
    elif given[4] == "-":
        print("Sorry, Python Calculator cannot solve for velocity without mass. Please try again.")
    else:
        print("Velocity = ", str(velocity(given[3], given[4])) + " by using the equation velocity = sqrt(2 * kinetic energy / mass).")
print("----------------------------------------")
# end of code

