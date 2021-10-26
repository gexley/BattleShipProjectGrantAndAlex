import random
from Player import Player
from math import abs


class GrantCPU(Player):

    def __init__(self):
        Player.__init__(self)
        self.hitsA = 0
        self.hitsB = 0
        self.hitsC = 0
        self.hitsS = 0
        self.hitsD = 0
        self.fireList = []
        self.searching = True
        self.totalHits = 0
        self.totalSpacesSunk = 0

    def takeTurn(self, otherPlayer):
        self.stillSearching()
        fireLoc = self.whereToFire()
        fireRow = fireLoc[0]
        fireCol = fireLoc[1]

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
            print("CPU Grant missed.")
            otherPlayer.gridShips.changeSingleSpace(fireRow, fireCol, "O")
            self.gridShots.changeSingleSpace(fireRow, fireCol, "O")
            self.fireList.append((fireRow, fireCol, "O", "O"))
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
        self.totalHits += 1
        print("CPU Grant hit your ship!")
        self.gridShots.changeSingleSpace(fireRow, fireCol, 'X')
        otherPlayer.gridShips.changeSingleSpace(fireRow, fireCol, "X")
        if varLib[ship] == sizeLib[ship]:  # if the cpu has hit the ship enough to sink it
            print("CPU Grant sunk your", nameLib[ship], "!")
            self.fireList.append((fireRow, fireCol, "X", ship))
            self.totalSpacesSunk += sizeLib[ship]
        else:
            self.fireList.append((fireRow, fireCol, "X", "O"))

    def whereToFire(self):
        if self.searching:
            while True:
                fireRow = random.randint(0,9)
                fireCol = random.randint(0,9)
                if self.gridShots.isSpaceWater(fireRow, fireCol) and (fireRow + fireCol) % 2 == 0:
                    return (fireRow, fireCol)
        else:
            for i in reversed(self.fireList):
                if i[2] == "X":
                    possibleShots = [(i[0]+1,i[1]),(i[0]-1,i[1]),(i[0],i[1]+1),(i[0],i[1]-1)]
                    for a in possibleShots:
                        if (a[0] >= 0 and a[0] < 10) and (a[1] >= 0 and a[1] < 10):
                            optimal_row = a[0]
                            optimal_column = a[1]

                            if self.gridShots.isSpaceWater(optimal_row, optimal_column):
                                return (optimal_row, optimal_column)

                            while self.gridShots.returnLocation(optimal_row, optimal_column) == "X":
                                #this outer if-elif-else statement is used to determine the orientation of the Xs
                                if math.abs(optimal_column - i[1]) == 1:
                                    if (optimal_column + 1 >= 0) and (optimal_column + 1 < 10) \
                                        and self.gridShots.isSpaceWater(optimal_row, optimal_column + 1):
                                        optimal_column += 1
                                        return (optimal_row, optimal_column)
                                    elif (optimal_column - 1 >= 0 and optimal_column - 1 < 10) \
                                        and self.gridShots.isSpaceWater(optimal_row, optimal_column - 1):
                                        optimal_column -= 1
                                        return (optimal_row, optimal_column)
                                    else:
                                        continue
                                elif math.abs(optimal_row - i[0]) == 1:
                                    if (optimal_row + 1 >= 0) and (optimal_row + 1 < 10) \
                                        and self.gridShots.isSpaceWater(optimal_row + 1, optimal_column):
                                        optimal_row += 1
                                        return (optimal_row, optimal_column)
                                    elif (optimal_row - 1 >= 0) and (optimal_row - 1 < 10) \
                                        and self.gridShots.isSpaceWater(optimal_row - 1, optimal_column):
                                        optimal_row -= 1
                                        return (optimal_row, optimal_column)
                                    else:
                                        continue

    def stillSearching(self):
        if self.totalHits > self.totalSpacesSunk:
            self.searching = False
        else:
            self.searching = True

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