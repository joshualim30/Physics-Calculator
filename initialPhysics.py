# initialPhysics.py - Initial Starter Physics File (For PHY2048 @ UCF)
# By: Joshua Lim
# Date: 10/04/2022

# function to ask what section of physics to use
def physicsSection():
    print("What section of physics would you like to use?")
    print("1. Vector Algebra")
    print("2. Motion in 1D")
    print("3. Projectile Motion (2D)")
    print("4. Forces")
    print("5. Newton's Laws of Motion")
    print("6. Circular Motion")
    print("7. Work and Kinetic Energy")
    print("8. Conservation of Mechanical Energy")
    print("9. Linear Momentum and Conservation of Momentum")
    print("10. Collisions and Many Particle Systems")
    print("11. Torques and Static Equilibrium")
    print("12. Rotational Motion")
    print("13. Angular Momentum")
    print("14. Simple Harmonic Motion")
    print("15. Waves and Oscillation")
    choice = input("Enter the number of the section you would like to use: ")
    if choice == "1":
        # python3 vectorAlgebra.py
        with open("vectorAlgebra.py", "r") as vectorAlgebra:
            code = vectorAlgebra.read()
            exec(code)
    elif choice == "2":
        # python3 motion1D.py
        with open("motion1D.py", "r") as motion1D:
            code = motion1D.read()
            exec(code)
    elif choice == "3":
        # python3 projectileMotion.py
        with open("projectileMotion.py", "r") as projectileMotion:
            code = projectileMotion.read()
            exec(code)
    elif choice == "4":
        # python3 forces.py
        with open("forces.py", "r") as forces:
            code = forces.read()
            exec(code)
    elif choice == "5":
        # python3 newtonsLaws.py
        with open("newtonsLaws.py", "r") as newtonsLaws:
            code = newtonsLaws.read()
            exec(code)
    elif choice == "6":
        # python3 circularMotion.py
        with open("circularMotion.py", "r") as circularMotion:
            code = circularMotion.read()
            exec(code)
    elif choice == "7":
        # python3 workAndKineticEnergy.py
        with open("workAndKineticEnergy.py", "r") as workAndKineticEnergy:
            code = workAndKineticEnergy.read()
            exec(code)
    elif choice == "8":
        # python3 conservationOfMechanicalEnergy.py
        with open("conservationOfMechanicalEnergy.py", "r") as conservationOfMechanicalEnergy:
            code = conservationOfMechanicalEnergy.read()
            exec(code)
    elif choice == "9":
        # python3 linearMomentumAndConservationOfMomentum.py
        with open("linearMomentumAndConservationOfMomentum.py", "r") as linearMomentumAndConservationOfMomentum:
            code = linearMomentumAndConservationOfMomentum.read()
            exec(code)
    elif choice == "10":
        # python3 collisionsAndManyParticleSystems.py
        with open("collisionsAndManyParticleSystems.py", "r") as collisionsAndManyParticleSystems:
            code = collisionsAndManyParticleSystems.read()
            exec(code)
    elif choice == "11":
        # python3 torquesAndStaticEquilibrium.py
        with open("torquesAndStaticEquilibrium.py", "r") as torquesAndStaticEquilibrium:
            code = torquesAndStaticEquilibrium.read()
            exec(code)
    elif choice == "12":
        # python3 rotationalMotion.py
        with open("rotationalMotion.py", "r") as rotationalMotion:
            code = rotationalMotion.read()
            exec(code)
    elif choice == "13":
        # python3 angularMomentum.py
        with open("angularMomentum.py", "r") as angularMomentum:
            code = angularMomentum.read()
            exec(code)
    elif choice == "14":
        # python3 simpleHarmonicMotion.py
        with open("simpleHarmonicMotion.py", "r") as simpleHarmonicMotion:
            code = simpleHarmonicMotion.read()
            exec(code)
    elif choice == "15":
        # python3 wavesAndOscillation.py
        with open("wavesAndOscillation.py", "r") as wavesAndOscillation:
            code = wavesAndOscillation.read()
            exec(code)
    else:
        print("Please enter a valid number.")
        physicsSection()
        

# runs this to start the program
def main():
    physicsSection()