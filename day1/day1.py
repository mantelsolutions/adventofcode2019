# Solution for day1 of advent of code 2019

import math

lines = [line.rstrip('\n') for line in open('day1/input.txt')]

# part1
fuel = 0
for line in lines:
    fuelForModule = math.floor(int(line) / 3) - 2
    fuel += fuelForModule

print("Fuel needed: " + str(fuel))

# part2
def calculateFuelForMass(mass):
    """calculate the fuel for a given mass"""
    return math.floor(int(mass) / 3) - 2

def recursiveCalc(mass):
    """Recursive calculation of fuel required"""    
    if(mass > 0):
       return mass + recursiveCalc(calculateFuelForMass(mass))
    else:
        return 0

fuel = 0
for line in lines:
    fuel += recursiveCalc(calculateFuelForMass(int(line)))

print("Part2 - fuel needed: " + str(fuel))

