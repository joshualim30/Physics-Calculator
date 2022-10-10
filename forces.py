# forces.py - Forces Equations File
# By: Joshua Lim
# Date: 10/04/2022
# Version 0 Optimized

# imports
import math
import sys
import decimal
import formatting

# global variables
gravity = 9.81

# EQUATIONS:
# - net force
# F1 = i1, j1
# F2 = i2, j2
# F3 = i3, j3
# Fn = i sum, j sum
# - net force with theta
# Fn = i cos theta sum, j sin theta sum
# - normal force
# fn = mg
# - normal force components
# Fn = mg (cos or sin) theta
# - magnitude of force
# F = ma
# - magnitude of tension
# T = mg sin theta
# - static friction (to keep object at equilibrium)
# Fs = mu s N
# - kinetic friction (to keep object moving)
# Fk = mu k N
# - minimum force to start moving object
# F = mu s N
# - spring constant (at rest)
# k = F / x
# - spring extension/extended length    
# x = F / k
# - angle that object will slide down incline plane
# theta = tan inverse (h / l)
# - pulley spring constant
# k = F / x
# - pulley spring extension
# x = F / k
# - pulley rope tension
# T = F / x

formulas = []
def load_formulas():
    with open("formulas.yml", "r") as f:
        for line in f:
            formulas.append(
                line.strip().replace("'", "").replace("[", "").replace("]", "").replace("-", ""))
load_formulas() 

# function to ask what the user is trying to find
def findWhat(): 
    print("----------------------------------------")
    print("What are you trying to find?")
    print("0.1) Choose a different section (back)")
    print("0.2) List of all equations")
    print("---")
    print("1) Net Force")
    print("2) Net Force with Theta")
    print("3) Normal Force")
    print("4) Normal Force Components")
    print("5) Magnitude of Force")
    print("6) Magnitude of Tension")
    print("7) Static Friction (to keep object at equilibrium)")
    print("8) Kinetic Friction (to keep object moving)")
    print("9) Minimum Force to Start Moving Object")
    print("10) Spring Constant (at rest)")
    print("11) Spring Extension/Extended Length")
    print("12) Angle that Object Will Slide Down Incline Plane")
    print("13) Pulley Spring Constant")
    print("14) Pulley Spring Extension")
    print("15) Pulley Rope Tension")
    choice = float(input("Enter the number of the variable you are trying to find: "))
    if choice == 0.1:
        sys.exit()
    elif choice == 0.2:
        print("List of all equations:")
        for formula in formulas:
            print(formula)
        print("Press enter to continue")
        input()
        findWhat()
    elif choice >= 1 and choice <= 15:
        return choice
    else:
        print("Please enter a valid number.")
        findWhat()

# function to ask what variables are given
def givenVariables(finding):
    print("----------------------------------------")
    print("What variables are given? (enter '-' if it is not given)")
    if finding == 1: # net force
        print("How many forces are given?")
        numForces = int(input("Enter the number of forces given as an integer: "))
        if numForces > 1 and numForces != 0:
            i = 0
            iValues = []
            jValues = []
            while i < numForces:
                iValue = float(input("Enter i force #" + str(i + 1) + ": "))
                jValue = float(input("Enter j force #" + str(i + 1) + ": "))
                iValues.append(iValue)
                jValues.append(jValue)
                i += 1
            return [iValues, jValues]
        else:
            print("You must enter at least 2 forces.")
            givenVariables(finding)
    elif finding == 2: # net force with theta
        print("How many forces are given?")
        numForces = int(input("Enter the number of forces given as an integer: "))
        if numForces > 1 and numForces != 0:
            i = 0
            iValues = []
            jValues = []
            iThetas = []
            jThetas = []
            while i < numForces:
                iValue = float(input("Enter i force #" + str(i + 1) + ": "))
                jValue = float(input("Enter j force #" + str(i + 1) + ": "))
                iTheta = float(input("Enter i theta #" + str(i + 1) + ": "))
                jTheta = float(input("Enter j theta #" + str(i + 1) + ": "))
                iValues.append(iValue)
                jValues.append(jValue)
                iThetas.append(iTheta)
                jThetas.append(jTheta)
                i += 1
            return [iValues, jValues, iThetas, jThetas]
    elif finding == 3: # normal force
        mass = float(input("Enter mass: "))
        return mass
    elif finding == 4: # normal force with theta
        mass = float(input("Enter mass: "))
        theta = float(input("Enter theta: "))
        return [mass, theta]
    elif finding == 5: # magnitude of force
        mass = float(input("Enter mass: "))
        acceleration = float(input("Enter acceleration: "))
        return [mass, acceleration]
    elif finding == 6: # magnitude of tension
        mass = float(input("Enter mass: "))
        angle = float(input("Enter angle: "))
        return [mass, angle]
    elif finding == 7: # static friction
        muS = float(input("Enter coefficient of static friction: "))
        normalForce = float(input("Enter normal force: "))
        return [muS, normalForce]
    elif finding == 8: # kinetic friction
        muK = float(input("Enter coefficient of kinetic friction: "))
        normalForce = float(input("Enter normal force: "))
        return [muK, normalForce]
    elif finding == 9: # minimum force to start moving object
        force = float(input("Enter force: "))
        muS = float(input("Enter coefficient of static friction: "))
        normalForce = float(input("Enter normal force: "))
        return [force, muS, normalForce]
    elif finding == 10: # spring constant
        force = float(input("Enter force: "))
        extension = float(input("Enter extension: "))
        return [force, extension]
    elif finding == 11: # spring extension
        force = float(input("Enter force: "))
        springConstant = float(input("Enter spring constant: "))
        return [force, springConstant]
    elif finding == 12: # angle that object will slide down incline plane
        height = float(input("Enter height: "))
        length = float(input("Enter length: "))
        return [height, length]
    elif finding == 13: # pulley spring constant
        force = float(input("Enter force: "))
        extension = float(input("Enter extension: "))
        return [force, extension]
    elif finding == 14: # pulley spring extension
        force = float(input("Enter force: "))
        springConstant = float(input("Enter spring constant: "))
        return [force, springConstant]
    elif finding == 15: # pulley rope tension
        force = float(input("Enter force: "))
        extension = float(input("Enter extension: "))
        return [force, extension]
    else:
        print("Please enter a valid number.")
        givenVariables(finding)

# function to calculate the net force
def netForce(iValues, jValues, iTheta, jTheta, trig):
    if trig == 0: # no theta
        i = 0
        j = 0
        print("- Finding net force by adding all i values together")
        for iValue in iValues:
            i += iValue
        print("- Finding net force by adding all j values together")
        for jValue in jValues:
            j += jValue
        return [i, j]
    elif trig == 1: # theta
        i = 0
        iFinal = 0
        jFinal = 0
        print("- Finding net force by adding all i values together after multiplying by cos(theta), then adding all j values together after multiplying by sin(theta)")
        while i < len(iValues):
            iFinal += float(iValues[i] * math.cos(math.degrees(iTheta[i])))
            jFinal += float(jValues[i] * math.sin(math.degrees(jTheta[i])))
            i += 1
        return [iFinal, jFinal]

# function to find magnitude of net force
def magnitudeOfForceComponents(i, j):
    print("- Finding square root of " + str(i) + "^2 + " + str(j) + "^2")
    return math.sqrt(i ** 2 + j ** 2)

# function to calculate the normal force
def normalForce(mass, angle, trig):
    if trig == 0: # no theta
        print("- Finding normal force by multiplying " + str(mass) + " * gravity (9.81)")
        return mass * gravity
    elif trig == 1: # theta
        print("- Finding normal force components by multiplying " + str(mass) + " * gravity (9.81) * cos(" + str(angle) + ") for the i component and " + str(mass) + " * gravity (9.81) * sin(" + str(angle) + ") for the j component")
        xComponent = mass * gravity * math.cos(math.degrees(angle))
        yComponent = mass * gravity * math.sin(math.degrees(angle))
        return [xComponent, yComponent]

# function to calculate the magnitude of force
def magnitudeOfForce(mass, acceleration):
    print("- Finding magnitude of force by multiplying " + str(mass) + " * " + str(acceleration))
    return mass * acceleration
    
# function to calculate the magnitude of tension
def magnitudeOfTension(mass, angle):
    print("- Finding magnitude of tension by multiplying " + str(mass) + " * gravity (9.81) * " + str(math.sin(math.degrees(angle))))
    return mass * gravity * math.sin(angle)

# function to calculate the static friction
def staticFriction(muS, normalForce):
    print("- Finding static friction by multiplying " + str(muS) + " * " + str(normalForce))
    return muS * normalForce

# function to calculate the kinetic friction
def kineticFriction(muK, normalForce):
    print("- Finding kinetic friction by multiplying " + str(muK) + " * " + str(normalForce))
    return muK * normalForce

# function to calculate the minimum force to start moving object
def minimumForce(muS, normalForce):
    print("- Finding minimum force to start moving object by multiplying " + str(muS) + " * " + str(normalForce))
    return muS * normalForce

# function to calculate the spring constant
def springConstant(force, extension):
    print("- Finding spring constant by dividing " + str(force) + " by " + str(extension))
    return force / extension

# function to calculate the spring extension
def springExtension(force, springConstant):
    print("- Finding spring extension by dividing " + str(force) + " by " + str(springConstant))
    return force / springConstant

# function to calculate the angle that object will slide down incline plane
def angleInclinePlane(mass, angle, coefficientOfFriction):
    print("- Finding angle that object will slide down incline plane by dividing " + str(mass) + " * gravity (9.81) * " + str(math.sin(math.degrees(angle))) + " by " + str(coefficientOfFriction) + " * " + str(mass) + " * gravity (9.81) * " + str(math.cos(math.degrees(angle))))
    return math.asin((mass * gravity * math.sin(angle)) / (mass * gravity * coefficientOfFriction))
    
# function to calculate the pulley spring constant
def pulleySpringConstant(force, extension):
    print("- Finding pulley spring constant by dividing " + str(force) + " by " + str(extension))
    return force / extension

# function to calculate the pulley spring extension
def pulleySpringExtension(force, springConstant):
    print("- Finding pulley spring extension by dividing " + str(force) + " by " + str(springConstant))
    return force / springConstant

# function to calculate the pulley rope tension
def pulleyRopeTension(force, extension):
    print("- Finding pulley rope tension by dividing " + str(force) + " by " + str(extension))
    return force / extension
    
# run the code
finding = findWhat()
given = givenVariables(finding)
if finding == 1: # net force
    netForce = netForce(given[0], given[1], 0, 0, 0)
    print("The net force is " + str(formatting.formatDecimal(netForce[0], ".0000")) + " i + " + str(formatting.formatDecimal(netForce[1], ".0000")) + " j")
elif finding == 2: # net force with theta
    netForce = netForce(given[0], given[1], given[2], given[3], 1)
    print("The net force is " + str(formatting.formatDecimal(netForce[0], ".0000")) + " i + " + str(formatting.formatDecimal(netForce[1], ".0000")) + " j")
elif finding == 3: # normal force
    normalForce = normalForce(given[0], 0, 0)
    print("The normal force is " + str(formatting.formatDecimal(normalForce, ".0000")) + " N")
elif finding == 4: # normal force components
    normalForce = normalForce(given[0], given[1], 1)
    print("The normal force components are " + str(formatting.formatDecimal(normalForce[0], ".0000")) + " i + " + str(formatting.formatDecimal(normalForce[1], ".0000")) + " j")
elif finding == 5: # magnitude of force
    magnitudeOfForce = magnitudeOfForce(given[0], given[1])
    print("The magnitude of force is " + str(formatting.formatDecimal(magnitudeOfForce, ".0000")) + " N")
elif finding == 6: # magnitude of tension
    magnitudeOfTension = magnitudeOfTension(given[0], given[1])
    print("The magnitude of tension is " + str(formatting.formatDecimal(magnitudeOfTension, ".0000")) + " N")
elif finding == 7: # static friction
    staticFriction = staticFriction(given[0], given[1])
    print("The static friction is " + str(formatting.formatDecimal(staticFriction, ".0000")) + " muS")
elif finding == 8: # kinetic friction
    kineticFriction = kineticFriction(given[0], given[1])
    print("The kinetic friction is " + str(formatting.formatDecimal(kineticFriction, ".0000")) + " muK")
elif finding == 9: # minimum force to start moving object
    minimumForce = minimumForce(given[0], given[1])
    print("The minimum force to start moving object is " + str(formatting.formatDecimal(minimumForce, ".0000")) + " N")
elif finding == 10: # spring constant
    springConstant = springConstant(given[0], given[1])
    print("The spring constant is " + str(formatting.formatDecimal(springConstant, ".0000")) + " N/m")
elif finding == 11: # spring extension
    springExtension = springExtension(given[0], given[1])
    print("The spring extension is " + str(formatting.formatDecimal(springExtension, ".0000")) + " m")
elif finding == 12: # angle that object will slide down incline plane
    angleInclinePlane = angleInclinePlane(given[0], given[1], given[2])
    print("The angle that object will slide down incline plane is " + str(formatting.formatDecimal(angleInclinePlane, ".0000")) + " degrees")
elif finding == 13: # pulley spring constant
    pulleySpringConstant = pulleySpringConstant(given[0], given[1])
    print("The pulley spring constant is " + str(formatting.formatDecimal(pulleySpringConstant, ".0000")) + " N/m")
elif finding == 14: # pulley spring extension
    pulleySpringExtension = pulleySpringExtension(given[0], given[1])
    print("The pulley spring extension is " + str(formatting.formatDecimal(pulleySpringExtension, ".0000")) + " m")
elif finding == 15: # pulley rope tension
    pulleyRopeTension = pulleyRopeTension(given[0], given[1])
    print("The pulley rope tension is " + str(formatting.formatDecimal(pulleyRopeTension, ".0000")) + " N")
# end of code