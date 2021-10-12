import random
from Player import Player

class ComputerPlayer(Player):

    def __init__(self):
        Player.__init__(self)

    def placeShip(self, ship , size):
        badship = True
        while badship:
            badship = False
            orientation = random.randint(0,1)
            # orientation 0 is horizontal, orientation 1 is vertical
            if orientation == 0:
                startRow = random.randint(0,10-size)
                startCol = random.randint(0,9)
                for i in range(size):
                    if not self.gridShips.returnLocation(startRow + i,startCol) == '~':
                        badship = True
            elif orientation == 1:
                startRow = random.randint(0,9)
                startCol = random.randint(0,10-size)
                for i in range(size):
                    if not self.gridShips.returnLocation(startRow,startCol + i) == '~':
                        badship = True
        if orientation == 0:
            for i in range(size):
                self.gridShips.changeSingleSpace(startRow + i, startCol, ship)
        if orientation == 1:
            for i in range(size):
                self.gridShips.changeSingleSpace(startRow, startCol + i, ship)
