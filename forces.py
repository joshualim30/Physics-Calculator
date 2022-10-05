# forces.py - Forces Equations File
# By: Joshua Lim
# Date: 10/04/2022

# imports
import math

# function to ask what variables are given
def givenVariables():
    print("What variables are given? (enter '-' if it is not given)")
    mass = input("Enter the mass: ")
    acceleration = input("Enter the acceleration: ")
    force = input("Enter the force: ")
    solving = solvingFor()
    if solving == "mass":
        solution = mass(acceleration, force)
        print("The mass is " + str(solution))
    elif solving == "acceleration":
        solution = acceleration(mass, force)
        print("The acceleration is " + str(solution))
    elif solving == "force":
        solution = force(mass, acceleration)
        print("The force is " + str(solution))

# function to ask what variables are being solved for
def solvingFor():
    print("What variable are you solving for?")
    print("1. Mass")
    print("2. Acceleration")
    print("3. Force")
    choice = int(input("Enter the number of the variable you are solving for: "))
    if choice == 1:
        return "mass"
    elif choice == 2:
        return "acceleration"
    elif choice == 3:
        return "force"
    else:
        print("Please enter a valid number.")

# function to calculate mass
def mass(acceleration, force):
    return force / acceleration

# function to calculate acceleration
def acceleration(mass, force):
    return force / mass

# function to calculate force
def force(mass, acceleration):
    return mass * acceleration

# main function
givenVariables()