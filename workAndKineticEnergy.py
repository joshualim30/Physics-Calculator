# workAndKineticEnergy.py - Work and Kinetic Energy Equations File
# By: Joshua Lim
# Date: 10/04/2022

# imports
import math

# function to ask what variables are given
def givenVariables():
    print("What variables are given? (enter '-' if it is not given)")
    force = input("Enter the force: ")
    distance = input("Enter the distance: ")
    work = input("Enter the work: ")
    kineticEnergy = input("Enter the kinetic energy: ")
    solving = solvingFor()
    if solving == "force":
        solution = force(distance, work, kineticEnergy)
        print("The force is " + str(solution))
    elif solving == "distance":
        solution = distance(force, work, kineticEnergy)
        print("The distance is " + str(solution))
    elif solving == "work":
        solution = work(force, distance, kineticEnergy)
        print("The work is " + str(solution))
    elif solving == "kineticEnergy":
        solution = kineticEnergy(force, distance, work)
        print("The kinetic energy is " + str(solution))

# function to ask what variables are being solved for
def solvingFor():
    print("What variable are you solving for?")
    print("1. Force")
    print("2. Distance")
    print("3. Work")
    print("4. Kinetic Energy")
    choice = int(input("Enter the number of the variable you are solving for: "))
    if choice == 1:
        return "force"
    elif choice == 2:
        return "distance"
    elif choice == 3:
        return "work"
    elif choice == 4:
        return "kineticEnergy"
    else:
        print("Please enter a valid number.")

# function to calculate force
def force(distance, work, kineticEnergy):
    return work / distance

# function to calculate distance
def distance(force, work, kineticEnergy):
    return work / force

# function to calculate work
def work(force, distance, kineticEnergy):
    return force * distance

# function to calculate kinetic energy
def kineticEnergy(force, distance, work):
    return work / distance

# main function
givenVariables()