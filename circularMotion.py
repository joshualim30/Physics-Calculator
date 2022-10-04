# circularMotion.py - Circular Motion Equations File
# By: Joshua Lim
# Date: 10/04/2022

# imports
import math

# function to ask what variables are given
def givenVariables():
    print("What variables are given? (enter '-' if it is not given)")
    radius = input("Enter the radius: ")
    angularVelocity = input("Enter the angular velocity: ")
    angularAcceleration = input("Enter the angular acceleration: ")
    time = input("Enter the time: ")
    angle = input("Enter the angle: ")
    solving = solvingFor()
    if solving == "radius":
        solution = radius(angularVelocity, angularAcceleration, time, angle)
        print("The radius is " + str(solution))
    elif solving == "angularVelocity":
        solution = angularVelocity(radius, angularAcceleration, time, angle)
        print("The angular velocity is " + str(solution))
    elif solving == "angularAcceleration":
        solution = angularAcceleration(radius, angularVelocity, time, angle)
        print("The angular acceleration is " + str(solution))
    elif solving == "time":
        solution = time(radius, angularVelocity, angularAcceleration, angle)
        print("The time is " + str(solution))
    elif solving == "angle":
        solution = angle(radius, angularVelocity, angularAcceleration, time)
        print("The angle is " + str(solution))

# function to ask what variables are being solved for
def solvingFor():
    print("What variable are you solving for?")
    print("1. Radius")
    print("2. Angular Velocity")
    print("3. Angular Acceleration")
    print("4. Time")
    print("5. Angle")
    choice = int(input("Enter the number of the variable you are solving for: "))
    if choice == 1:
        return "radius"
    elif choice == 2:
        return "angularVelocity"
    elif choice == 3:
        return "angularAcceleration"
    elif choice == 4:
        return "time"
    elif choice == 5:
        return "angle"
    else:
        print("Please enter a valid number.")
        solvingFor()

# function to solve for radius
def radius(angularVelocity, angularAcceleration, time, angle):
    if angularVelocity == "-":
        angularVelocity = 0
    if angularAcceleration == "-":
        angularAcceleration = 0
    if time == "-":
        time = 0
    if angle == "-":
        angle = 0
    return (angularVelocity * time) / angle

# function to solve for angular velocity
def angularVelocity(radius, angularAcceleration, time, angle):
    if radius == "-":
        radius = 0
    if angularAcceleration == "-":
        angularAcceleration = 0
    if time == "-":
        time = 0
    if angle == "-":
        angle = 0
    return (radius * angle) / time

# function to solve for angular acceleration
def angularAcceleration(radius, angularVelocity, time, angle):
    if radius == "-":
        radius = 0
    if angularVelocity == "-":
        angularVelocity = 0
    if time == "-":
        time = 0
    if angle == "-":
        angle = 0
    return (radius * angle) / (time * time)

# function to solve for time
def time(radius, angularVelocity, angularAcceleration, angle):
    if radius == "-":
        radius = 0
    if angularVelocity == "-":
        angularVelocity = 0
    if angularAcceleration == "-":
        angularAcceleration = 0
    if angle == "-":
        angle = 0
    return (radius * angle) / angularVelocity

# function to solve for angle
def angle(radius, angularVelocity, angularAcceleration, time):
    if radius == "-":
        radius = 0
    if angularVelocity == "-":
        angularVelocity = 0
    if angularAcceleration == "-":
        angularAcceleration = 0
    if time == "-":
        time = 0
    return (radius * time) / angularVelocity

# main function
def main():
    givenVariables()