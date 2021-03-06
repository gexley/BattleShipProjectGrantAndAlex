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

        while True:#runs until break
            fireRow = random.randint(0, 9)
            fireCol = random.randint(0, 9)
            if self.gridShots.isSpaceWater(fireRow, fireCol): #if the space hasn't been fired at before
                break

        if otherPlayer.gridShips.returnLocation(fireRow, fireCol) == 'A':#if shot hits the A ship
            otherPlayer.hitsA += 1
            self.shotHit(otherPlayer, fireRow, fireCol, "A")
        elif otherPlayer.gridShips.returnLocation(fireRow, fireCol) == 'B':#if shot hits the B ship
            otherPlayer.hitsB += 1
            self.shotHit(otherPlayer, fireRow, fireCol, "B")
        elif otherPlayer.gridShips.returnLocation(fireRow, fireCol) == 'C':#if shot hits the C ship
            otherPlayer.hitsC += 1
            self.shotHit(otherPlayer, fireRow, fireCol, "C")
        elif otherPlayer.gridShips.returnLocation(fireRow, fireCol) == 'S':#if shot hits the S ship
            otherPlayer.hitsS += 1
            self.shotHit(otherPlayer, fireRow, fireCol, "S")
        elif otherPlayer.gridShips.returnLocation(fireRow, fireCol) == 'D':#if shot hits the D ship
            otherPlayer.hitsD += 1
            self.shotHit(otherPlayer, fireRow, fireCol, "D")
        else:#if shot misses
            print("\n\n\n")
            print("The CPU missed.")
            otherPlayer.gridShips.changeSingleSpace(fireRow, fireCol, "O")
            self.gridShots.changeSingleSpace(fireRow, fireCol, 'O')
        print (("-" * 40) + "YOUR SHIP GRID" + ("-" * 40))
        otherPlayer.gridShips.printGrid()

    def shotHit(self, otherPlayer, fireRow, fireCol, ship):
        varLib = {
            "A": otherPlayer.hitsA,
            "B": otherPlayer.hitsB,
            "C": otherPlayer.hitsC,
            "D": otherPlayer.hitsD,
            "S": otherPlayer.hitsS
        }
        nameLib = {
            "A": "Aircraft Carrier",
            "B": "Battleship",
            "C": "Cruiser",
            "D": "Destroyer",
            "S": "Submarine"
        }
        sizeLib = {
            "A": 5,
            "B": 4,
            "C": 3,
            "D": 2,
            "S": 3
        }

        print("\n\n\n")
        print("The CPU hit your", nameLib[ship], "!")
        self.gridShots.changeSingleSpace(fireRow, fireCol, 'X')
        otherPlayer.gridShips.changeSingleSpace(fireRow, fireCol, "X")
        if varLib[ship] == sizeLib[ship]:  # if the cpu has hit the ship enough to sink it
            print("The CPU sunk your", nameLib[ship], "!")


    def placeShip(self, ship , size):
        badship = True
        orientation = 0
        startRow = 0
        startCol = 0

        while badship: # runs until the ship generated is valid
            badship = False
            orientation = random.randint(0, 1)

            # orientation 0 is horizontal, orientation 1 is vertical
            if orientation == 0: # if the ship is horizontal
                startCol = random.randint(0, 10-size)
                startRow = random.randint(0, 9)
                for i in range(size): # runs size amount of times
                    if not self.gridShips.isSpaceWater(startRow , startCol+i):# if the placement is not legal
                        badship = True
            elif orientation == 1: # if the ship is vertical
                startCol = random.randint(0, 9)
                startRow = random.randint(0, 10-size)
                for i in range(size): # runs size amount of times
                    if not self.gridShips.isSpaceWater(startRow + i, startCol):#if the placement is not legal
                        badship = True

        if orientation == 0: # if the ship is horizontal
            self.gridShips.changeRow(startRow, ship, startCol, size)
        if orientation == 1: # if the ship is vertical
            self.gridShips.changeCol(startCol, ship, startRow, size)

    # this method will determine if the Player's ship grid still
    # has ships or not
    # If they have no ships left, the other player wins
    # This method returns true if they still have ships
    # This method returns false if they don't have ships
    def stillHasShips(self):
        # this if-else statement is used to determine whether the game is over (meaning that the player has
        # no more turns left)
        if self.hitsA == 5 and self.hitsB == 4 and self.hitsC == 3 and self.hitsS == 3 and self.hitsD == 2:#if all the cpus ships have been sunk
            return False
        else:#if the cpu still has ships
            return True


