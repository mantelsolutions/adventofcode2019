
class Moon:

    def __init__(self,position, velocity, name):
        super().__init__()
        self.position = position
        self.velocity = velocity
        self.name = name

    def getPotentialEnergy(self):
        result = 0
        for aPosition in self.position:
            result += abs(aPosition)
        return result

    def getKineticEnergy(self):
        result = 0
        for aVelocity in self.velocity:
            result += abs(aVelocity)
        return result
    
    def __repr__(self):
        return "{} - Position: {} - Velocity: {}\n".format(self.name, self.position, self.velocity)



def updateGravity(moonA, moonB):
    #print("Before update: A: {} - B: {}".format(moonA,moonB))
    for dimension in range (0,3):
        moonA_position = moonA.position[dimension]
        moonB_position = moonB.position[dimension]
        if moonA_position < moonB_position:
            moonA.velocity[dimension] += 1
            moonB.velocity[dimension] -= 1
        elif moonA_position > moonB_position:
            moonA.velocity[dimension] -= 1
            moonB.velocity[dimension] += 1
    #print("After update: A: {} - B: {}".format(moonA,moonB))

def updatePosition(moon):
    for dimension in range(0,3):
        moon.position[dimension] += moon.velocity[dimension]

def totalSystemEnergy(moons):
    result = 0
    for moon in moons:
        result += moon.getPotentialEnergy() * moon.getKineticEnergy()
    return result

lines = [line.rstrip('>\n').lstrip('<') for line in open('day12/input.txt')]

moons = list()
counter = 0
for line in lines:
    parts = line.split(',')
    coordinates = list()
    for part in parts:
        part = part.strip() #remove whitespaces
        coordinates.append(int(part[2:len(part)]))
    moon = Moon(coordinates, list((0,0,0)), "Moon{}".format(counter))
    moons.append(moon)
    counter += 1

def updateSystem(moons):
    updatedTuples = {}
    for moon in moons:
        for otherMoon in moons:
            if otherMoon != moon:
                if not (moon.name, otherMoon.name) in updatedTuples and not (otherMoon.name,moon.name) in updatedTuples:
                    updateGravity(moon, otherMoon)
                    updatedTuples[(moon.name,otherMoon.name)] = True
        updatePosition(moon)

steps = 1000

system = moons.copy()
for step in range(0, steps):
    updateSystem(system)


resultPart1 = totalSystemEnergy(system)

print("Result part1: {}".format(resultPart1))

def dimensionState(moons,dimension):
    """returns the state for the given dimension"""
    result = list()
    for moon in moons:
        result.append((moon.position[dimension],moon.velocity[dimension]))
    return result

initialXState = dimensionState(moons,0)
print(initialXState)

system = moons.copy()

def findInitialStateForDimension(system, initialSystem, dimension):
    """Find the number of steps necessary to reach the same initial state"""
    initialState = dimensionState(initialSystem,dimension)

    stateFound = False
    counter = 0
    while not stateFound:
        updateSystem(system)
        state = list()
        for moon in system:
            state.append((moon.position[dimension], moon.velocity[dimension]))
        if state == initialState:
            stateFound = True
        counter += 1
    return counter

xSteps = findInitialStateForDimension(moons.copy(), moons, 0)
print("Steps for X-Axis: {}".format(xSteps))
ySteps = findInitialStateForDimension(moons.copy(), moons, 1)
print("Steps for Y-Axis: {}".format(ySteps))
zSteps = findInitialStateForDimension(moons.copy(), moons, 2)
print("Steps for Z-Axis: {}".format(zSteps))

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

resultPart2 = lcm(xSteps, lcm(ySteps,zSteps))

print("Result part2: {}".format(resultPart2))
