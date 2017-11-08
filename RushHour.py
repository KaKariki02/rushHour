import sys
import numpy as np

class gameboard(object):
    def __init__(self):
        self.board = [[0 for x in range(6)] for y in range(6)]

    def printboard(self):
        print(np.matrix(self.board))

    def  putcar(self):
        self.board[1][1] = "A"
        self.board[2][1] = "A"

board = gameboard()
board.printboard()
board.putcar()
board.printboard()
