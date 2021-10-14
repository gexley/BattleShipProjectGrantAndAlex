from HumanPlayer import HumanPlayer
from ComputerPlayer import ComputerPlayer

class Game:

    def __init__(self):
        self.human = HumanPlayer()
        self.cpu = ComputerPlayer()

    def playGame(self):
        self.cpu.createShipGrid()
        self.human.createShipGrid()

        while True:
            if not human.takeTurn():
                break
            if not cpu.takeTurn():
                break


