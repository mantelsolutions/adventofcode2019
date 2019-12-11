import math
import numpy as np
from math import acos
from math import sqrt
from math import pi

lines = [line.strip() for line in open('day10/input.txt')]

x=0
y=0
asteroidsCoordinates = []
for line in lines:
    for char in line:
        if "#" == char:
            asteroidsCoordinates.append((x,y))
        x += 1
    y +=1
    x = 0


def angleTwoPoints(pointA, pointB):
    return math.atan2(pointB[1] - pointA[1], pointB[0]- pointA[0]) * 180 / math.pi % 360


listOfSights = []
sightsToAsteroidMap = {}
for asteroid in asteroidsCoordinates:
    anglesSet = set() # use a set of angles, so that the angles are in there only once

    for potentialSight in asteroidsCoordinates:
        if asteroid != potentialSight:
            # add the angle to the set
            anglesSet.add(angleTwoPoints(asteroid, potentialSight))
    listOfSights.append(len(anglesSet)) #number of angles = number of direct sights
    sightsToAsteroidMap[len(anglesSet)] = asteroid

part1 = max(listOfSights)

print("Result part1: " + str(part1))

def distance(pointA, pointB):
    distance = math.sqrt((pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2)
    return distance

androidStation = sightsToAsteroidMap[part1]

print("AsteroidStation: {}".format(androidStation))

class Asteroid:

    def __init__(self, coordinates, angle, distance):
        super().__init__()
        self.coordinates = coordinates
        self.angle = angle
        self.distance = distance
    
    def __repr__(self):
        return "coords: {} -- angle: {} -- distance: {}".format(self.coordinates, self.angle, self.distance)

    def __str__(self):
        return "coords: {} -- angle: {} -- distance: {}".format(self.coordinates, self.angle, self.distance)

mapOfAsteroidsToCrush = {}

for aAsteroid in asteroidsCoordinates:
    if aAsteroid != androidStation:
        prepareAsteroid = Asteroid(aAsteroid, (angleTwoPoints(androidStation, aAsteroid)- 270.0)%360, distance(androidStation, aAsteroid))
        listOfAsteroidsForAngle = mapOfAsteroidsToCrush.get(prepareAsteroid.angle, list())
        listOfAsteroidsForAngle.append(prepareAsteroid)
        listOfAsteroidsForAngle.sort(key=lambda x: x.distance)
        mapOfAsteroidsToCrush[prepareAsteroid.angle] = listOfAsteroidsForAngle

angles = list(mapOfAsteroidsToCrush.keys())
angles.sort(reverse=False)

numberOfLaserShots = 1
requestedLaserShots = 200

while numberOfLaserShots < requestedLaserShots:
    for angle in angles:
        listOfAsteroids = mapOfAsteroidsToCrush[angle]
        numberOfAsteroids = len(listOfAsteroids)

        if numberOfAsteroids > 0:
            currentAsteroid = listOfAsteroids[0]

            listOfAsteroids.remove(currentAsteroid)
            mapOfAsteroidsToCrush[angle] = listOfAsteroids

            numberOfLaserShots += 1

            if numberOfLaserShots >= 201:
                print("200th asteroid: {}".format(currentAsteroid))
                resultPart2 = currentAsteroid.coordinates[0] * 100 + currentAsteroid.coordinates[1]
                print("Result part2: " + str(resultPart2))
                break




