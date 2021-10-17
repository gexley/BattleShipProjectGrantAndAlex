import random
from Player import Player


class ComputerPlayer(Player):

    def __init__(self):
        Player.__init__(self)
        self.hitsA = 0
        self.hitsB = 0
        self.hitsC = 0
        self.hitsS = 0
        self.hitsD = 0

    def takeTurn(self, otherPlayer):
        while True:
            fireRow = random.randint(0, 9)
            fireCol = random.randint(0, 9)
            if self.gridShots.isSpaceWater(fireRow, fireCol):
                break

        if otherPlayer.gridShips.returnLocation(fireRow, fireCol) == 'A':
            print("The CPU hit your ship!")
            self.gridShots.changeSingleSpace(fireRow, fireCol, 'X')
            self.hitsA += 1
            if self.hitsA == 5:
                print("The CPU sunk your Aircraft Carrier!")
        elif otherPlayer.gridShips.returnLocation(fireRow, fireCol) == 'B':
            print("The CPU hit your ship!")
            self.gridShots.changeSingleSpace(fireRow, fireCol, 'X')
            self.hitsB += 1
            if self.hitsB == 4:
                print("The CPU sunk your Battleship!")
        elif otherPlayer.gridShips.returnLocation(fireRow, fireCol) == 'C':
            print("The CPU hit your ship!")
            self.gridShots.changeSingleSpace(fireRow, fireCol, 'X')
            self.hitsC += 1
            if self.hitsC == 3:
                print("The CPU sunk your Cruiser!")
        elif otherPlayer.gridShips.returnLocation(fireRow, fireCol) == 'S':
            print("The CPU hit your ship!")
            self.gridShots.changeSingleSpace(fireRow, fireCol, 'X')
            self.hitsS += 1
            if self.hitsS == 3:
                print("The CPU sunk your Submarine!")
        elif otherPlayer.gridShips.returnLocation(fireRow, fireCol) == 'D':
            print("The CPU hit your ship!")
            self.gridShots.changeSingleSpace(fireRow, fireCol, 'X')
            self.hitsD += 1
            if self.hitsD == 2:
                print("The CPU sunk your Destroyer!")
        else:
            print("The CPU missed.")

        if self.hitsA == 5 and self.hitsB == 4 and self.hitsC == 3 and self.hitsS == 3 and self.hitsD == 2:
            return False
        else:
            return True

    def placeShip(self, ship , size):
        badship = True
        orientation = random.randint(0, 1)
        startCol = random.randint(0, 10 - size)
        startRow = random.randint(0, 9)

        while badship: # runs until the ship generated is valid
            badship = False
            orientation = random.randint(0, 1)

            # orientation 0 is horizontal, orientation 1 is vertical
            if orientation == 0: # if the ship is horizontal
                startCol = random.randint(0, 10-size)
                startRow = random.randint(0, 9)
                for i in range(size): # runs size amount of times
                    if not self.gridShips.isSpaceWater(startCol + i, startRow): # if the placement is not legal
                        badship = True
            elif orientation == 1: # if the ship is vertical
                startCol = random.randint(0, 9)
                startRow = random.randint(0, 10-size)
                for i in range(size): # runs size amount of times
                    if not self.gridShips(startCol, startRow + i): # if the placement is not legal
                        badship = True

        if orientation == 0: # if the ship is horizontal
            self.gridShips.changeRow(startRow, ship, startCol, size)
        if orientation == 1: # if the ship is vertical
            self.gridShips.changeCol(startCol, ship, startRow, size)


