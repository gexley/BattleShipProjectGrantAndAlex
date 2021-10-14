from Grid import Grid
from Player import Player

class HumanPlayer(Player):

    def __init__(self, t):
        super().__init__()

    def takeTurn(self):

    def placeShip(self, ship , size):
        orientation = input("Do you want the ship to be horizontal or vertical? 0 for vertical, 1 for horizontal: ")

        while orientation != "0" or orientation != "1":
            orientation = input(
                "Do you want the ship to be horizontal or vertical? 0 for vertical, 1 for horizontal: ")

        if orientation == "0":
            startRow = int(input("Please enter the starting row of your ship: "))

            while startRow < 0 or startRow > 9 or startRow + size - 1 > 9:
                print("Invalid Row.")
                startRow = int(input("Please enter the starting row of your ship: "))

            col = int(input("Please enter the starting column of your ship: "))

            while col < 0 or startCol > 9:
                print("Invalid Column.")
                col = int(input("Please enter the column of your ship: "))

            for i in range(size):
                self.gridShips[i][col] = ""

        elif orientation == "1":
            startCol = int(input("Please enter the first column of your ship: "))







