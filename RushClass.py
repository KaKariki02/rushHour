from math import ceil
import matplotlib.pyplot as plt
import copy

# Class Vehicle with properties for id, x-coordinate, y-coordinate, vertical or
# horizontal orientation and the length of the vehicle
class Vehicle():
    def __init__(self, id, x, y, orientation, length):
        self.id = id
        self.x = x
        self.y = y
        self.orientation = orientation
        self.length = int(length)

    def __repr__(self):
        return "'{0}{1}{2}{3}'".format(self.id, self.x, self.y, self.orientation)

    def __hash__(self):
        return hash(self.__repr__())

    def __eq__(self, other):
        return hash(self) == hash(other)

class Dimensions():
    def init():
        global width
        global height

class Gameboard():
#GRID = 6

    def __init__(self, vehicles):

        self.width = Dimensions.width
        self.height = Dimensions.height

        # Fill the board with dots
        self.board = [["." for x in range(self.width)] for y in range(self.height)]
        self.vehicles = vehicles

        # Place vehicles on the board
        for vehicle in self.vehicles:
            if vehicle.orientation == 'H':
                for i in range(vehicle.length):
                    self.board[int(vehicle.y)][int(vehicle.x)+i] = vehicle.id
            if vehicle.orientation == 'V':
                for i in range(vehicle.length):
                    self.board[int(vehicle.y)+i][int(vehicle.x)] = vehicle.id

    # hash the gameboardstring
    def __hash__(self):
        return hash(self.__repr__())

    def plot(self):
        plotboard = copy.copy(self.board)
        number = 1
        for i in range(self.width):
            for j in range(self.width):
                if (plotboard[i][j] == "."):
                    plotboard[i][j] = 0
                else:
                    plotboard[i][j] = ord(plotboard[i][j]) * 10
                    number += 1
        plt.matshow(plotboard)
        plt.show()

    # represents the gameboardobject as a string
    def __repr__(self):
        self.printableboard = '\n\n'.join(['      '.join(['{}'.format(item) for item in row]) for row in self.board])
        return self.printableboard

    # compare two hashed gameboards
    def __eq__(self, other):
        return hash(self) == hash(other)

    # check if vehicle is oriented horizontal or vertical and if it's not on the edge of the board
    # move if not blocked by another vehicle
    def checkformoves(self):
        possibleBoards = []
        for vehicle in self.vehicles:
            x_position = int(vehicle.x)
            y_position = int(vehicle.y)

            if vehicle.orientation == 'H':
                if x_position != 0:
                    if self.board[y_position][x_position - 1] == '.':
                        newVehicles = self.vehicles.copy()
                        newVehicle = Vehicle(vehicle.id, x_position - 1, y_position, vehicle.orientation, vehicle.length)
                        newVehicles.remove(vehicle)
                        newVehicles.append(newVehicle)
                        possibleBoards.append(newVehicles)
                if (x_position + vehicle.length - 1) != self.width - 1:
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
                if y_position + (vehicle.length - 1) != self.height - 1:
                    if self.board[y_position + vehicle.length][x_position] == '.':
                        newVehicles = self.vehicles.copy()
                        newVehicle = Vehicle(vehicle.id, x_position, y_position + 1, vehicle.orientation, vehicle.length)
                        newVehicles.remove(vehicle)
                        newVehicles.append(newVehicle)
                        possibleBoards.append(newVehicles)

        return possibleBoards

    # check if the red car is at the winning position
    def hasSolved(self):
        for vehicle in self.vehicles:
            winning_x = Dimensions.width - 2
            winning_y = ceil(Dimensions.height / 2) - 1
            if vehicle.id == '#' and vehicle.x == winning_x and vehicle.y == winning_y and vehicle.orientation == "H":
                return True

        return False
