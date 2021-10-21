from HumanPlayer import HumanPlayer
from ComputerPlayer import ComputerPlayer

class Game:

    def __init__(self):
        self.human = HumanPlayer()
        self.cpu = ComputerPlayer()

    def playGame(self):
        self.cpu.createShipGrid()
        #here so we can cheat vs cpu
        print("CPU SHIP GRID")
        self.cpu.gridShips.printGrid()
        self.human.createShipGrid()

        while True: # runs until break
            if self.human.stillHasShips(): # if the human still has ships
                self.human.takeTurn(self.cpu)
            else: # if the human doesnt have ships
                humanWon = False
                break

            if self.cpu.stillHasShips(): # if the cpu still has ships
                self.cpu.takeTurn(self.human)
            else: # if the cpu doesnt have ships
                humanWon = True
                break

        if humanWon: # if the human won
            print("Congratulations!!!!! You Won!!!!!!!!!!")
        else: # if the cpu won
            print("WOW! You are unbelievably bad at this game.")

