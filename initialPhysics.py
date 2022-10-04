# initialPhysics.py - Initial Starter Physics File
# By: Joshua Lim
# Date: 10/04/2022

# function to ask what section of physics to use
def physicsSection():
    print("What section of physics would you like to use?")
    print("1. Kinematics")
    print("2. Dynamics")
    print("3. Work, Energy, and Power")
    print("4. Momentum and Collisions")
    print("5. Rotational Motion")
    print("6. Gravitation")
    print("7. Fluids")
    print("8. Thermal Physics")
    print("9. Waves and Sound")
    print("10. Electromagnetism")
    print("11. Optics")
    print("12. Modern Physics")
    print("13. Quantum Physics")
    print("14. Relativity")
    print("15. Astrophysics")
    print("16. Cosmology")
    print("17. Particle Physics")
    print("18. Nuclear Physics")
    print("19. Atomic Physics")
    print("20. Solid State Physics")
    print("21. Condensed Matter Physics")
    print("22. Statistical Physics")
    print("23. Biophysics")
    print("24. Medical Physics")
    print("25. Environmental Physics")
    print("26. Geophysics")
    choice = input("Enter the number of the section you would like to use: ")
    if choice == "1":
        # python3 kinematics.py
        with open("kinematics.py", "r") as kinematics:
            code = kinematics.read()
            exec(code)
    elif choice == "2":
        exec("dynamics.py")
    elif choice == "3":
        exec("workEnergyPower.py")
    elif choice == "4":
        exec("momentumCollisions.py")
    elif choice == "5":
        exec("rotationalMotion.py")
    elif choice == "6":
        exec("gravitation.py")
    elif choice == "7":
        exec("fluids.py")
    elif choice == "8":
        exec("thermalPhysics.py")
    elif choice == "9":
        exec("wavesSound.py")
    elif choice == "10":
        exec("electromagnetism.py")
    elif choice == "11":
        exec("optics.py")
    elif choice == "12":
        exec("modernPhysics.py")
    elif choice == "13":
        exec("quantumPhysics.py")
    elif choice == "14":
        exec("relativity.py")
    elif choice == "15":
        exec("astrophysics.py")
    elif choice == "16":
        exec("cosmology.py")
    elif choice == "17":
        exec("particlePhysics.py")
    elif choice == "18":
        exec("nuclearPhysics.py")
    elif choice == "19":
        exec("atomicPhysics.py")
    elif choice == "20":
        exec("solidStatePhysics.py")
    elif choice == "21":
        exec("condensedMatterPhysics.py")
    elif choice == "22":
        exec("statisticalPhysics.py")
    elif choice == "23":
        exec("biophysics.py")
    elif choice == "24":
        exec("medicalPhysics.py")
    elif choice == "25":
        exec("environmentalPhysics.py")
    elif choice == "26":
        exec("geophysics.py")
    else:
        print("Invalid choice. Please try again.")
        physicsSection()

# runs this to start the program
physicsSection()