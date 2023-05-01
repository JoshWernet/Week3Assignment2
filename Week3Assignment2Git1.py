#Program Filename: Week3Assignment2
#Author: Joshua Wernet
#4/26/2023
#Compute the amount of power produced by a wind turbine
#Input: Average Wind Speed, Operating Efficiency, and the Blade Radius
#Output: Actual and Maximum Power Efficiency


#import the math package
import math

#Initialize the average wind speed, operating efficiency, and the radius of the blade
run = True
avgWindSpeed = 0
operatingEfficiency = 0.0
bladeRadius = 0

#Keep iterating through program till user decides they are done
while run == True:
    #assigning values to the intialized variables
    avgWindSpeed = float(input("What is the Average Wind Speed(m/s)?:"))
    bladeRadius = float(input("What is the radius of the blades(m)?:"))
    operatingEfficiency = float(input("What is the operating efficiency of the blades?(Input as number, computed as a percent!):"))

    #compute area with pi*bladeRadius^2
    area = math.pi*(bladeRadius**2)

    #Compute maximum power with 0.5*1.2*avgWindSpeed^3
    powerMaximum = (0.5)*(1.2)*(area)*(avgWindSpeed**3)

    #Compute actual power by taking percent of maximum power
    powerActual = powerMaximum * (operatingEfficiency/100)

    #Print the actual and maximum power of the wind turbine
    print("The actual turbine power is: ", powerActual)
    print("The Maximum power is: ", powerMaximum)

    #Input recalculation choice
    runChoice = input("Would you like to make another computation(y/n)?:")
    if runChoice == 'y':
        continue
    elif runChoice == 'n':
        run = False
    else:
        print("invalid")

        