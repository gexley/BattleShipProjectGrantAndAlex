from HumanPlayer import HumanPlayer

# instantiate a HumanPlayer object
h = HumanPlayer()

# printGrids() method (from Player class)
h.printGrids()

# used to test placeShip() method in HumanPlayer class
h.createShipGrid()

# printGrids() method
h.printGrids()

# stillHasShips() method
print(str(h.stillHasShips()))