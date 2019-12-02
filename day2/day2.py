# Solution for day2 of advent of code

origValues = list(map(int, open('day2/input.txt').readline().rstrip().split(',')))

print(origValues)

valuesPart1 = origValues.copy()

valuesPart1[1] = 12
valuesPart1[2] = 2

opCodeIndex = 0
numberOfCodesEvaluated = 0
codeAndArgumentWidth = 4

def getOpCode(codeAndArgumentWidth, numberOfCodesEvaluated):
    currentOpCodeIndex = getCurrentOpCodeIndex(codeAndArgumentWidth, numberOfCodesEvaluated)
    return int(valuesPart1[currentOpCodeIndex])

def addOperation(opCodeIndex):
    operant1 = int(valuesPart1[valuesPart1[opCodeIndex+1]])
    operant2 = int(valuesPart1[valuesPart1[opCodeIndex+2]])
    valuesPart1[valuesPart1[opCodeIndex+3]] = operant1 + operant2

def multiplyOperation(opCodeIndex):
    operant1 = int(valuesPart1[valuesPart1[opCodeIndex+1]])
    operant2 = int(valuesPart1[valuesPart1[opCodeIndex+2]])
    valuesPart1[valuesPart1[opCodeIndex+3]] = operant1 * operant2

def getCurrentOpCodeIndex(codeAndArgumentWidth, numberOfCodesEvaluated):
    return codeAndArgumentWidth * numberOfCodesEvaluated

haltCodeFound = False
while  not haltCodeFound:
    opCode = getOpCode(codeAndArgumentWidth, numberOfCodesEvaluated)
    print("Current opCode: " + str(opCode))

    if(opCode == 1):
        print("add operation")
        addOperation(getCurrentOpCodeIndex(codeAndArgumentWidth, numberOfCodesEvaluated))
    elif(opCode == 2):
        print("multiply operation")
        multiplyOperation(getCurrentOpCodeIndex(codeAndArgumentWidth,numberOfCodesEvaluated))
    elif(opCode == 99):
        print("HALT found")
        haltCodeFound = True
    else:
        print("ERROR unknown opcode found: " + str(opCode))
        break

    numberOfCodesEvaluated += 1

print("Result of part1: " + str(valuesPart1[0]))