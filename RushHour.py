import sys
<<<<<<< HEAD
# from python import RED
# import numpy as np


def main():
#GRID = 6

# Create a grid
    width, height = 6, 6;
    #Matrix = [["X" for x in range(width)] for y in range(height)]
    a = 2
    b = 1
    c = 2
    grid_x=[]
    red = ""

    def RED():
        grid_x[a][b:(b+2)] = ['#', '#']
        red = grid_x[a][b:(b+2)]
        print (grid_x[a][b:c])


    def moveLeft():
        grid_x[a][b:(c+1)] = ['x', 'x']
        grid_x[a][(b+1):(c+2)] = ['#', '#']

    def hasWon():
        if red == grid_x[2][4:5]:
            print("you have won")
        else :
            print("try some other moves")

    grid_x = [["x" for x in range(6)]for y in range(6)]
    # for x in range(height):
    #     grid_y=[]
    #     for y in range (width):
    #         #
    #         grid_y.append(' ')
    #     grid_x.append(grid_y)

    RED()

    moveLeft()
    print(grid_x[a][b::b])
    # hasWon()



    print(grid_x)

    #print(RED.position_x_R)


    # for i in range(height):
    #     for j in range (width):
    #         print("  ", end='')
    #         print(grid_x[i][j], end='')
    #         print("  ", end='')
    #     print('\n')

if __name__ == "__main__":
    main()
=======
import numpy as np
import csv

CAR_IDS = ['#','A', 'B', 'C', 'D', 'E']
TRUCK_IDS = ['O','P','Q','R','S','T','U']

class Vehicle():
    def __init__(self, id, x, y, orientation):
        self.id = id
        self.x = x
        self.y = y
        self.orientation = orientation
        if id in CAR_IDS:
            self.length = 2
        if id in TRUCK_IDS:
            self.length = 3
class Gameboard():
#GRID = 6

    def __init__(self):
        width, height = 6, 6;
        #Matrix = [["X" for x in range(width)] for y in range(height)]

        self.board = [["." for x in range(width)] for y in range(height)]

    def printboard(self):
        print("New board:")
        print('\n\n'.join(['      '.join(['{}'.format(item) for item in row]) for row in self.board]))

    def setupBoard(self):
        for vehicle in self.vehicles:
            if vehicle.orientation == 'H':
                for i in range(vehicle.length):
                    self.board[int(vehicle.y)][int(vehicle.x)+i] = vehicle.id
            if vehicle.orientation == 'V':
                for i in range(vehicle.length):
                    self.board[int(vehicle.y)+i][int(vehicle.x)] = vehicle.id

    def checkformoves(self):


    def uploadBoard(self):
        self.vehicles = []
        with open('game1length2.csv', 'r') as csvboard:
            boardreader = csv.DictReader(csvboard)
            for row in boardreader:
                self.vehicles.append(Vehicle(row['id'], row['x'], row['y'], row['orientation']))

p = Gameboard()
p.printboard()
p.uploadBoard()
p.setupBoard()
p.printboard()
>>>>>>> c722a3a02abc02961ee0e50662da7c12bcc1a9d0
