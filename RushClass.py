import dimensions
from math import ceil

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

        self.width = dimensions.width
        self.height = dimensions.height

        self.board = [["." for x in range(self.width)] for y in range(self.height)]
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
        return hash(self) == hash(other)

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

    def hasSolved(self):
        for vehicle in self.vehicles:
            winning_x = dimensions.width - 2
            winning_y = ceil(dimensions.height / 2) - 1
            if vehicle.id == '#' and vehicle.x == winning_x and vehicle.y == winning_y and vehicle.orientation == "H":
                return True

        return False

    def printPossibilities(self):
        for board in Gameboard.checkformoves(self):
            for vehicle in board:
                print(vehicle.id, vehicle.x, vehicle.y, vehicle.orientation)
