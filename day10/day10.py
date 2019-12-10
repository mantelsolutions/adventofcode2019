import math

lines = [line.strip() for line in open('day10/input.txt')]

asteroidField = [[]]

asteroidsCoordinates = []

x = 0
y = 0


for line in lines:
    for char in line:
        #asteroidField[x][y] = char
        if "#" == char:
            asteroidsCoordinates.append((x,y))
        x += 1
    y +=1
print(asteroidsCoordinates)

listOfSights = []
for asteroid in asteroidsCoordinates:
    anglesSet = set() # use a set of angles, so that the angles are in there only once

    for potentialSight in asteroidsCoordinates:
        if asteroid != potentialSight:
            # add the angle to the set
            anglesSet.add(math.atan2(potentialSight[1] - asteroid[1], potentialSight[0]- asteroid[0]))
    listOfSights.append(len(anglesSet)) #number of angles = number of direct sights

part1 = max(listOfSights)

print("Result part1: " + str(part1))




