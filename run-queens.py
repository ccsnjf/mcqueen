import random
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
import time

# Target initialisation
x = 15
while x >= 0:
    kit.servo[x].set_pulse_width_range(900, 2100)
    print("Initialising target " + str(x))
    x = x - 1
RUN = "Y"

y = 15
while y >= 0:
    kit.servo[y].angle = 90
    print("Target " + str(y) + " away...")
    y = y - 1

# Main loop
while RUN != "N":
    Program = input("Which program  (1:Mcqueen, 2:control or 3:three)?")
    while Program != "1" and Program != "2" and Program != "3":
        Program = input("Which program  (1:Mcqueen, 2:control or 3:three)?")
    if Program == "1":

        y = 15
        while y >= 0:
            kit.servo[y].angle = 0
            print("Facing for Exposure " + str(y))
            y = y - 1

        time.sleep(5)
        y = 15
        while y >= 0:
            kit.servo[y].angle = 0
            print("Facing for Exposure " + str(y))
            y = y - 1

        # Main timed routine
        print("\n\nReady... 10 Exposures... \n\n")
        Y = 1
        while Y <= 10:
            # sleep a random time between 10 and 20 secs
            # if randint arguments are not (10,20) we are testing
            delay = random.randint(5, 6)
            print("Away time of " + str(delay) + "secs")
            time.sleep(delay)

            # Pick a target at random
            # For a 16 pin IO board we should have randint(0,15)
            PinNumber = random.randint(1, 2)

            print(PinNumber)

            kit.servo[PinNumber].angle = 0
            print("Face.... Exposure " + str(Y))
            time.sleep(3)

            kit.servo[PinNumber].angle = 90
            print("Edge....")

            print(PinNumber)

            print("Cycle " + str(Y) + "\n\n")
            Y = Y + 1

        y = 15
        while y >= 0:
            kit.servo[y].angle = 0
            print("Facing for Exposure " + str(y))
            y = y - 1

        print("End")

    if Program == "2":
        v = input("servo number")
        x = input("Servo angle")
        t = v
        o = x
        v = int(v)
        x = int(x)
        kit.servo[v].angle = x
        print("Servo " + t + " moved to angle " + o)

    if Program == "3":
        y = 15
        while y >= 0:
            kit.servo[y].angle = 0
            print("Face....")
            y = y - 1

        time.sleep(3)

        y = 15
        while y >= 0:
            kit.servo[y].angle = 90
            print("Edge....")
            y = y - 1

        print("End")
