# tests.py - Test Physics Equations File
# By: Joshua Lim
# Date: 10/05/2022
# Test File, NOT FOR USE IN PROGRAM

# run '$python3 tests.py' to start the program

# imports
import unittest
import math
import vectorAlgebra as va # vectorAlgebra.py
import motion1D as m1d # motion1D.py
import projectileMotion as pm # projectileMotion.py
import forces as f # forces.py
import newtonsLaws as nl # newtonsLaws.py
import circularMotion as cm # circularMotion.py
import workAndKineticEnergy as wke # workAndKineticEnergy.py
import conservationOfMechanicalEnergy as cme # conservationOfMechanicalEnergy.py

# test vectorAlgebra.py - 6 tests
class TestVectorAlgebra(unittest.TestCase):
    # test x1
    def test_x1(self):
        self.assertEqual(va.x1(3, 4, 5, 12), 9)
    # test y1
    def test_y1(self):
        self.assertEqual(va.y1(3, 4, 5, 12), 8)
    # test x2
    def test_x2(self):
        self.assertEqual(va.x2(3, 4, 5, 12), 13)
    # test y2
    def test_y2(self):
        self.assertEqual(va.y2(3, 4, 5, 12), 16)
    # test magnitude
    def test_magnitude(self):
        self.assertEqual(va.magnitude(3, 4), 5)
    # test angle
    def test_angle(self):
        self.assertEqual(va.angle(3, 4), 53.13010235415598)

# test motion1D.py - 4 tests
class TestMotion1D(unittest.TestCase):
    # test displacement
    def test_displacement(self):
        self.assertEqual(m1d.displacement(3, 4, 5), 7)
    # test velocity
    def test_velocity(self):
        self.assertEqual(m1d.velocity(3, 4, 5), 1.4)
    # test time
    def test_time(self):
        self.assertEqual(m1d.time(3, 4, 5), 3.5)
    # test acceleration
    def test_acceleration(self):
        self.assertEqual(m1d.acceleration(3, 4, 5), 0.6)

# test projectileMotion.py - 4 tests
class TestProjectileMotion(unittest.TestCase):
    # test horizontalRange
    def test_horizontalRange(self):
        self.assertEqual(pm.horizontalRange(3, 4), 12)
    # test maximumHeight
    def test_maximumHeight(self):
        self.assertEqual(pm.maximumHeight(3, 4), 6)
    # test timeOfFlight
    def test_timeOfFlight(self):
        self.assertEqual(pm.timeOfFlight(3, 4), 4)
    # test verticalRange
    def test_verticalRange(self):
        self.assertEqual(pm.verticalRange(3, 4), 24)

# test forces.py - 4 tests
class TestForces(unittest.TestCase):
    # test force
    def test_force(self):
        self.assertEqual(f.force(3, 4), 12)
    # test mass
    def test_mass(self):
        self.assertEqual(f.mass(3, 4), 0.25)
    # test acceleration
    def test_acceleration(self):
        self.assertEqual(f.acceleration(3, 4), 0.75)
    # test weight
    def test_weight(self):
        self.assertEqual(f.weight(3), 27.9)

# test newtonsLaws.py - 4 tests
class TestNewtonsLaws(unittest.TestCase):
    # test newtonsFirstLaw
    def test_newtonsFirstLaw(self):
        self.assertEqual(nl.newtonsFirstLaw(3, 4), 0.75)
    # test newtonsSecondLaw
    def test_newtonsSecondLaw(self):
        self.assertEqual(nl.newtonsSecondLaw(3, 4), 12)
    # test newtonsThirdLaw
    def test_newtonsThirdLaw(self):
        self.assertEqual(nl.newtonsThirdLaw(3, 4), 12)
    # test newtonsThirdLaw2
    def test_newtonsThirdLaw2(self):
        self.assertEqual(nl.newtonsThirdLaw2(3, 4), 12)

# test circularMotion.py - 4 tests
class TestCircularMotion(unittest.TestCase):
    # test centripetalForce
    def test_centripetalForce(self):
        self.assertEqual(cm.centripetalForce(3, 4), 12)
    # test centripetalAcceleration
    def test_centripetalAcceleration(self):
        self.assertEqual(cm.centripetalAcceleration(3, 4), 4)
    # test centripetalVelocity
    def test_centripetalVelocity(self):
        self.assertEqual(cm.centripetalVelocity(3, 4), 12)
    # test centripetalVelocity2
    def test_centripetalVelocity2(self):
        self.assertEqual(cm.centripetalVelocity2(3, 4), 12)

# test workAndKineticEnergy.py - 4 tests
class TestWorkAndKineticEnergy(unittest.TestCase):
    # test work
    def test_work(self):
        self.assertEqual(wke.work(3, 4, 5), 60)
    # test kineticEnergy
    def test_kineticEnergy(self):
        self.assertEqual(wke.kineticEnergy(3, 4), 12)
    # test work2
    def test_work2(self):
        self.assertEqual(wke.work2(3, 4, 5), 60)
    # test kineticEnergy2
    def test_kineticEnergy2(self):
        self.assertEqual(wke.kineticEnergy2(3, 4), 12)

# test conservationOfMechanicalEnergy.py - 4 tests
class TestConservationOfMechanicalEnergy(unittest.TestCase):
    # test potentialEnergy
    def test_potentialEnergy(self):
        self.assertEqual(cme.potentialEnergy(3, 4), 12)
    # test kineticEnergy
    def test_kineticEnergy(self):
        self.assertEqual(cme.kineticEnergy(3, 4), 12)
    # test potentialEnergy2
    def test_potentialEnergy2(self):
        self.assertEqual(cme.potentialEnergy2(3, 4), 12)
    # test kineticEnergy2
    def test_kineticEnergy2(self):
        self.assertEqual(cme.kineticEnergy2(3, 4), 12)

# ask what tests to run
print("Which tests would you like to run?")
print("1. All")
print("2. Vector Algebra")
print("3. Motion 1D")
print("4. Projectile Motion")
print("5. Forces")
print("6. Newton's Laws")
print("7. Circular Motion")
print("8. Work and Kinetic Energy")
print("9. Conservation of Mechanical Energy")
choice = int(input("Enter your choice: "))
# run tests
if choice == 1:
    unittest.main()
elif choice == 2:
    unittest.main(module='testVectorAlgebra', exit=False)
elif choice == 3:
    unittest.main(module='testMotion1D', exit=False)
elif choice == 4:
    unittest.main(module='testProjectileMotion', exit=False)
elif choice == 5:
    unittest.main(module='testForces', exit=False)
elif choice == 6:
    unittest.main(module='testNewtonsLaws', exit=False)
elif choice == 7:
    unittest.main(module='testCircularMotion', exit=False)
elif choice == 8:
    unittest.main(module='testWorkAndKineticEnergy', exit=False)
elif choice == 9:
    unittest.main(module='testConservationOfMechanicalEnergy', exit=False)
else:
    print("Invalid choice")