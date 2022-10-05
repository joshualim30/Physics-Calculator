# motion1D.py - Motion in 1D Equations File
# By: Joshua Lim
# Date: 10/04/2022

# imports
# import math

# function to ask what the user is trying to find
def findWhat():
    print("What are you trying to find?")
    print("1. Initial Velocity")
    print("2. Final Velocity")
    print("3. Acceleration")
    print("4. Time")
    print("5. Distance")
    choice = int(input("Enter the number of the variable you are trying to find: "))
    if choice == 1:
        return "initial velocity"
    elif choice == 2:
        return "final velocity"
    elif choice == 3:
        return "acceleration"
    elif choice == 4:
        return "time"
    elif choice == 5:
        return "distance"
    else:
        print("Please enter a valid number.")
        findWhat()

# function to ask what variables are given
def givenVariables(finding):
    print("What variables are given? (enter '-' if it is not given)")
    if finding != "initial velocity":
        initialVelocity = int(input("Enter the initial velocity: "))
    else:
        initialVelocity = "-"
    if finding != "final velocity":
        finalVelocity = int(input("Enter the final velocity: "))
    else:
        finalVelocity = "-"
    if finding != "acceleration":
        acceleration = int(input("Enter the acceleration: "))
    else:
        acceleration = "-"
    if finding != "time":
        time = int(input("Enter the time: "))
    else:
        time = "-"
    if finding != "distance":
        distance = int(input("Enter the distance: "))
    else:
        distance = "-"
    return [initialVelocity, finalVelocity, acceleration, time, distance]

# function to solve for initial velocity
def initialVelocity(finalVelocity, acceleration, time, distance):
    return finalVelocity - (acceleration * time) - (distance / time)

# function to solve for final velocity
def finalVelocity(initialVelocity, acceleration, time, distance):
    return initialVelocity + (acceleration * time) + (distance / time)

# function to solve for acceleration
def acceleration(initialVelocity, finalVelocity, time, distance):
    return (finalVelocity - initialVelocity - distance / time) / time

# function to solve for time
def time(initialVelocity, finalVelocity, acceleration, distance):
    return (finalVelocity - initialVelocity - distance / acceleration) / acceleration

# function to solve for distance
def distance(initialVelocity, finalVelocity, acceleration, time):
    return (finalVelocity - initialVelocity - acceleration * time) * time

# run code here
# given list structure: [initial velocity, final velocity, acceleration, time, distance]
#                               0               1               2          3       4
solvingFor = findWhat()
given = givenVariables(solvingFor)
if solvingFor == "initial velocity": # needs final velocity, acceleration, time, distance
    if given[1] == "-":
        print("Sorry, Python Calculator cannot solve for initial velocity without final velocity. Please try again.")
    elif given[2] == "-":
        print("Sorry, Python Calculator cannot solve for initial velocity without acceleration. Please try again.")
    elif given[3] == "-":
        print("Sorry, Python Calculator cannot solve for initial velocity without time. Please try again.")
    elif given[4] == "-":
        print("Sorry, Python Calculator cannot solve for initial velocity without distance. Please try again.")
    else:
        solution = initialVelocity(given[1], given[2], given[3], given[4])
        print("The initial velocity is " + str(solution) + " by using the formula v = v0 + at + d/t.")
elif solvingFor == "final velocity": # needs initial velocity, acceleration, time, distance
    if given[0] == "-":
        print("Sorry, Python Calculator cannot solve for final velocity without initial velocity. Please try again.")
    elif given[2] == "-":
        print("Sorry, Python Calculator cannot solve for final velocity without acceleration. Please try again.")
    elif given[3] == "-":
        print("Sorry, Python Calculator cannot solve for final velocity without time. Please try again.")
    elif given[4] == "-":
        print("Sorry, Python Calculator cannot solve for final velocity without distance. Please try again.")
    else:
        solution = finalVelocity(given[0], given[2], given[3], given[4])
        print("The final velocity is " + str(solution) + " by using the formula v = v0 + at + d/t.")
elif solvingFor == "acceleration": # needs initial velocity, final velocity, time, distance
    if given[0] == "-":
        print("Sorry, Python Calculator cannot solve for acceleration without initial velocity. Please try again.")
    elif given[1] == "-":
        print("Sorry, Python Calculator cannot solve for acceleration without final velocity. Please try again.")
    elif given[3] == "-":
        print("Sorry, Python Calculator cannot solve for acceleration without time. Please try again.")
    elif given[4] == "-":
        print("Sorry, Python Calculator cannot solve for acceleration without distance. Please try again.")
    else:
        solution = acceleration(given[0], given[1], given[3], given[4])
        print("The acceleration is " + str(solution) + " by using the formula a = (v - v0 - d/t) / t.")
elif solvingFor == "time": # needs initial velocity, final velocity, acceleration, distance
    if given[0] == "-":
        print("Sorry, Python Calculator cannot solve for time without initial velocity. Please try again.")
    elif given[1] == "-":
        print("Sorry, Python Calculator cannot solve for time without final velocity. Please try again.")
    elif given[2] == "-":
        print("Sorry, Python Calculator cannot solve for time without acceleration. Please try again.")
    elif given[4] == "-":
        print("Sorry, Python Calculator cannot solve for time without distance. Please try again.")
    else:
        solution = time(given[0], given[1], given[2], given[4])
        print("The time is " + str(solution) + " by using the formula t = (v - v0 - d/a) / a.")
elif solvingFor == "distance": # needs initial velocity, final velocity, acceleration, time
    if given[0] == "-":
        print("Sorry, Python Calculator cannot solve for distance without initial velocity. Please try again.")
    elif given[1] == "-":
        print("Sorry, Python Calculator cannot solve for distance without final velocity. Please try again.")
    elif given[2] == "-":
        print("Sorry, Python Calculator cannot solve for distance without acceleration. Please try again.")
    elif given[3] == "-":
        print("Sorry, Python Calculator cannot solve for distance without time. Please try again.")
    else:
        solution = distance(given[0], given[1], given[2], given[3])
        print("The distance is " + str(solution) + " by using the formula d = (v - v0 - a*t) * t.")
# end of code