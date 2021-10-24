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
        """Allows the human player to take a turn
        (which consists of firing at a location and getting a message if they hit one of the ComputerPlayer's ships).

        :param otherPlayer: a ComputerPlayer Subclass object
        :return: a boolean that is True if the HumanPlayer object can take another turn, and False if they cannot
        """

        print(("-" * 40) + "SHOT GRID" + ("-" * 40))
        self.gridShots.printGrid()

        already_hit = ["X", "O"]
        location = "O"
        fireRow = "0"
        fireCol = "0"
        count = 0
        validRowsAndCols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        # runs while the player already fired (more than once) at the location they chose
        while location in already_hit:
            # runs every time after the first iteration of the while-loop
            if count > 0:
                print("You already fired there. Choose a new spot!")

            fireRow = input("Enter the row where you would like to shoot: ")
            # runs while fireRow is out of the range of valid rows in gridShots
            while fireRow not in validRowsAndCols:
                print("Invalid row")
                fireRow = input("Enter the row where you would like to shoot: ")

            fireCol = input("Enter the column where you would like to shoot: ")
            # runs while fireCol is out of the range of valid columns in gridShots
            while fireCol not in validRowsAndCols:
                print("Invalid column")
                fireCol = input("Enter the column where you would like to shoot: ")

            location = otherPlayer.gridShips.returnLocation(int(fireRow), int(fireCol))


        ships = ["A", "B", "C", "D", "S"]

        # used to determine whether a ship was hit or if the player missed
        if location in ships:
            print("\n\n\n")
            print("You hit a ship!")
            self.gridShots.changeSingleSpace(int(fireRow), int(fireCol), "X")
            otherPlayer.gridShips.changeSingleSpace(int(fireRow), int(fireCol), "X")

            print(("-" * 40) + "SHOT GRID" + ("-" * 40))
            self.gridShots.printGrid()
        elif otherPlayer.gridShips.isSpaceWater(int(fireRow), int(fireCol)):
            print("\n\n\n")
            print("You missed. That sucks!")
            self.gridShots.changeSingleSpace(int(fireRow), int(fireCol), "O")
            otherPlayer.gridShips.changeSingleSpace(int(fireRow), int(fireCol), "O")

            print(("-" * 40) + "SHOT GRID" + ("-" * 40))
            self.gridShots.printGrid()

        # this if-elif-else statement handles which type of ship was hit, as well as if the player missed
        # or fired at a single location more than once
        # the nested if-statements are used to give information about whether a ship was sunk (and what ship was sunk)
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
        """This method legally places a ship on the HumanPlayer's ship grid

        :param ship: a single-character string representing the type of ship to be placed
        :param size: an int representing the size of the ship
        """

        ship_dict = { "A": "Aircraft Carrier",
                      "B": "Battleship",
                      "C": "Cruiser",
                      "D": "Destroyer",
                      "S": "Submarine"
        }

        # prints the blank grid (only runs the first time placeShip() is called)
        if ship == "A":
            print("\n\n\n")
            print(("-" * 40) + "YOUR SHIP GRID" + ("-" * 40))
            self.gridShips.printGrid()

        orientation = input("Do you want your " + ship_dict[ship] +
                                " to be vertical or horizontal? 0 for vertical, 1 for horizontal: ")

        valid_orientations = ["0", "1"]
        validRowsAndCols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        # runs while orientation is an invalid input
        while orientation not in valid_orientations:
            print("Invalid input.")
            orientation = input(
                "Do you want the ship to be vertical or horizontal? 0 for vertical, 1 for horizontal: ")

        valid = False

        # this if-elif statement handles whether the orientation is 0 or 1 (vertical or horizontal)
        if orientation == "0":
            startRow = input("Please enter the first row of your ship: ")

            # runs while the value for startRow is an illegal location
            while startRow not in validRowsAndCols or int(startRow) + size - 1 > 9:
                print("Invalid row.")
                startRow = input("Please enter the first row of your ship: ")

            col = input("Please enter the column of your ship: ")

            # used to ensure that ship placement is ultimately valid
            while valid == False:
                valid = True

                # used to traverse the Player's ship grid
                # from row "startRow" to row "startRow + size - 1" in column "col"
                for i in range(int(startRow), int(startRow) + size):
                    # handles conditions that, if true, result in illegal ship placement
                    if col not in validRowsAndCols:
                        valid = False
                        print("Invalid column.")
                        col = input("Please enter the column of your ship: ")
                    elif self.gridShips.isSpaceWater(i, int(col)) == False:
                        valid = False
                        print("Invalid column.")
                        col = input("Please enter the column of your ship: ")

            self.gridShips.changeCol(int(col), ship, int(startRow), size)
        elif orientation == "1":
            startCol = input("Please enter the first column of your ship: ")

            # runs while the value for startCol is an illegal location
            while startCol not in validRowsAndCols or int(startCol) + size - 1 > 9:
                print("Invalid column.")
                startCol = input("Please enter the first column of your ship: ")

            row = input("Please enter the row of your ship: ")

            # used to ensure that ship placement is ultimately valid
            while valid == False:
                valid = True

                # used to traverse the Player's ship grid
                # from column "startCol" to column "startCol + size - 1" in row "row"
                for i in range(int(startCol), int(startCol) + size):
                    # handles conditions that, if true, result in illegal ship placement
                    if row not in validRowsAndCols:
                        valid = False
                        print("Invalid row.")
                        row = input("Please enter the row of your ship: ")
                    elif self.gridShips.isSpaceWater(int(row), i) == False:
                        valid = False
                        print("Invalid row.")
                        row = input("Please enter the row of your ship: ")

            self.gridShips.changeRow(int(row), ship, int(startCol), size)

        print(("-" * 40) + "SHIP GRID" + ("-" * 40))
        self.gridShips.printGrid()

    def stillHasShips(self):
        """Determines if the Player's ship grid still has ships or not

        If they have no ships left, the other player wins

        :return: Ture if the HumanPlayer still has ships, False if they do not
        """

        # this if-else statement is used to determine whether the game is over (meaning that the player has
        # no more turns left)
        if self.hitsA == 5 and self.hitsB == 4 and self.hitsC == 3 and \
                self.hitsS == 3 and self.hitsD == 2:
            return False
        else:
            return True







