#move check

import sys
import numpy as np
import csv
import random
import copy
import time

# CAR_IDS = ['#','A', 'B', 'C', 'D', 'E']
# TRUCK_IDS = ['O','P','Q','R','S','T','U']

class Vehicle():
    def __init__(self, id, x, y, orientation, length):
        self.id = id
        self.x = x
        self.y = y
        self.orientation = orientation
        self.length = int(length)
class Gameboard():
#GRID = 6

    def __init__(self, vehicles):
        width, height = 6, 6;
        #Matrix = [["X" for x in range(width)] for y in range(height)]

        self.board = [["." for x in range(width)] for y in range(height)]
        self.vehicles = vehicles
        for vehicle in self.vehicles:
            if vehicle.orientation == 'H':
                for i in range(vehicle.length):
                    self.board[int(vehicle.y)][int(vehicle.x)+i] = vehicle.id
            if vehicle.orientation == 'V':
                for i in range(vehicle.length):
                    self.board[int(vehicle.y)+i][int(vehicle.x)] = vehicle.id

    def printboard(self):
        print("New board:")
        print('\n\n'.join(['      '.join(['{}'.format(item) for item in row]) for row in self.board]))

    def checkformoves(self):
        possibleBoards = []
        for vehicle in self.vehicles:
            x_position = int(vehicle.x)
            y_position = int(vehicle.y)
            move = 1
            if vehicle.orientation == 'H':
                if x_position != 0:
                    if self.board[y_position][x_position - 1] == '.':
                        newVehicles = self.vehicles.copy()
                        newVehicle = Vehicle(vehicle.id, x_position - 1, y_position, vehicle.orientation, vehicle.length)
                        newVehicles.remove(vehicle)
                        newVehicles.append(newVehicle)
                        possibleBoards.append(newVehicles)
                if (x_position + vehicle.length - 1) != 5:
                    if self.board[y_position][x_position + (vehicle.length)] == '.':
                        newVehicles = self.vehicles.copy()
                        newVehicle = Vehicle(vehicle.id, x_position + 1, y_position, vehicle.orientation, vehicle.length)
                        newVehicles.remove(vehicle)
                        newVehicles.append(newVehicle)
                        possibleBoards.append(newVehicles)
            if vehicle.orientation == 'V':
                if y_position != 0:
                    if self.board[y_position - 1][x_position] == '.':
                        newVehicles = self.vehicles.copy()
                        newVehicle = Vehicle(vehicle.id, x_position, y_position - 1, vehicle.orientation, vehicle.length)
                        newVehicles.remove(vehicle)
                        newVehicles.append(newVehicle)
                        possibleBoards.append(newVehicles)
                if y_position + (vehicle.length - 1) != 5:
                    if self.board[y_position + vehicle.length][x_position] == '.':
                        newVehicles = self.vehicles.copy()
                        newVehicle = Vehicle(vehicle.id, x_position, y_position + 1, vehicle.orientation, vehicle.length)
                        newVehicles.remove(vehicle)
                        newVehicles.append(newVehicle)
                        possibleBoards.append(newVehicles)

        return possibleBoards

    def hasSolved(self):
        for vehicle in self.vehicles:
            if vehicle.id == '#' and vehicle.x == 4 and vehicle.y == 2 and vehicle.orientation == "H":
                return True

        return False



    def printPossibilities(self):
        for board in Gameboard.checkformoves(self):
            for vehicle in board:
                print(vehicle.id, vehicle.x, vehicle.y, vehicle.orientation)


def uploadBoard():
    vehicles = []
    with open('Boards/game1.csv', 'r') as csvboard:
        boardreader = csv.DictReader(csvboard)
        for row in boardreader:
            vehicles.append(Vehicle(row['id'], row['x'], row['y'], row['orientation'], row['length']))

    return vehicles

def randomSolver(gameboard):
<<<<<<< HEAD
    runtimes = open('runtime.csv', 'w')
    runwriter = csv.writer(runtimes)
    for i in range(5000):
        start = time.time()
        print (i)
        newgameboard = copy.copy(gameboard)
        while True:
            newgameboard = Gameboard(random.choice(newgameboard.checkformoves()))
            if newgameboard.hasSolved():
                runwriter.writerow([time.time() - start])
                break
=======
    i=0
    newgameboard = copy.copy(gameboard)
    while True:
        newgameboard = Gameboard(random.choice(newgameboard.checkformoves()))
        print("Try: " + str(i))
        i += 1
        if newgameboard.hasSolved():
            break
    print("ping pong ching chong, you solved tha board")

def breadth_First_Search(gameboard):
    boardsQueue = queue.Queue
    visited = []

    boardsQueue.put(gameboard)
    visited.append(gameboard)

    while boardsQueue is != 0 :
        new_board = boardsQueue.get
        childList = checkformoves(new_board)

        for child in childList:
            maak child_board

            if child_board is not in visited:

                if child_board.hasSolved:
                    print("solved")
                    break
                else
                    boardsQueue.put(child_board)
                    visited.append(child_board)




>>>>>>> 888a269e933a078301182fd4700ccb470e3df369



p = Gameboard(uploadBoard())
p.printboard()
input(" ")
randomSolver(p)
