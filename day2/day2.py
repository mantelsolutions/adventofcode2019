# Solution for day2 of advent of code

origValues = list(map(int, open('day2/input.txt').readline().rstrip().split(',')))

print(origValues)

def getOpCode(values, codeAndArgumentWidth, numberOfCodesEvaluated):
    currentOpCodeIndex = getCurrentOpCodeIndex(values, codeAndArgumentWidth, numberOfCodesEvaluated)
    return int(values[currentOpCodeIndex])

def addOperation(values, opCodeIndex):
    operant1 = int(values[values[opCodeIndex+1]])
    operant2 = int(values[values[opCodeIndex+2]])
    values[values[opCodeIndex+3]] = operant1 + operant2

def multiplyOperation(values, opCodeIndex):
    operant1 = int(values[valuesPart1[opCodeIndex+1]])
    operant2 = int(values[valuesPart1[opCodeIndex+2]])
    values[values[opCodeIndex+3]] = operant1 * operant2

def getCurrentOpCodeIndex(values, codeAndArgumentWidth, numberOfCodesEvaluated):
    """Computes the current opCode index"""
    return codeAndArgumentWidth * numberOfCodesEvaluated


def getResult(values):
    """Calculates the result for the memory operations"""

    numberOfCodesEvaluated = 0
    codeAndArgumentWidth = 4
    haltCodeFound = False
    while  not haltCodeFound:
        opCode = getOpCode(values, codeAndArgumentWidth, numberOfCodesEvaluated)
        #print("Current opCode: " + str(opCode))

        if(opCode == 1):
            #print("add operation")
            addOperation(values, getCurrentOpCodeIndex(values, codeAndArgumentWidth, numberOfCodesEvaluated))
        elif(opCode == 2):
            #print("multiply operation")
            multiplyOperation(values, getCurrentOpCodeIndex(values, codeAndArgumentWidth,numberOfCodesEvaluated))
        elif(opCode == 99):
            #print("HALT found")
            haltCodeFound = True
        else:
            print("ERROR unknown opcode found: " + str(opCode) + " for opCodeIndex: " + str(getCurrentOpCodeIndex(values, codeAndArgumentWidth, numberOfCodesEvaluated)))
            return -1

        numberOfCodesEvaluated += 1
    return values[0]

valuesPart1 = origValues.copy()

valuesPart1[1] = 12
valuesPart1[2] = 2

resultPart1 = getResult(valuesPart1)
print("Result of part1: " + str(valuesPart1[0]))
assert 5098658 == resultPart1

# part2

# Initialize
valuesPart2 = origValues.copy()

noun = 0
verb = 0
desiredOutput = 19690720

desiredOutputFound = False
while not desiredOutputFound:
    # print("Noun: " + str(noun) + " -- Verb: " + str(verb))
    valuesPart2[1] = noun
    valuesPart2[2] = verb

    currentResult = getResult(valuesPart2)
    if(currentResult < 0):
        print("Found unknown opcode ==> FAIL")
        break

    if currentResult == desiredOutput:
        desiredOutputFound = True
    else:
        # keep guessing the verb & noun
        if verb >= 99:
            noun += 1
            verb = 0
        else:
            verb += 1  
        
        # reset the "memory"
        valuesPart2 = origValues.copy()

print("Result part2: " + str(100 * valuesPart2[1] + valuesPart2[2]))