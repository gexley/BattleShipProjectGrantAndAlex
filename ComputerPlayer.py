import random
from Player import Player

class ComputerPlayer(Player):

    def __init__(self):
        Player.__init__(self)

    def takeTurn(self):



    def placeShip(self, ship , size):
        badship = True
        while badship: #runs until the ship generated is valid
            badship = False
            orientation = random.randint(0,1)
            # orientation 0 is horizontal, orientation 1 is vertical
            if orientation == 0:#if the ship is horizontal
                startRow = random.randint(0,10-size)
                startCol = random.randint(0,9)
                for i in range(size):#runs size amount of times
                    if not self.gridShips.isSpaceWater(startRow + i, startCol):#if the placement is not legal
                        badship = True
            elif orientation == 1:#if the ship is vertical
                startRow = random.randint(0,9)
                startCol = random.randint(0,10-size)
                for i in range(size):#runs size amount of times
                    if not self.gridShips(startRow,startCol + i): #if the placement is not legal
                        badship = True
        if orientation == 0:#if the ship is horizontal
            for i in range(size):#runs size amount of times
                self.gridShips.changeSingleSpace(startRow + i, startCol, ship)
        if orientation == 1:#if the ship is vertical
            for i in range(size):#runs size amount of times
                self.gridShips.changeSingleSpace(startRow, startCol + i, ship)


