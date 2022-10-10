# circularMotion.py - Circular Motion Equations File
# By: Joshua Lim
# Date: 10/04/2022
# Version 0 Optimized

# imports
import math
import sys
import decimal

# CIRCULAR MOTION EQUATIONS
# initial velocity

# function to ask what the user is trying to find for circular motion
def findWhat():
    print("----------------------------------------")
    print("What are you trying to find?")
    print("1) Centripetal Force")


# function to ask what variables are given for circular motion
def givenVariables(finding):
    print("----------------------------------------")
    print("What variables are given? (enter '-' if it is not given)")
    if finding != "initial velocity":
        initialVelocity = float(input("Enter the initial velocity: "))
    else:
        initialVelocity = "-"
    if finding != "final velocity":
        finalVelocity = float(input("Enter the final velocity: "))
    else:
        finalVelocity = "-"
    if finding != "acceleration":
        acceleration = float(input("Enter the acceleration: "))
    else:
        acceleration = "-"
    if finding != "time":
        time = float(input("Enter the time: "))
    else:
        time = "-"
    if finding != "distance":
        distance = float(input("Enter the distance: "))
    else:
        distance = "-"
    if finding != "centripetal force":
        centripetalForce = float(input("Enter the centripetal force: "))
    else:
        centripetalForce = "-"
    if finding != "centripetal acceleration":
        centripetalAcceleration = float(input("Enter the centripetal acceleration: "))
    else:
        centripetalAcceleration = "-"
    if finding != "angular velocity":
        angularVelocity = float(input("Enter the angular velocity: "))
    else:
        angularVelocity = "-"
    if finding != "angular acceleration":
        angularAcceleration = float(input("Enter the angular acceleration: "))
    else:
        angularAcceleration = "-"
    if finding != "tangential velocity":
        tangentialVelocity = float(input("Enter the tangential velocity: "))
    else:
        tangentialVelocity = "-"
    if finding != "tangential acceleration":
        tangentialAcceleration = float(input("Enter the tangential acceleration: "))
    else:
        tangentialAcceleration = "-"
    if finding != "radius":
        radius = float(input("Enter the radius: "))
    else:
        radius = "-"
    if finding != "centripetal velocity":
        centripetalVelocity = float(input("Enter the centripetal velocity: "))
    else:
        centripetalVelocity = "-"
    return [initialVelocity, finalVelocity, acceleration, time, distance, centripetalForce, centripetalAcceleration, angularVelocity, angularAcceleration, tangentialVelocity, tangentialAcceleration, radius, centripetalVelocity]

# function to solve for initial velocity for circular motion
def initialVelocity(finalVelocity, acceleration, time, distance):
    return finalVelocity - (acceleration * time) - (distance / time)

# function to solve for final velocity for circular motion
def finalVelocity(initialVelocity, acceleration, time, distance):
    return initialVelocity + (acceleration * time) + (distance / time)

# function to solve for acceleration for circular motion
def acceleration(initialVelocity, finalVelocity, time, distance):
    return (finalVelocity - initialVelocity - (distance / time)) / time

# function to solve for time for circular motion
def time(initialVelocity, finalVelocity, acceleration, distance): # broken function
    return (finalVelocity - initialVelocity - (distance / time)) / acceleration

# function to solve for distance for circular motion
def distance(initialVelocity, finalVelocity, acceleration, time):
    return (initialVelocity + finalVelocity) * time + (acceleration * (time ** 2)) / 2
    
# function to solve for centripetal force for circular motion
def centripetalForce(centripetalAcceleration, mass):
    return centripetalAcceleration * mass

# function to solve for centripetal acceleration for circular motion
def centripetalAcceleration(centripetalForce, mass):
    return centripetalForce / mass

# function to solve for angular velocity for circular motion
def angularVelocity(angularAcceleration, time):
    return angularAcceleration * time

# function to solve for angular acceleration for circular motion
def angularAcceleration(angularVelocity, time):
    return angularVelocity / time

# function to solve for tangential velocity for circular motion
def tangentialVelocity(angularVelocity, radius):
    return angularVelocity * radius

# function to solve for tangential acceleration for circular motion
def tangentialAcceleration(angularAcceleration, radius):
    return angularAcceleration * radius

# function to solve for radius
def radius(centripetalVelocity, time):
    return centripetalVelocity * time / (2 * math.pi)

# function to solve for centripetal velocity
def centripetalVelocity(radius, time):
    return 2 * math.pi * radius / time

# run the code
# given list structure [initialVelocity, finalVelocity, acceleration, time, distance, centripetalForce, centripetalAcceleration, angularVelocity, angularAcceleration, tangentialVelocity, tangentialAcceleration]
#                              0               1              2         3       4            5                     6                   7                   8                   9                     10
solvingFor = findWhat()
given = givenVariables(solvingFor)
print("----------------------------------------")
if solvingFor == "initial velocity": # needs final velocity, acceleration, time, distance (1, 2, 3, 4)
    if given[1] == "-":
        print("Sorry, Python Calculator cannot solve for initail velocity without final velocity.")
    elif given[2] == "-":
        print("Sorry, Python Calculator cannot solve for initail velocity without acceleration.")
    elif given[3] == "-":
        print("Sorry, Python Calculator cannot solve for initail velocity without time.")
    elif given[4] == "-":
        print("Sorry, Python Calculator cannot solve for initail velocity without distance.")
    else:
        print("Initial Velocity = ", str(initialVelocity(given[1], given[2], given[3], given[4])) + " by using the equation v = v0 + at + d/t")
elif solvingFor == "final velocity": # needs initial velocity, acceleration, time, distance (0, 2, 3, 4)
    if given[0] == "-":
        print("Sorry, Python Calculator cannot solve for final velocity without initial velocity.")
    elif given[2] == "-":
        print("Sorry, Python Calculator cannot solve for final velocity without acceleration.")
    elif given[3] == "-":
        print("Sorry, Python Calculator cannot solve for final velocity without time.")
    elif given[4] == "-":
        print("Sorry, Python Calculator cannot solve for final velocity without distance.")
    else:
        print("Final Velocity = ", str(finalVelocity(given[0], given[2], given[3], given[4])) + " by using the equation v = v0 + at + d/t")
elif solvingFor == "acceleration": # needs initial velocity, final velocity, time, distance (0, 1, 3, 4)
    if given[0] == "-":
        print("Sorry, Python Calculator cannot solve for acceleration without initial velocity.")
    elif given[1] == "-":
        print("Sorry, Python Calculator cannot solve for acceleration without final velocity.")
    elif given[3] == "-":
        print("Sorry, Python Calculator cannot solve for acceleration without time.")
    elif given[4] == "-":
        print("Sorry, Python Calculator cannot solve for acceleration without distance.")
    else:
        print("Acceleration = ", str(acceleration(given[0], given[1], given[3], given[4])) + " by using the equation a = (v - v0 - d/t) / t")
elif solvingFor == "time": # needs initial velocity, final velocity, acceleration, distance (0, 1, 2, 4)
    print("Sorry, Python Calculator cannot solve for time as of Version 0.")
    # if given[0] == "-":
    #     print("Sorry, Python Calculator cannot solve for time without initial velocity.")
    # elif given[1] == "-":
    #     print("Sorry, Python Calculator cannot solve for time without final velocity.")
    # elif given[2] == "-":
    #     print("Sorry, Python Calculator cannot solve for time without acceleration.")
    # elif given[4] == "-":
    #     print("Sorry, Python Calculator cannot solve for time without distance.")
    # else:
    #     print("Time = ", str(time(given[0], given[1], given[2], given[4])) + " by using the equation t = (v - v0 - d/t) / a")
elif solvingFor == "distance": # needs initial velocity, final velocity, acceleration, time (0, 1, 2, 3)
    if given[0] == "-":
        print("Sorry, Python Calculator cannot solve for distance without initial velocity.")
    elif given[1] == "-":
        print("Sorry, Python Calculator cannot solve for distance without final velocity.")
    elif given[2] == "-":
        print("Sorry, Python Calculator cannot solve for distance without acceleration.")
    elif given[3] == "-":
        print("Sorry, Python Calculator cannot solve for distance without time.")
    else:
        print("Distance = ", str(distance(given[0], given[1], given[2], given[3])) + " by using the equation d = (v + v0) * t + (a * t^2) / 2")
elif solvingFor == "centripetal force": # needs centripetal acceleration, mass (6, 7)
    if given[6] == "-":
        print("Sorry, Python Calculator cannot solve for centripetal force without centripetal acceleration.")
    elif given[7] == "-":
        print("Sorry, Python Calculator cannot solve for centripetal force without mass.")
    else:
        print("Centripetal Force = ", str(centripetalForce(given[6], given[7])) + " by using the equation F = ma")
elif solvingFor == "centripetal acceleration": # needs centripetal force, mass (5, 7)
    if given[5] == "-":
        print("Sorry, Python Calculator cannot solve for centripetal acceleration without centripetal force.")
    elif given[7] == "-":
        print("Sorry, Python Calculator cannot solve for centripetal acceleration without mass.")
    else:
        print("Centripetal Acceleration = ", str(centripetalAcceleration(given[5], given[7])) + " by using the equation a = F / m")
elif solvingFor == "angular velocity": # needs angular acceleration, time (8, 9)
    if given[8] == "-":
        print("Sorry, Python Calculator cannot solve for angular velocity without angular acceleration.")
    elif given[9] == "-":
        print("Sorry, Python Calculator cannot solve for angular velocity without time.")
    else:
        print("Angular Velocity = ", str(angularVelocity(given[8], given[9])) + " by using the equation w = at")
elif solvingFor == "angular acceleration": # needs angular velocity, time (7, 9)
    if given[7] == "-":
        print("Sorry, Python Calculator cannot solve for angular acceleration without angular velocity.")
    elif given[9] == "-":
        print("Sorry, Python Calculator cannot solve for angular acceleration without time.")
    else:
        print("Angular Acceleration = ", str(angularAcceleration(given[7], given[9])) + " by using the equation a = w / t")
elif solvingFor == "tangential velocity": # needs radius, angular velocity (10, 7)
    if given[10] == "-":
        print("Sorry, Python Calculator cannot solve for tangential velocity without radius.")
    elif given[7] == "-":
        print("Sorry, Python Calculator cannot solve for tangential velocity without angular velocity.")
    else:
        print("Tangential Velocity = ", str(tangentialVelocity(given[10], given[7])) + " by using the equation v = r * w")
elif solvingFor == "radius": # needs tangential velocity, angular velocity (11, 7)
    if given[11] == "-":
        print("Sorry, Python Calculator cannot solve for radius without tangential velocity.")
    elif given[7] == "-":
        print("Sorry, Python Calculator cannot solve for radius without angular velocity.")
    else:
        print("Radius = ", str(radius(given[11], given[7])) + " by using the equation r = v / w")
elif solvingFor == "centripetal velocity": # needs radius, angular velocity (10, 7)
    if given[10] == "-":
        print("Sorry, Python Calculator cannot solve for centripetal velocity without radius.")
    elif given[7] == "-":
        print("Sorry, Python Calculator cannot solve for centripetal velocity without angular velocity.")
    else:
        print("Centripetal Velocity = ", str(centripetalVelocity(given[10], given[7])) + " by using the equation v = r * w")
print("----------------------------------------")
# end of code
