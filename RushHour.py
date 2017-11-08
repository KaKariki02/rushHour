import sys
<<<<<<< HEAD
import numpy as np

class gameboard(object):
    def __init__(self):
        self.board = [[0 for x in range(6)] for y in range(6)]

    def printboard(self):
        print(np.matrix(self.board))

    def  putcar(self):
        self.board[1][1] = "A"
        self.board[2][1] = "A"
=======
from python import RED


def main():
#GRID = 6

# Create a grid
    width, height = 6, 6;
    #Matrix = [["X" for x in range(width)] for y in range(height)]

    grid_x=[]

    def moveLeft():
        a = 2
        b = 0
        grid_x[a][b] = '#'
        b -= 1

    for x in range(height):
        grid_y=[]
        for y in range (width):
            #
            grid_y.append('x')
        grid_x.append(grid_y)

    print(grid_x[2][0:2])
    grid_x[2][0:1] = ['#', '#']



    #print(RED.position_x_R)
    print(grid_x)

    for i in range(height):
        for j in range (width):
            print("  ", end='')
            print(grid_x[i][j], end='')
            print("  ", end='')
        print('\n')
>>>>>>> c2d1b265ccda7eb7b486f1c4917f9876694e8cdd

board = gameboard()
board.printboard()
board.putcar()
board.printboard()
