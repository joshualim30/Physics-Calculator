# vectorAlgebra.py - Vector Algebra Equations File
# By: Joshua Lim
# Date: 10/04/2022

# imports
import math

# function to ask what variables are given
def givenVariables():
    print("What variables are given? (enter '-' if it is not given)")
    x1 = input("Enter the x1 value: ")
    y1 = input("Enter the y1 value: ")
    x2 = input("Enter the x2 value: ")
    y2 = input("Enter the y2 value: ")
    magnitude = input("Enter the magnitude: ")
    angle = input("Enter the angle: ")
    solving = solvingFor()
    if solving == "x1":
        solution = x1(y1, x2, y2, magnitude, angle)
        print("The x1 value is " + str(solution))
    elif solving == "y1":
        solution = y1(x1, x2, y2, magnitude, angle)
        print("The y1 value is " + str(solution))
    elif solving == "x2":
        solution = x2(x1, y1, y2, magnitude, angle)
        print("The x2 value is " + str(solution))
    elif solving == "y2":
        solution = y2(x1, y1, x2, magnitude, angle)
        print("The y2 value is " + str(solution))
    elif solving == "magnitude":
        solution = magnitude(x1, y1, x2, y2, angle)
        print("The magnitude is " + str(solution))
    elif solving == "angle":
        solution = angle(x1, y1, x2, y2, magnitude)
        print("The angle is " + str(solution))

# function to ask what variables are being solved for
def solvingFor():
    print("What variable are you solving for?")
    print("1. x1")
    print("2. y1")
    print("3. x2")
    print("4. y2")
    print("5. Magnitude")
    print("6. Angle")
    choice = int(input("Enter the number of the variable you are solving for: "))
    if choice == 1:
        return "x1"
    elif choice == 2:
        return "y1"
    elif choice == 3:
        return "x2"
    elif choice == 4:
        return "y2"
    elif choice == 5:
        return "magnitude"
    elif choice == 6:
        return "angle"
    else:
        print("Please enter a valid number.")
        solvingFor()
    
# function to solve for x1
def x1(y1, x2, y2, magnitude, angle):
    if y1 == "-":
        y1 = 0
    if x2 == "-":
        x2 = 0
    if y2 == "-":
        y2 = 0
    if magnitude == "-":
        magnitude = 0
    if angle == "-":
        angle = 0
    return x2 - magnitude * math.cos(math.radians(angle))

# function to solve for y1
def y1(x1, x2, y2, magnitude, angle):
    if x1 == "-":
        x1 = 0
    if x2 == "-":
        x2 = 0
    if y2 == "-":
        y2 = 0
    if magnitude == "-":
        magnitude = 0
    if angle == "-":
        angle = 0
    return y2 - magnitude * math.sin(math.radians(angle))

# function to solve for x2
def x2(x1, y1, y2, magnitude, angle):
    if x1 == "-":
        x1 = 0
    if y1 == "-":
        y1 = 0
    if y2 == "-":
        y2 = 0
    if magnitude == "-":
        magnitude = 0
    if angle == "-":
        angle = 0
    return x1 + magnitude * math.cos(math.radians(angle))

# function to solve for y2
def y2(x1, y1, x2, magnitude, angle):
    if x1 == "-":
        x1 = 0
    if y1 == "-":
        y1 = 0
    if x2 == "-":
        x2 = 0
    if magnitude == "-":
        magnitude = 0
    if angle == "-":
        angle = 0
    return y1 + magnitude * math.sin(math.radians(angle))

# function to solve for magnitude
def magnitude(x1, y1, x2, y2, angle):
    if x1 == "-":
        x1 = 0
    if y1 == "-":
        y1 = 0
    if x2 == "-":
        x2 = 0
    if y2 == "-":
        y2 = 0
    if angle == "-":
        angle = 0
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# function to solve for angle
def angle(x1, y1, x2, y2, magnitude):
    if x1 == "-":
        x1 = 0
    if y1 == "-":
        y1 = 0
    if x2 == "-":
        x2 = 0
    if y2 == "-":
        y2 = 0
    if magnitude == "-":
        magnitude = 0
    return math.degrees(math.atan((y2 - y1) / (x2 - x1)))

# main function
def main():
    givenVariables()