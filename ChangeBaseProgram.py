# Filename: ChangeBaseProgram.py
# Author: Mike Shea
# Date: 8/14/20
#
# Description: A program that prompts the user to enter a value to convert
# as well as the current number base and the desired number base.

# User Inputs #
valueString = input("Enter the value to convert: ")
initialBase = input("Enter the current base of the number: ")
newBase = input("Enter the base you would like to convert to: ")

# Validate Inputs
while(int(valueString) <= 0 or int(initialBase) <= 0 or int(newBase) <= 0):
    print("Invalid input. Please enter positive values for the value and bases.")
    valueString = input("Enter the value to convert: ")
    initialBase = input("Enter the current base of the number: ")
    newBase = input("Enter the base you would like to convert to: ")
    
# Initialize Variables #
value = int(valueString)
valueLength = len(valueString)
newValue = int(0)
totalSum = int(0)

# Convert to base 10 #
if(initialBase != 10):

    counter = valueLength - 1
    
    for i in range(valueLength):
        currentValue = int(valueString[i])
        currentProduct = currentValue * (int(initialBase) ** counter)
        totalSum += currentProduct
        --counter
        
# Convert to new base
solutionList = []
remainder = float(0)
quotient = float(totalSum)
finishedDividing = False

while(finishedDividing == False):
    remainder = quotient % int(newBase)
    quotient = quotient // int(newBase)
    solutionList.append(int(remainder))

    if(quotient == 0):
        finishedDividing = True

# New value is the quotients in reverse order
solutionList.reverse()
solution = ""
for i in solutionList:
    solution += str(i)

# Output
print("=======================")
print("Entered value: " + str(value))
print("Initial base: " + initialBase)
print("New Value: " + solution)
print("New base: " + str(newBase))
print("=======================")
