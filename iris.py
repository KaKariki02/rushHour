#move check

import sys
import numpy as np
import csv
import random
import copy
import time
import queue

# CAR_IDS = ['#','A', 'B', 'C', 'D', 'E']
# TRUCK_IDS = ['O','P','Q','R','S','T','U']

class Vehicle():
    def __init__(self, id, x, y, orientation, length):
        self.id = id
        self.x = x
        self.y = y
        self.orientation = orientation
        self.length = int(length)

    def __repr__(self):
        return True

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

    def __hash__(self):
        return hash(self.__repr__())

    def __repr__(self):
        self.printableboard = '\n\n'.join(['      '.join(['{}'.format(item) for item in row]) for row in self.board])
        return self.printableboard

    def __eq__(self, other):
        return repr(self) == repr(other)

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


def uploadBoard(filepath):
    vehicles = []
    with open(filepath, 'r') as csvboard:
        boardreader = csv.DictReader(csvboard)
        for row in boardreader:
            vehicles.append(Vehicle(row['id'], row['x'], row['y'], row['orientation'], row['length']))

    return vehicles

def randomSolver(gameboard):

    runtimes = open('runtime.csv', 'w')
    runwriter = csv.writer(runtimes)
    for i in range(5000):
        print (i)
        newgameboard = copy.copy(gameboard)
        j=0
        while True:
            newgameboard = Gameboard(random.choice(newgameboard.checkformoves()))
            j += 1
            if newgameboard.hasSolved():
                runwriter.writerow([j])
                break



def breadth_First_Search(gameboard):
    newgameboard = copy.copy(gameboard)
    boardsQueue = queue.Queue()
    visited = set()
    boardsQueue.put(newgameboard)
    visited.add(gameboard)
    while boardsQueue.qsize() != 0 :
        new_board = boardsQueue.get()
        childList = new_board.checkformoves()

        for child in childList:
            newgameboard = Gameboard(child)
            if newgameboard.hasSolved():
                return  print(newgameboard)
            if newgameboard in visited:
                continue
            else:
                boardsQueue.put(newgameboard)
                visited.add(newgameboard)


p = Gameboard(uploadBoard("Boards/game2.csv"))
randomSolver(p)
