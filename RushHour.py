import sys
import numpy as np
import csv
import random
import copy
import time
import queue
from RushClass import Gameboard, Vehicle
from Algorithms import breadth_First_Search, randomSolver
import os
import dimensions

def uploadBoard(filepath):
    vehicles = []
    with open(filepath, 'r') as csvboard:
        boardreader = csv.reader(csvboard)
        next(boardreader)
        for row in boardreader:
            id, x, y, orientation, length = row
            vehicles.append(Vehicle(id, x, y, orientation, length))

    return vehicles


if __name__ == "__main__":
    dimensions.init()
    boardsize = input("What board size would you like to solve?\n 1. 6x6\n 2. 9x9 \n 3. 12x12\n")
    path = "Boards/"
    if (boardsize == "1" or boardsize =="6x6"):
        path = path + "6x6/"
        dimensions.width = 6
        dimensions.height = 6
        print("These 6x6 boards are available:")
        for item in os.listdir(path):
            print (item)
        path = path + input("Which board would you like to solve?")
        breadth_First_Search(Gameboard(uploadBoard(path)))
    if (boardsize == "2" or boardsize == "9x9"):
        path = path + "9x9/"
        dimensions.width = 9
        dimensions.height = 9
        print("These 9x9 boards are available:")
        for item in os.listdir(path):
            print (item)
        path = path + input("Which board would you like to solve?")
        breadth_First_Search(Gameboard(uploadBoard(path)))
    if (boardsize == "3" or boardsize == "12x12"):
        path = path + "12x12/"
        for item in os.listdir(path):
            print (item)
        width, height = 12, 12
