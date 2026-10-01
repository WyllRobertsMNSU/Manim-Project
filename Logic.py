from manim import Text
from manim import VGroup
from typing import List
from enum import Enum
from copy import deepcopy


class Logic:
    def convertTo16Bits(elevenBits:List[Text]):
        elevenBits.insert(0, Text(str(0)))  # P0
        elevenBits.insert(1, Text(str(0)))  # P1
        elevenBits.insert(2, Text(str(0)))  # P2
        elevenBits.insert(4, Text(str(0)))  # P4
        elevenBits.insert(8, Text(str(0)))  # P8

        return elevenBits

    def calculateParityBits(bits:List[Text]):
        endArray = deepcopy(bits)

        #Calculates P1
        if(Checks.Q1_1Check(bits) is False):
            endArray[1] = Text(str(1))

        #Calculates P2
        if(Checks.Q2_1Check(bits) is False):
            endArray[2] = Text(str(1))

        #Calculates P3
        if(Checks.Q3_1Check(bits) is False):
            endArray[4] = Text(str(1))


        #Calculates P4
        if(Checks.Q4_1Check(bits) is False):
            endArray[8] = Text(str(1))

        # Overall parity bit
        parity = 0

        for x in range(1, 16):
            parity += int(endArray[x].text)

        endArray[0] = Text(str(parity % 2))

        return endArray

    def detectError(bits:List[Text]):
        #Used to for the animate to know what check found an error 
        #False means check 1, true means check 2
        checkResults = [False, False, False, False]
        Q1PotentialPositions = []
        Q2PotentialPositions = []
        Q3PotentialPositions = []
        Q4PotentialPositions = []
        if(not Checks.Q1_1Check(bits)):
            Q1PotentialPositions = [1, 3, 5, 7, 9, 11, 13, 15]
        elif(not Checks.Q1_1Check(bits)):
            Q1PotentialPositions = [0, 2, 4, 6, 8, 10, 12, 14]
            checkResults[0] = True

        if(not Checks.Q2_1Check(bits)):
            Q2PotentialPositions = [2, 3, 6, 7, 10, 11, 14, 15]
        elif(not Checks.Q2_2Check(bits)):
            Q2PotentialPositions = [0, 1, 4, 5, 8, 9, 12, 13]
            checkResults[1] = True

        if(not Checks.Q3_1Check(bits)):
            Q3PotentialPositions = [4, 5, 6, 7, 12, 13, 14, 15]
        elif(not Checks.Q3_2Check(bits)):
            Q3PotentialPositions = [0, 1, 2, 3, 8, 9, 10, 11]
            checkResults[2] = True

        if(not Checks.Q4_1Check(bits)):
            Q4PotentialPositions = [8, 9, 10, 11, 12, 13, 14, 15]
        elif(not Checks.Q4_2Check(bits)):
            Q4PotentialPositions = [0, 1, 2, 3, 4, 5, 6, 7]
            checkResults[3] = True

        errorLocation = set(Q1PotentialPositions).intersection(Q2PotentialPositions, Q3PotentialPositions, Q4PotentialPositions)
        return (errorLocation, checkResults)

        

    
class Checks:
    #region Column Checks

    def Q1_1Check(bits):
        parity = 0

        # Checks columns 1 and 3
        for x in [1, 3, 5, 7, 9, 11, 13, 15]:
            parity += int(bits[x].text)

        if(parity % 2 == 0):
            return False
        else:
            return True

    def Q1_2Check(bits):
        parity = 0

        # Checks columns 0 and 2
        for x in [0, 2, 4, 6, 8, 10, 12, 14]:
            parity += int(bits[x].text)

        if(parity % 2 == 0):
            return False
        else:
            return True

    def Q2_1Check(bits):
        parity = 0

        # Checks columns 2 and 3
        for x in [2, 3, 6, 7, 10, 11, 14, 15]:
            parity += int(bits[x].text)

        if(parity % 2 == 0):
            return False
        else:
            return True

    def Q2_2Check(bits):
        parity = 0

        # Checks columns 0 and 1
        for x in [0, 1, 4, 5, 8, 9, 12, 13]:
            parity += int(bits[x].text)

        if(parity % 2 == 0):
            return False
        else:
            return True

    #endregion


    #region Row Checks

    def Q3_1Check(bits):
        parity = 0

        # Checks rows 1 and 3
        for x in [4, 5, 6, 7, 12, 13, 14, 15]:
            parity += int(bits[x].text)

        if(parity % 2 == 0):
            return False
        else:
            return True

    def Q3_2Check(bits):
        parity = 0

        # Checks rows 0 and 2
        for x in [0, 1, 2, 3, 8, 9, 10, 11]:
            parity += int(bits[x].text)

        if(parity % 2 == 0):
            return False
        else:
            return True

    def Q4_1Check(bits):
        parity = 0

        # Checks rows 2 and 3
        for x in [8, 9, 10, 11, 12, 13, 14, 15]:
            parity += int(bits[x].text)

        if(parity % 2 == 0):
            return False
        else:
            return True

    def Q4_2Check(bits):
        parity = 0

        # Checks rows 0 and 1
        for x in [0, 1, 2, 3, 4, 5, 6, 7]:
            parity += int(bits[x].text)

        if(parity % 2 == 0):
            return False
        else:
            return True

    #endregion


if __name__ == "__main__":
    bits = [
        Text(str(1)),
        Text(str(0)),
        Text(str(1)),
        Text(str(1)),
        Text(str(1)),
        Text(str(1)),
        Text(str(1)),
        Text(str(0)),
        Text(str(0)),
        Text(str(1)),
        Text(str(0))
    ]

    Logic.convertTo16Bits(bits)
    bits = Logic.calculateParityBits(bits)
    bits[5].text = 1
    print(Logic.detectError(bits))
