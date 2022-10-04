# motion1D.py - Motion in 1D Equations File
# By: Joshua Lim
# Date: 10/04/2022

# imports
import math

# function to ask what variables are given
def givenVariables():
    print("What variables are given? (enter '-' if it is not given)")
    initialVelocity = input("Enter the initial velocity: ")
    finalVelocity = input("Enter the final velocity: ")
    acceleration = input("Enter the acceleration: ")
    time = input("Enter the time: ")
    distance = input("Enter the distance: ")
    solving = solvingFor()
    if solving == "initialVelocity":
        solution = initialVelocity(finalVelocity, acceleration, time, distance)
        print("The initial velocity is " + str(solution))
    elif solving == "finalVelocity":
        solution = finalVelocity(initialVelocity, acceleration, time, distance)
        print("The final velocity is " + str(solution))
    elif solving == "acceleration":
        solution = acceleration(initialVelocity, finalVelocity, time, distance)
        print("The acceleration is " + str(solution))
    elif solving == "time":
        solution = time(initialVelocity, finalVelocity, acceleration, distance)
        print("The time is " + str(solution))
    elif solving == "distance":
        solution = distance(initialVelocity, finalVelocity, acceleration, time)
        print("The distance is " + str(solution))
    
# function to ask what variables are being solved for
def solvingFor():
    print("What variable are you solving for?")
    print("1. Initial Velocity")
    print("2. Final Velocity")
    print("3. Acceleration")
    print("4. Time")
    print("5. Distance")
    choice = int(input("Enter the number of the variable you are solving for: "))
    if choice == 1:
        return "initialVelocity"
    elif choice == 2:
        return "finalVelocity"
    elif choice == 3:
        return "acceleration"
    elif choice == 4:
        return "time"
    elif choice == 5:
        return "distance"
    else:
        print("Please enter a valid number.")
        solvingFor()

# function to solve for initial velocity
def initialVelocity(finalVelocity, acceleration, time, distance):
    if finalVelocity == "-":
        finalVelocity = 0
    if acceleration == "-":
        acceleration = 0
    if time == "-":
        time = 0
    if distance == "-":
        distance = 0
    return finalVelocity - (acceleration * time) - (distance / time)

# function to solve for final velocity
def finalVelocity(initialVelocity, acceleration, time, distance):
    if initialVelocity == "-":
        initialVelocity = 0
    if acceleration == "-":
        acceleration = 0
    if time == "-":
        time = 0
    if distance == "-":
        distance = 0
    return initialVelocity + (acceleration * time) + (distance / time)

# function to solve for acceleration
def acceleration(initialVelocity, finalVelocity, time, distance):
    if initialVelocity == "-":
        initialVelocity = 0
    if finalVelocity == "-":
        finalVelocity = 0
    if time == "-":
        time = 0
    if distance == "-":
        distance = 0
    return (finalVelocity - initialVelocity) / time - (distance / (time ** 2))

# function to solve for time
def time(initialVelocity, finalVelocity, acceleration, distance):
    if initialVelocity == "-":
        initialVelocity = 0
    if finalVelocity == "-":
        finalVelocity = 0
    if acceleration == "-":
        acceleration = 0
    if distance == "-":
        distance = 0
    return (finalVelocity - initialVelocity) / acceleration - (distance / (acceleration ** 2))

# function to solve for distance
def distance(initialVelocity, finalVelocity, acceleration, time):
    if initialVelocity == "-":
        initialVelocity = 0
    if finalVelocity == "-":
        finalVelocity = 0
    if acceleration == "-":
        acceleration = 0
    if time == "-":
        time = 0
    return (finalVelocity - initialVelocity) * time - (acceleration * (time ** 2))

# main function
def main():
    givenVariables()