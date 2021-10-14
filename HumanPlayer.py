from Grid import Grid
from Player import Player

class HumanPlayer(Player):

    def __init__(self, t):
        Player.__init__(self)
        self.hitsA = 0
        self.hitsB = 0
        self.hitsC = 0
        self.hitsD = 0
        self.hitsS = 0

    def takeTurn(self, otherPlayer):

        self.gridShots.printGrid()

        row_shot = int(input("Enter the row where you would like to shoot: "))

        while row_shot < 0 or row_shot > 9:
            print("Invalid row")
            row_shot = int(input("Enter the row where you would like to shoot: "))

        column_shot = int(input("Enter the column where you would like to shoot: "))

        while column_shot < 0 or column_shot > 9:
            print("Invalid column")
            column_shot = int(input("Enter the column where you would like to shoot: "))

        if self.gridShots[row_shot][column_shot] == "A":
            print("You hit a ship!")
            self.gridShots[row_shot][column_shot] = "X"
            self.hitsA += 1
            if self.hitsA == 5:
                print("You sunk the enemy's Aircraft Carrier!")

            self.gridShots.printGrid()
        elif self.gridShots[row_shot][column_shot] == "B":
            print("You hit a ship!")
            self.gridShots[row_shot][column_shot] = "X"
            self.hitsB += 1
            if self.hitsB == 4:
                print("You sunk the enemy's Battleship!")

            self.gridShots.printGrid()
        elif self.gridShots[row_shot][column_shot] == "C":
            print("You hit a ship!")
            self.gridShots[row_shot][column_shot] = "X"
            self.hitsC += 1
            if self.hitsC == 3:
                print("You sunk the enemy's Cruiser!")

            self.gridShots.printGrid()
        elif self.gridShots[row_shot][column_shot] == "D":
            print("You hit a ship!")
            self.gridShots[row_shot][column_shot] = "X"
            self.hitsD += 1
            if self.hitsD == 2:
                print("You sunk the enemy's Destroyer!")

            self.gridShots.printGrid()
        elif self.gridShots[row_shot][column_shot] == "S":
            print("You hit a ship!")
            self.gridShots[row_shot][column_shot] = "X"
            self.hitsS += 1
            if self.hitsS == 3:
                print("You sunk the enemy's Submarine!")

            self.gridShots.printGrid()
        else:
            print("You missed. That sucks!")

        if self.hitsA == 5 and self.hitsB == 4 and self.hitsC == 3 and self.hitsS == 3 and self.hitsD == 2:
            return False
        else:
            return True

    def placeShip(self, ship , size):

        orientation = input("Do you want the ship to be horizontal or vertical? 0 for vertical, 1 for horizontal: ")

        while orientation != "0" or orientation != "1":
            orientation = input(
                "Do you want the ship to be horizontal or vertical? 0 for vertical, 1 for horizontal: ")

        if orientation == "0":
            startRow = int(input("Please enter the first row of your ship: "))

            while startRow < 0 or startRow > 9 or startRow + size - 1 > 9:
                print("Invalid row.")
                startRow = int(input("Please enter the first row of your ship: "))

            col = int(input("Please enter the first column of your ship: "))

            while col < 0 or col > 9:
                print("Invalid column.")
                col = int(input("Please enter the column of your ship: "))

            for i in range(size):
                self.gridShips[startRow + i][col] = ship

        elif orientation == "1":
            startCol = int(input("Please enter the first column of your ship: "))

            while startCol < 0 or startCol > 9 or startCol + size - 1 > 9:
                print("Invalid column.")
                startCol = int(input("Please enter the first column of your ship: "))

            row = int(input("Please enter the row of your ship: "))

            while row < 0 or row > 9:
                print("Invalid row.")
                row = int(input("Please enter the row of your ship: "))

            for i in range(size):
                self.gridShips[row][startCol + i] = ship

        self.gridShips.printGrid()







