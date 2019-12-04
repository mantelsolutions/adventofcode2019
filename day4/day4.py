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

def noDecreasingDigits(password):
    lastDigit = 0
    for aDigit in str(password):
        if lastDigit < int(aDigit):
            lastDigit = int(aDigit)
        elif lastDigit > int(aDigit):
            return False
    return True

numberOfPotentialPasswords = 0
for potentialPassword in range(272091, 815432):
    if len(str(potentialPassword)) < 6 or len(str(potentialPassword)) > 6:
        continue
    elif not containsAdjancentDigits(potentialPassword):
        continue
    elif not noDecreasingDigits(potentialPassword):
        continue
    else:
        numberOfPotentialPasswords += 1

print("Result part1: " + str(numberOfPotentialPasswords))