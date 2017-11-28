import time
import random
class planeZ:
    def __init__(self, positionRow, positionCol):
        self.currentPos_Row = positionRow
        self.currentPos_Col = positionCol
#Moves Row+=3 | Col+=(Col+1) % 7

    flag = False

    def move(self, positionMatrix):
        if self.flag is False: 
        #    lastPos_Col = (self.currentPos_Col-1) % 7
            lastPos_Row = 0  # (self.currentPos_Row - 1) % 8
            lastPos_Col = 0  # (self.currentPos_Col - 1) % 7
            self.changeDir(lastPos_Row, lastPos_Col)
            self.subCheck(positionMatrix, self.currentPos_Row, lastPos_Col, self.currentPos_Row, self.currentPos_Col)

        #if self.flag is False:
            self.currentPos_Col = (self.currentPos_Col + 1) % 7
            self.addCheck(positionMatrix)
            self.subCheck(positionMatrix, self.currentPos_Row, lastPos_Col, self.currentPos_Row, self.currentPos_Col)
     
    def getRow(self):
        return self.currentPos_Row

    def getCol(self):
        return self.currentPos_Col

    def addCheck(self, positionMatrix):
        if positionMatrix[self.currentPos_Row][self.currentPos_Col] == 0:
            positionMatrix[self.currentPos_Row][self.currentPos_Col] =  'Z'
            return
        elif positionMatrix[self.currentPos_Row][self.currentPos_Col] == 'X':
            positionMatrix[self.currentPos_Row][self.currentPos_Col] = 'XZ'
            return
        elif positionMatrix[self.currentPos_Row][self.currentPos_Col] == 'Y':
            positionMatrix[self.currentPos_Row][self.currentPos_Col] = 'YZ'
            return
        elif positionMatrix[self.currentPos_Row][self.currentPos_Col] == 'XY':
            positionMatrix[self.currentPos_Row][self.currentPos_Col] = 'XYZ'
            return

    def subCheck(self, positionMatrix, lastPos_Row, lastPos_Col,currentPos_Row, currentPos_Col):
        count = 0
        
        for i in range (0,7):
          
        
            for j in range (0,6):

                if (i != currentPos_Row or j != currentPos_Col) and positionMatrix[i][j] == 'Z':
                    positionMatrix[i][j] = 0

        
                
        if positionMatrix[lastPos_Row][lastPos_Col] == 'Z':
            positionMatrix[lastPos_Row][lastPos_Col] = 0
            return
        elif positionMatrix[lastPos_Row][lastPos_Col] == 'XZ':
            positionMatrix[lastPos_Row][lastPos_Col] = 'X'
            return
        elif positionMatrix[lastPos_Row][lastPos_Col] == 'YZ':
            positionMatrix[lastPos_Row][lastPos_Col] = 'Y'
            return
        elif positionMatrix[lastPos_Row][lastPos_Col] == 'XYZ':
            positionMatrix[lastPos_Row][lastPos_Col] = 'XY'
            return

    def changeDir(self,lastPos_Row,lastPos_Col):
        #0=up,1=down,2=left,3=right
        dir=random.randint(0,7)
        if dir==0:
            lastPos_Col = (self.currentPos_Col - 1) % 7
            self.currentPos_Col = (self.currentPos_Col + 1) % 7
        elif dir==1:
            lastPos_Col = (self.currentPos_Col + 1) % 7
            self.currentPos_Col = (self.currentPos_Col - 1) % 7
        elif dir==2:
            lastPos_Row = (self.currentPos_Row - 1) % 8
            self.currentPos_Row = (self.currentPos_Row + 1) % 8
        elif dir==3:
            lastPos_Row = (self.currentPos_Row + 1) % 8
            self.currentPos_Row = (self.currentPos_Row - 1) % 8
        if dir==4:
            lastPos_Col = (self.currentPos_Col - 2) % 7
            self.currentPos_Col = (self.currentPos_Col + 2) % 7
        elif dir==5:
            lastPos_Col = (self.currentPos_Col + 2) % 7
            self.currentPos_Col = (self.currentPos_Col - 2) % 7
        elif dir==6:
            lastPos_Row = (self.currentPos_Row - 2) % 8
            self.currentPos_Row = (self.currentPos_Row + 2) % 8
        elif dir==7:
            lastPos_Row = (self.currentPos_Row + 2) % 8
            self.currentPos_Row = (self.currentPos_Row - 2) % 8


    def stop(self):
        if random.randint(0,99) >= 0:
            self.flag = True
        else:
            print "Failed to stop Z"

    def start(self):
        self.flag = False
    def getflag(self):
        return self.flag
