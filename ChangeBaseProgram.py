# Filename: ChangeBaseProgram.py
# Author: Mike Shea
# Date: 8/15/20
#
# Description: A program that prompts the user to enter a value to convert
# as well as the current number base and the desired number base.

class ChangeBase:
    
    def __init__(self):
        self.debug = True
        self.value = 0
        self.initialBase = 0
        self.newBase = 0
        self.solution = 0
        self.charList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'
                    'U', 'V', 'W', 'X', 'Y', 'Z']
        
    def userInput(self):
        self.value = self.inputValue()
        self.initialBase = self.inputInitialBase()
        self.newBase = self.inputNewBase()
    
    def inputValue(self):
        value = input("Enter the value to convert: ")
        while(int(value) <= 0):
            print("Invalid input. Please enter a positive value.")
            value = input("Enter the value to convert: ")
        return value

    def inputInitialBase(self):
        initialBase =  input("Enter the current number base: ")
        while(int(initialBase) <= 0):
            print("Invalid input. Please enter a positive value.")
            initialBase =  input("Enter the current number base: ")
        return initialBase


    def inputNewBase(self):
        newBase =  input("Enter the new number base: ")
        while(int(newBase) <= 0):
            print("Invalid input. Please enter a positive value.")
            newBase =  input("Enter the new number base: ")
        return newBase

    def convertToBase10(self):
        
        if(self.initialBase != 10):
            valueLength = len(self.value)
            counter = valueLength - 1
            valueString = str(self.value)
            totalSum = int(0)

            for i in range(valueLength):
                currentValue = int(valueString[i])
                currentProduct = currentValue * (int(self.initialBase) ** counter)

                if(self.debug == True):
                    print(str(currentProduct) + " = " + str(currentValue) + " * " + str(self.initialBase) + " ^ " + str(counter))
                
                totalSum += currentProduct
                counter -= 1

        if(self.debug == True):  
            print("totalSum = " + str(totalSum))
            print()
            
        return totalSum


    def calculateNewValue(self):
        value = self.value
        initialBase = self.initialBase

        valueString = str(value)
        valueLength = len(value)
        newValue = int(0)
        totalSum = int(0)
        totalSum = self.convertToBase10()

        if (int(self.newBase) == 10):
            self.solution = totalSum
        else:
            self.solution = self.convertToNewBase(totalSum)

    
        
    def convertToNewBase(self, totalSum):
        
        # Convert to new base
        solutionList = []
        remainder = float(0)
        quotient = float(totalSum)
        finishedDividing = False

        while(finishedDividing == False):

            
            remainder = quotient % int(self.newBase)

            if(self.debug == True):
                print("quotient = " + str(quotient))
                print("remainder = " + str(remainder))
                print()
                
            quotient = quotient // int(self.newBase)
            solutionList.append(int(remainder))

            if(quotient == 0):
                finishedDividing = True

        # New value is the remainders in reverse order
        solutionList.reverse()
        tempSolution = ""
        for i in solutionList:
            tempSolution += str(i)

        solution = ""

        print("solution: ")
        for i in range(len(tempSolution)):
            if(i < len(tempSolution) - 1):

                thisValue = ""
               
                numberPair = str(tempSolution[i]) + str(tempSolution[i+1])

                if(numberPair >= self.newBase):
                   firstChar = tempSolution[i]
                   secondChar = tempSolution[i+1]
                   newChar = ''

                   # index to check
                   thisValue = str(firstChar) + str(secondChar)
                   thisValue = int(thisValue)

                if thisValue <= 36:
                    newChar = self.convertToChar(index)

                    if(self.debug):
                        print(str(firstChar) + str(secondChar) + " converted to " + str(newChar))

                    solution += str(newChar)
                else:
                    solution += str(tempSolution[i])                    

        self.solution = solution

    def convertToChar(self, index):
        
        return self.charList[index]


    def getIndex(self, char):

        for x in range(self.charList):
            if x == char:
                return x

    def output(self):
        print()
        print("=======================")
        print("Entered value: " + str(self.value))
        print("Initial base: " + str(self.initialBase))
        print("New Value: " + str(self.solution))
        print("New base: " + str(self.newBase))
        print("=======================")

# Main #
changeBase = ChangeBase()
changeBase.userInput()
changeBase.calculateNewValue()
changeBase.output()
