"""Tic-Tac-Toe"""

# structure
'''
1 2 3
4 5 6
7 8 9
'''
import math

class Game():
    # initializes the game
    def __init__(self, length):
        self.length = length
        self.playerTurn = True
        self.gameState = self.initializeField()

    # initializes or resets the field
    def initializeField(self):
        result = []
        for i in range(self.length):
            result.append([])
            for j in range(self.length):
                result[i].append("-")
        return result

    # returns array with free indexes
    def getFreeSpaces(self):
        result = []
        for i in range(self.length):
            for j in range(self.length):
                if self.gameState[i][j] == "-":
                    result.append(i * self.length + j + 1)
        return result

    # returns -1 if a player won the game, 0 if there is a draw, 1 if the game is not over
    def checkGameState(self):
        if not self.getFreeSpaces():
            return 0

        win = False

        # horizontal
        for i in range(self.length):
            sign = self.gameState[i][0]
            if sign == "-":
                continue
            win = True
            for j in range(1, self.length):
                if self.gameState[i][j] == sign:
                    continue
                win = False
                break

            if win == True:
                return -1

        # diagonal
        for j in range(self.length):
            sign = self.gameState[0][j]
            if sign == "-":
                continue
            win = True
            for i in range(1, self.length):
                if self.gameState[i][j] == sign:
                    continue
                win = False
                break

            if win == True:
                return -1

        # vertical
        sign = self.gameState[0][0]
        if sign != "-":
            win = True
            for k in range(1, self.length):
                if self.gameState[k][k] == sign:
                    continue
                win = False
                break

        if win == True:
            return -1

        sign = self.gameState[self.length - 1][self.length - 1]
        if sign != "-":
            win = True
            for k in range(0, self.length - 1):
                if self.gameState[k][k] == sign:
                    continue
                win = False
                break

            if win == True:
                return -1
        return 1

    # sets a sign at a free place, return true if it was possible
    def setSign(self, index):
        if index in self.getFreeSpaces():
            index -= 1
            i = math.floor(index / self.length)
            j = index % self.length
            if self.playerTurn:
                self.gameState[i][j] = "X"
            else:
                self.gameState[i][j] = "O"
            return True

        return False

    # prints out the gameState
    def printGameState(self):
        for line in self.gameState:
            print(line)

    # plays the game
    def game(self):
        while self.checkGameState() == 1:
            self.printGameState()
            print("\n")
            if self.playerTurn:
                space = input("Player X : ")
            else:
                space = input("Player O : ")

            try:
                space = int(space)
                if not self.setSign(space):
                    raise Exception
            except:
                print("Retry !")
                continue

            self.playerTurn = not self.playerTurn

        print("\n")
        self.printGameState()

        if self.checkGameState() == 0:
            print("Draw !")

        else:
            if self.playerTurn:
                print("Player O wins!")
            else:
                print("Player X wins!")


def main():
    game = Game(3)
    game.game()

if __name__ == "__main__":
    main()