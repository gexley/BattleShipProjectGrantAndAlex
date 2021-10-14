from Grid import Grid

class Player:

    def __init__(self):
        self.gridShips = Grid()
        self.gridShots = Grid()

    def takeTurn(self):
        # over write in the HumanPlayer and ComputerPlayer subclasses
        pass

    def placeShip(self, ship , size ):
        # over write in the HumanPlayer and ComputerPlayer subclasses
        pass

    def createShipGrid(self):
        self.placeShip( "A", 5 )
        self.placeShip( "B", 4 )
        self.placeShip( "C", 3 )
        self.placeShip( "S", 3 )
        self.placeShip( "D", 2 )

    def printGrids(self):
        print("Ship Grid")
        self.gridShips.printGrid()
        print("Shot Grid")
        self.gridShots.printGrid()
