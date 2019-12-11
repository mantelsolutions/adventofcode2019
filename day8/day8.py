lines = [line.rstrip('\n') for line in open('day8/input.txt')]

pixels = lines[0]

width = 25
height = 6
layers = list()

digitsPerLayer = width * height

class Layer:
    
    def __init__(self):
        super().__init__()
        self.digits = list()
        self.numberOfZeros = 0
        self.digitToAmountMap = {}

    def addDigit(self, digit):
        if digit == 0:
            self.numberOfZeros += 1
        self.digits.append(digit)
        timesOfDigit = self.digitToAmountMap.get(digit,0)
        timesOfDigit += 1
        self.digitToAmountMap[digit] = timesOfDigit
    
    def getAmountOfDigit(self, digit):
        return self.digitToAmountMap.get(digit, -1)

currentLayer = Layer()

for digit in pixels:
    if len(currentLayer.digits) < digitsPerLayer:
        currentLayer.addDigit(int(digit))
    else:
        layers.append(currentLayer)
        currentLayer = Layer()
        currentLayer.addDigit(int(digit))

layers.sort(key=lambda x: x.numberOfZeros)

resultPart1 = layers[0].getAmountOfDigit(1) * layers[0].getAmountOfDigit(2)

print("Result part1 {}".format(resultPart1))
