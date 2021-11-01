from HumanPlayer import HumanPlayer
from AdvancedComputerPlayer import AdvancedComputerPlayer

class AdvancedComputerPlayerGame:

    def __init__(self):
        self.human = HumanPlayer()
        self.cpu = AdvancedComputerPlayer()

    def playGame(self):
        self.cpu.createShipGrid()
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
            print("Congratulations!!!!! You Won!!!!!!!!!!")
        else:
            print("WOW! You are unbelievably bad at this game.")
