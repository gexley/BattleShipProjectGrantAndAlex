from HumanPlayer import HumanPlayer
from ComputerPlayer import ComputerPlayer

class Game:

    def __init__(self):
        self.human = HumanPlayer()
        self.cpu = ComputerPlayer()

    def playGame(self):
        self.cpu.createShipGrid()
        print("CPU SHIP GRID")
        self.cpu.gridShips.printGrid()
        self.human.createShipGrid()



        while True:
            if self.human.stillHasShips():
                self.human.takeTurn(self.cpu)
            else:
                humanWon = False
                break
            if self.cpu.stillHasShips():
                self.cpu.takeTurn(self.human)
            else:
                humanWon = True
                break
        if humanWon:
            print("Congradulations!!!!! You Won!!!!!!!!!!")
        else:
            print("WOW! You are unbelievably bad at this game")

