# solution for day4 of advent of code 2019

def containsAdjancentDigits(password):
    lastChar = ""
    for aChar in str(password):
        if not lastChar:
            lastChar = aChar
        elif lastChar == aChar:
            return True
        lastChar = aChar
    return False

def containsAtLeastOneDoubleDigits(password):
    numberOfDoubleDigits = 0
    numberOfAdjacentDigits = 0
    lastChar = ""
    for aChar in str(password):
        if not lastChar:
            lastChar = aChar
        elif lastChar == aChar:
            numberOfAdjacentDigits += 1
        else:
            lastChar = aChar
            if numberOfAdjacentDigits == 1:
                numberOfDoubleDigits += 1
            numberOfAdjacentDigits = 0
    result = numberOfDoubleDigits > 0 or numberOfAdjacentDigits == 1
    return result

def noDecreasingDigits(password):
    lastDigit = 0
    for aDigit in str(password):
        if lastDigit < int(aDigit):
            lastDigit = int(aDigit)
        elif lastDigit > int(aDigit):
            return False
    return True

def checkPasswordPart2(potentialPassword):
    if len(str(potentialPassword)) < 6 or len(str(potentialPassword)) > 6:
        return False
    elif not containsAtLeastOneDoubleDigits(potentialPassword):
        return False
    elif not noDecreasingDigits(potentialPassword):
        return False
    else:
        return True

numberOfPotentialPasswords = 0
for potentialPassword in range(272091, 815432):
    if len(str(potentialPassword)) < 6 or len(str(potentialPassword)) > 6:
        continue    
    elif not noDecreasingDigits(potentialPassword):
        continue
    elif not containsAdjancentDigits(potentialPassword):
        continue
    else:
        numberOfPotentialPasswords += 1

print("Result part1: " + str(numberOfPotentialPasswords))

numberOfPotentialPasswords = 0
for potentialPassword in range(272091, 815432):
    if checkPasswordPart2(potentialPassword):
        numberOfPotentialPasswords += 1

print("Result part2: " + str(numberOfPotentialPasswords))