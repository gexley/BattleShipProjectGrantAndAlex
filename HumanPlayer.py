from Player import Player


class HumanPlayer(Player):

    def __init__(self):
        Player.__init__(self)
        self.hitsA = 0
        self.hitsB = 0
        self.hitsC = 0
        self.hitsD = 0
        self.hitsS = 0

    def takeTurn(self, otherPlayer):
        if self.stillHasShips() == False:
            return False

        self.gridShots.printGrid()

        already_hit = ["X", "O"]
        location = "O"
        fireRow = 0
        fireCol = 0
        count = 0
        # runs while the player already fired (more than once) at the location they chose
        while location in already_hit:
            # runs every time after the first iteration of the while-loop
            if count > 0:
                print("You already fired there. Choose a new spot!")

            fireRow = int(input("Enter the row where you would like to shoot: "))
            # runs while fireRow is out of the range of valid rows in gridShots
            while fireRow < 0 or fireRow > 9:
                print("Invalid row")
                fireRow = int(input("Enter the row where you would like to shoot: "))

            fireCol = int(input("Enter the column where you would like to shoot: "))
            # runs while fireCol is out of the range of valid columns in gridShots
            while fireCol < 0 or fireCol > 9:
                print("Invalid column")
                fireCol = int(input("Enter the column where you would like to shoot: "))

            location = otherPlayer.gridShips.returnLocation(fireRow, fireCol)


        ships = ["A", "B", "C", "D", "S"]

        # used to determine whether a ship was hit or if the player missed
        if location in ships:
            print("You hit a ship!")
            self.gridShots.changeSingleSpace(fireRow, fireCol, "X")
            otherPlayer.gridShips.changeSingleSpace(fireRow, fireCol, "X")
            self.gridShots.printGrid()
        elif otherPlayer.gridShips.isSpaceWater(fireRow, fireCol):
            print("You missed. That sucks!")
            self.gridShots.changeSingleSpace(fireRow, fireCol, "O")
            otherPlayer.gridShips.changeSingleSpace(fireRow, fireCol, "O")

        # this if-elif-else statement handles which type of ship was hit, as well as if the player missed
        # or fired at a single location more than once
        if location == "A":
            otherPlayer.hitsA += 1
            if otherPlayer.hitsA == 5:
                print("You sunk the CPU's Aircraft Carrier!")
        elif location == "B":
            otherPlayer.hitsB += 1
            if otherPlayer.hitsB == 4:
                print("You sunk the CPU's Battleship!")
        elif location == "C":
            otherPlayer.hitsC += 1
            if otherPlayer.hitsC == 3:
                print("You sunk the CPU's Cruiser!")
        elif location == "D":
            otherPlayer.hitsD += 1
            if otherPlayer.hitsD == 2:
                print("You sunk the CPU's Destroyer!")
        elif location == "S":
            otherPlayer.hitsS += 1
            if otherPlayer.hitsS == 3:
                print("You sunk the CPU's Submarine!")

        return otherPlayer.stillHasShips()

    def placeShip(self, ship , size):
        orientation = int(input("Do you want the ship to be vertical or horizontal? 0 for vertical, 1 for horizontal: "))

        valid_inputs = [0, 1]

        # runs while orientation is an invalid input
        while orientation not in valid_inputs:
            print("Invalid input.")
            orientation = int(input(
                "Do you want the ship to be vertical or horizontal? 0 for vertical, 1 for horizontal: "))

        valid = False

        # this if-elif statement handles whether the orientation is 0 or 1 (vertical or horizontal)
        if orientation == 0:
            startRow = int(input("Please enter the first row of your ship: "))

            # runs while the value for startRow is an illegal location
            while startRow < 0 or startRow > 9 or startRow + size - 1 > 9:
                print("Invalid row.")
                startRow = int(input("Please enter the first row of your ship: "))

            col = int(input("Please enter the column of your ship: "))

            # runs while the value for the column of the ship is illegal
            while valid == False:
                valid = True

                # used to traverse the Player's ship grid
                # from row "startRow" to row "startRow + size - 1" in column "col"
                for i in range(startRow, startRow + size):
                    # handles conditions that, if true, result in illegal ship placement
                    if col < 0 or col > 9:
                        valid = False
                        print("Invalid column.")
                        col = int(input("Please enter the column of your ship: "))
                    elif self.gridShips.isSpaceWater(i, col) == False:
                        valid = False
                        print("Invalid column.")
                        col = int(input("Please enter the column of your ship: "))

            self.gridShips.changeCol(col, ship, startRow, size)
        elif orientation == 1:
            startCol = int(input("Please enter the first column of your ship: "))

            # runs while the value for startCol is an illegal location
            while startCol < 0 or startCol > 9 or startCol + size - 1 > 9:
                print("Invalid column.")
                startCol = int(input("Please enter the first column of your ship: "))

            row = int(input("Please enter the row of your ship: "))

            # used to ensure that ship placement is ultimately valid
            while valid == False:
                valid = True

                # used to traverse the Player's ship grid
                # from column "startCol" to column "startCol + size - 1" in row "row"
                for i in range(startCol, startCol + size):
                    # handles conditions that, if true, result in illegal ship placement
                    if row < 0 or row > 9:
                        valid = False
                        print("Invalid row.")
                        row = int(input("Please enter the row of your ship: "))
                    elif self.gridShips.isSpaceWater(row, i) == False:
                        valid = False
                        print("Invalid row.")
                        row = int(input("Please enter the row of your ship: "))

            self.gridShips.changeRow(row, ship, startCol, size)

        self.gridShips.printGrid()

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







