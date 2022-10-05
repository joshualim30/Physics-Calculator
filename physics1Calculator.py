# physics1Calculator.py - Initial Starter Physics File (For PHY2048 @ UCF)
# By: Joshua Lim
# Date: 10/04/2022
# Version 0 Optimized

# run '$python3 physics1Calculator.py' to start the program

# Importing Modules
import subprocess
import sys

# function to ask what section of physics to use
def physicsSection():
    print("----------------------------------------")
    print("----------------------------------------")
    print("What section of physics would you like to use?")
    print("1. Vector Algebra") # v0
    print("2. Motion in 1D") # v0
    print("3. Projectile Motion (2D)") # v0
    print("4. Forces") # v0
    print("5. Newton's Laws of Motion") # v0
    print("6. Circular Motion") # v0
    print("7. Work and Kinetic Energy") # v0
    print("8. Conservation of Mechanical Energy") # v0
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
        subprocess.run(['python3', 'vectorAlgebra.py'])
    elif choice == "2":
        # python3 motion1D.py
        subprocess.run(['python3', 'motion1D.py'])
    elif choice == "3":
        # python3 projectileMotion.py
        subprocess.run(['python3', 'projectileMotion.py'])
    elif choice == "4":
        # python3 forces.py
        subprocess.run(['python3', 'forces.py'])
    elif choice == "5":
        # python3 newtonsLaws.py
        subprocess.run(['python3', 'newtonsLaws.py'])
    elif choice == "6":
        # python3 circularMotion.py
        subprocess.run(['python3', 'circularMotion.py'])
    elif choice == "7":
        # python3 workAndKineticEnergy.py
        subprocess.run(['python3', 'workAndKineticEnergy.py'])
    elif choice == "8":
        # python3 conservationOfMechanicalEnergy.py
        subprocess.run(['python3', 'conservationOfMechanicalEnergy.py'])
    elif choice == "9":
        # python3 linearMomentumAndConservationOfMomentum.py
        # subprocess.run(['python3', 'linearMomentumAndConservationOfMomentum.py'])
        print("Linear Momentum and Conservation of Momentum is not yet implemented.")
    elif choice == "10":
        # python3 collisionsAndManyParticleSystems.py
        # subprocess.run(['python3', 'collisionsAndManyParticleSystems.py'])
        print("Collisions and Many Particle Systems is not yet implemented.")
    elif choice == "11":
        # python3 torquesAndStaticEquilibrium.py
        # subprocess.run(['python3', 'torquesAndStaticEquilibrium.py'])
        print("Torques and Static Equilibrium is not yet implemented.")
    elif choice == "12":
        # python3 rotationalMotion.py
        # subprocess.run(['python3', 'rotationalMotion.py'])
        print("Rotational Motion is not yet available.")
    elif choice == "13":
        # python3 angularMomentum.py
        # subprocess.run(['python3', 'angularMomentum.py'])
        print("Angular Momentum is not yet implemented.")
    elif choice == "14":
        # python3 simpleHarmonicMotion.py
        # subprocess.run(['python3', 'simpleHarmonicMotion.py'])
        print("Simple Harmonic Motion is not yet implemented.")
    elif choice == "15":
        # python3 wavesAndOscillation.py
        # subprocess.run(['python3', 'wavesAndOscillation.py'])
        print("Waves and Oscillation is not yet implemented.")
    else:
        print("Please enter a valid number.")
        physicsSection()
    again = input("Would you like to use another section of physics? (y/n): ")
    if again == "y":
        physicsSection()
    elif again == "n":
        print("Thank you for using Physics Calculator!")
        print("----------------------------------------")
        sys.exit()
    else:
        print("Invalid input, terminating program.")
        print("----------------------------------------")
        sys.exit()

# runs the code
physicsSection()