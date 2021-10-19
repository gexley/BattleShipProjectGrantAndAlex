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
            print("The CPU hit your Aircraft Carrier!")
            self.gridShots.changeSingleSpace(fireRow, fireCol, 'X')
            otherPlayer.hitsA += 1
            otherPlayer.gridShips.changeSingleSpace(fireRow, fireCol, "X")
            if otherPlayer.hitsA == 5:#if the cpu has hit the ship 5 times
                print("The CPU sunk your Aircraft Carrier!")
        elif otherPlayer.gridShips.returnLocation(fireRow, fireCol) == 'B':#if shot hits the B ship
            print("The CPU hit your Battleship!")
            self.gridShots.changeSingleSpace(fireRow, fireCol, 'X')
            otherPlayer.gridShips.changeSingleSpace(fireRow, fireCol, "X")
            otherPlayer.hitsB += 1
            if otherPlayer.hitsB == 4:#if the cpu has hit the ship 4 times
                print("The CPU sunk your Battleship!")
        elif otherPlayer.gridShips.returnLocation(fireRow, fireCol) == 'C':#if shot hits the C ship
            print("The CPU hit your Cruiser!")
            self.gridShots.changeSingleSpace(fireRow, fireCol, 'X')
            otherPlayer.gridShips.changeSingleSpace(fireRow, fireCol, "X")
            otherPlayer.hitsC += 1
            if otherPlayer.hitsC == 3:#if the cpu has hit the ship 3 times
                print("The CPU sunk your Cruiser!")
        elif otherPlayer.gridShips.returnLocation(fireRow, fireCol) == 'S':#if shot hits the S ship
            print("The CPU hit your Submarine!")
            self.gridShots.changeSingleSpace(fireRow, fireCol, 'X')
            otherPlayer.gridShips.changeSingleSpace(fireRow, fireCol, "X")
            otherPlayer.hitsS += 1
            if otherPlayer.hitsS == 3:#if the cpu has hit the ship 3 times
                print("The CPU sunk your Submarine!")
        elif otherPlayer.gridShips.returnLocation(fireRow, fireCol) == 'D':#if shot hits the D ship
            print("The CPU hit your Destroyer!")
            self.gridShots.changeSingleSpace(fireRow, fireCol, 'X')
            otherPlayer.gridShips.changeSingleSpace(fireRow, fireCol, "X")
            otherPlayer.hitsD += 1
            if otherPlayer.hitsD == 2:#if the cpu has hit the ship 2 times
                print("The CPU sunk your Destroyer!")
        else:
            print("The CPU missed.")#if shot misses
            otherPlayer.gridShips.changeSingleSpace(fireRow, fireCol, "O")

        return otherPlayer.stillHasShips()

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
                    if not self.gridShips.isSpaceWater(startCol, startRow + i): # if the placement is not legal
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
        if self.hitsA == 5 and self.hitsB == 4 and self.hitsC == 3 and self.hitsS == 3 and self.hitsD == 2:
            return False
        else:
            return True


