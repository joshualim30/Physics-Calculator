# vectorAlgebra.py - Vector Algebra Equations File
# By: Joshua Lim
# Date: 10/04/2022
# Version 0 Optimized

# imports
import math

# function to ask what the user is trying to find
def findWhat():
    print("What are you trying to find?")
    print("1. x1")
    print("2. y1")
    print("3. x2")
    print("4. y2")
    print("5. Magnitude")
    print("6. Angle")
    choice = int(input("Enter the number of the variable you are trying to find: "))
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
        findWhat()

# function to ask what variables are given
def givenVariables(finding):
    print("What variables are given? (enter '-' if it is not given)")
    if finding != "x1":
        x1 = int(input("Enter the x1 value: "))
    else:
        x1 = "-"
    if finding != "y1":
        y1 = int(input("Enter the y1 value: "))
    else:
        y1 = "-"
    if finding != "x2":
        x2 = int(input("Enter the x2 value: "))
    else:
        x2 = "-"
    if finding != "y2":
        y2 = int(input("Enter the y2 value: "))
    else:
        y2 = "-"
    if finding != "magnitude":
        magnitude = int(input("Enter the magnitude: "))
    else:
        magnitude = "-"
    if finding != "angle":
        angle = int(input("Enter the angle: "))
    else:
        angle = "-"
    return [x1, y1, x2, y2, magnitude, angle]

# function to solve for x1 given x2, magnitude & angle
def x1(x2, magnitude, angle):
    return x2 - magnitude * math.cos(math.radians(angle))

# function to solve for y1 given y2, magnitude & angle
def y1(y2, magnitude, angle):
    return y2 - magnitude * math.sin(math.radians(angle))

# function to solve for x2 given x1, magnitude & angle
def x2(x1, magnitude, angle):
    return x1 + magnitude * math.cos(math.radians(angle))

# function to solve for y2 given y1, magnitude & angle
def y2(y1, magnitude, angle):
    print(y1 + magnitude * math.sin(math.radians(angle)))
    return y1 + magnitude * math.sin(math.radians(angle))

# function to solve for magnitude x1, y1, x2 & y2
def magnitude(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# function to solve for angle given x1, y1, x2 & y2
def angle(x1, y1, x2, y2):
    return math.degrees(math.atan((y2 - y1) / (x2 - x1)))

# run code here
# given list structure: [x1, y1, x2, y2, magnitude, angle]
#                         0   1   2   3      4        5
solvingFor = findWhat()
given = givenVariables(solvingFor)
if solvingFor == "x1": # needs x2, magnitude, angle to solve (2, 4, 5)
    if given[2] == "-":
        print("Sorry, Python Calculator cannot solve for x1 without x2. Please try again.")
    elif given[4] == "-":
        print("Sorry, Python Calculator cannot solve for x1 without magnitude. Please try again.")
    elif given[5] == "-":
        print("Sorry, Python Calculator cannot solve for x1 without angle. Please try again.")
    else:
        solution = x1(float(given[2]), float(given[4]), float(given[5]))
        print("The x1 value is " + str(solution) + " by using the equation x1 = x2 - magnitude * cos(angle).")
elif solvingFor == "y1": # needs y2, magnitude, angle to solve (3, 4, 5)
    if given[3] == "-":
        print("Sorry, Python Calculator cannot solve for y1 without y2. Please try again.")
    elif given[4] == "-":
        print("Sorry, Python Calculator cannot solve for y1 without magnitude. Please try again.")
    elif given[5] == "-":
        print("Sorry, Python Calculator cannot solve for y1 without angle. Please try again.")
    else:
        solution = y1(float(given[3]), float(given[4]), float(given[5]))
        print("The y1 value is " + str(solution) + " by using the equation y1 = y2 - magnitude * sin(angle).")
elif solvingFor == "x2": # needs x1, magnitude, angle to solve (0, 4, 5)
    if given[0] == "-":
        print("Sorry, Python Calculator cannot solve for x2 without x1. Please try again.")
    elif given[4] == "-":
        print("Sorry, Python Calculator cannot solve for x2 without magnitude. Please try again.")
    elif given[5] == "-":
        print("Sorry, Python Calculator cannot solve for x2 without angle. Please try again.")
    else:
        solution = x2(float(given[0]), float(given[4]), float(given[5]))
        print("The x2 value is " + str(solution) + " by using the equation x2 = x1 + magnitude * cos(angle).")
elif solvingFor == "y2": # needs y1, magnitude, angle to solve (1, 4, 5)
    if given[1] == "-":
        print("Sorry, Python Calculator cannot solve for y2 without y1. Please try again.")
    elif given[4] == "-":
        print("Sorry, Python Calculator cannot solve for y2 without magnitude. Please try again.")
    elif given[5] == "-":
        print("Sorry, Python Calculator cannot solve for y2 without angle. Please try again.")
    else:
        solution = y2(float(given[1]), float(given[4]), float(given[5]))
        print("The y2 value is " + str(solution) + " by using the equation y2 = y1 + magnitude * sin(angle).")
elif solvingFor == "magnitude": # needs x1, y1, x2 & y2 to solve (0, 1, 2, 3)
    if given[0] == "-":
        print("Sorry, Python Calculator cannot solve for magnitude without x1. Please try again.")
    elif given[1] == "-":
        print("Sorry, Python Calculator cannot solve for magnitude without y1. Please try again.")
    elif given[2] == "-":
        print("Sorry, Python Calculator cannot solve for magnitude without x2. Please try again.")
    elif given[3] == "-":
        print("Sorry, Python Calculator cannot solve for magnitude without y2. Please try again.")
    else:
        solution = magnitude(float(given[0]), float(given[1]), float(given[2]), float(given[3]))
        print("The magnitude value is " + str(solution) + " by using the equation magnitude = sqrt((x2 - x1)^2 + (y2 - y1)^2).")
elif solvingFor == "angle": # needs x1, y1, x2 & y2 to solve (0, 1, 2, 3)
    if given[0] == "-":
        print("Sorry, Python Calculator cannot solve for angle without x1. Please try again.")
    elif given[1] == "-":
        print("Sorry, Python Calculator cannot solve for angle without y1. Please try again.")
    elif given[2] == "-":
        print("Sorry, Python Calculator cannot solve for angle without x2. Please try again.")
    elif given[3] == "-":
        print("Sorry, Python Calculator cannot solve for angle without y2. Please try again.")
    else:
        solution = angle(float(given[0]), float(given[1]), float(given[2]), float(given[3]))
        print("The angle value is " + str(solution) + " by using the equation angle = degrees(atan((y2 - y1) / (x2 - x1))).")
else:
    print("Sorry, Python Calculator cannot solve for " + solvingFor + ". Please try again.") # if solvingFor is not a valid option
# end of code
