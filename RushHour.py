import sys
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

    ##def checkformoves(self):


    def uploadBoard(self):
        self.vehicles = []
        with open('Boards/game1length2.csv', 'r') as csvboard:
            boardreader = csv.DictReader(csvboard)
            for row in boardreader:
                self.vehicles.append(Vehicle(row['id'], row['x'], row['y'], row['orientation']))

p = Gameboard()
p.printboard()
p.uploadBoard()
p.setupBoard()
p.printboard()
