# solution for day3 of advent of code 2019
import numpy as np

lines = [line.rstrip('\n') for line in open('day3/input.txt')]
print(lines)
stepsFirstWire = lines[0].split(',')
stepsSecondWire = lines[1].split(',')

print(stepsFirstWire)




maxUp = 0
maxDown = 0
maxLeft = 0
maxRight = 0
for step in stepsFirstWire:
    if step[0] == 'U':
        print("Up step found: " + step)
        maxUp += int(step.strip('U'))
    elif step[0] == 'D':
        print("Down step found: " + str(step[0]))
        maxDown += int(step.strip('D'))
    elif step[0] == 'L':
        print("Left step found: " + str(step[0]))
        maxLeft += int(step.strip('L'))
    elif step[0] == 'R':
        print("Left step found: " + str(step[0]))
        maxRight += int(step.strip('R'))
    else:
        print("ERROR unknown step type: " + str(step[0]))
        break

print("Max up: " + str(maxUp))
print("Max down: " + str(maxDown))
print("Max left: " + str(maxLeft))
print("Max right: " + str(maxRight))

startingPoint = 9

field = np.zeros((maxLeft+maxRight+1, maxUp+maxDown+1), dtype=int)


startX = 0
if maxLeft > maxRight:
    startX = maxLeft +1
else:
    startX = maxRight +1


startY = (maxUp+maxDown+1)//2
if maxUp > maxDown:
    startY = maxUp +1
else:
    startY = maxDown +1

field[startX][startY] = startingPoint

currentX = 0
currentY = 0

crossCoordinates = [[]]

coordinatesFirst = []
numberOfSteps = 0
coordsToStepsMapFirst = {}

for step in stepsFirstWire:
    if step[0] == 'U':
        print("Up step found: " + step)
        steps = int(step.strip('U'))
        for step in range(0, steps):
            currentY -= 1
            coordinatesFirst.append(tuple((currentX,currentY)))
            numberOfSteps += 1
            coordsToStepsMapFirst[tuple((currentX,currentY))] = numberOfSteps
    elif step[0] == 'D':
        print("Down step found: " + str(step[0]))
        steps = int(step.strip('D'))
        for step in range(0, steps):
            currentY += 1
            coordinatesFirst.append(tuple((currentX,currentY)))
            numberOfSteps += 1
            coordsToStepsMapFirst[tuple((currentX,currentY))] = numberOfSteps
    elif step[0] == 'L':
        print("Left step found: " + str(step[0]))
        steps = int(step.strip('L'))
        for step in range(0, steps):
            currentX -= 1
            coordinatesFirst.append(tuple((currentX,currentY)))
            numberOfSteps += 1
            coordsToStepsMapFirst[tuple((currentX,currentY))] = numberOfSteps
    elif step[0] == 'R':
        print("Left step found: " + str(step[0]))
        steps = int(step.strip('R'))
        for step in range(0, steps):
            currentX += 1
            coordinatesFirst.append(tuple((currentX,currentY)))
            numberOfSteps += 1
            coordsToStepsMapFirst[tuple((currentX,currentY))] = numberOfSteps
    else:
        print("ERROR unknown step type: " + str(step[0]))

currentX = 0
currentY = 0

coordinatesSecond = []

numberOfSteps = 0
coordsToStepsMapSecond = {}

for step in stepsSecondWire:
    if step[0] == 'U':
        print("Up step found: " + step)
        steps = int(step.strip('U'))
        for step in range(0, steps):
            currentY -= 1
            coordinatesSecond.append(tuple((currentX, currentY)))
            numberOfSteps += 1
            coordsToStepsMapSecond[tuple((currentX,currentY))] = numberOfSteps
    elif step[0] == 'D':
        print("Down step found: " + str(step[0]))
        steps = int(step.strip('D'))
        for step in range(0, steps):
            currentY += 1
            coordinatesSecond.append(tuple((currentX,currentY)))
            numberOfSteps += 1
            coordsToStepsMapSecond[tuple((currentX,currentY))] = numberOfSteps
    elif step[0] == 'L':
        print("Left step found: " + str(step[0]))
        steps = int(step.strip('L'))
        for step in range(0, steps):
            currentX -= 1
            coordinatesSecond.append(tuple((currentX,currentY)))
            numberOfSteps += 1
            coordsToStepsMapSecond[tuple((currentX,currentY))] = numberOfSteps
    elif step[0] == 'R':
        print("Left step found: " + str(step[0]))
        steps = int(step.strip('R'))
        for step in range(0, steps):
            currentX += 1
            coordinatesSecond.append(tuple((currentX, currentY)))
            numberOfSteps += 1
            coordsToStepsMapSecond[tuple((currentX,currentY))] = numberOfSteps
    else:
        print("ERROR unknown step type: " + str(step[0]))

print(len(coordinatesFirst))

matchingCoordinates = [x for x in coordinatesFirst if x in coordsToStepsMapSecond]

print(matchingCoordinates)

distances = []
for coordinate in matchingCoordinates:
    distance = abs(coordinate[0]) + abs(coordinate[1])
    distances.append(distance)

resultPart1 = min(distances)
print("Result part1: " + str(resultPart1))

listOfStepsToIntersections = []
for coordinate in matchingCoordinates:
    stepsFirst = coordsToStepsMapFirst.get(coordinate)
    stepsSecond = coordsToStepsMapSecond.get(coordinate)
    listOfStepsToIntersections.append(stepsFirst+stepsSecond)

resultPart2 = min(listOfStepsToIntersections)
print("Result part2: " + str(resultPart2))
