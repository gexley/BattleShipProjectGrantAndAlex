from ComputerPlayer import ComputerPlayer
from Game import Game

c = ComputerPlayer()
c.createShipGrid()
c.printGrids()

g = Game()

g.playGame()


