import sys
import csv
import random
import copy
import time
import queue
from RushClass import Gameboard, Vehicle, Dimensions
from RushHelpers import backtrace, backtraceV2
from Algorithms import randomSolver, breadth_First_Search_without, depth_First_Search_without
import os

# Get vehicles from csv file and return as vehicle class
def uploadBoard(filepath):
    vehicles = []
    with open(filepath, 'r') as csvboard:
        boardreader = csv.reader(csvboard)
        next(boardreader)
        for row in boardreader:
            id, x, y, orientation, length = row
            vehicles.append(Vehicle(id, int(x), int(y), orientation, length))

    return vehicles



if __name__ == "__main__":
    # let user choose the boardsize and the game
    Dimensions.init()
    boardsize = input("What board size would you like to solve?\n 1. 6x6\n 2. 9x9 \n 3. 12x12\n")
    path = "Boards/"

    if (boardsize == "1" or boardsize =="6x6"):
        path = path + "6x6/"
        Dimensions.width = 6
        Dimensions.height = 6
        print("These 6x6 boards are available:")
        for item in os.listdir(path):
            print (item)
        path = path + input("Which board would you like to solve?\n")

    if (boardsize == "2" or boardsize == "9x9"):
        path = path + "9x9/"
        Dimensions.width = 9
        Dimensions.height = 9
        print("These 9x9 boards are available:")
        for item in os.listdir(path):
            print (item)
        path = path + input("Which board would you like to solve?\n")

    if (boardsize == "3" or boardsize == "12x12"):
        path = path + "12x12/"
        for item in os.listdir(path):
            print (item)
        Dimensions.width = 12
        Dimensions.height = 12
        path = path + "game7.csv"

    # let user choose the algorithm, load game in gameboard class and print results
    algorithm = input("Which algorithm would you like to use?\n 1. Random Solver\n 2. Breadth First Search\n 3. Depth First Search\n")
    if (algorithm == "1" or algorithm.lower() == "random solver"):
        results = randomSolver(Gameboard(uploadBoard(path)))
        print(results["solvetime"])
        print(results["steps"])
    if (algorithm == "2" or algorithm.lower() == "breadth first search"):
        game = Gameboard(uploadBoard(path))
        results = breadth_First_Search_without(game)
        print("Time: " + str(results["solvetime"]))
        print("Nodes: " + str(results["nodes_popped"]))
        path = backtrace(results["archive"], results["solution"])
<<<<<<< HEAD
        visualize(path)
=======
>>>>>>> 972ca3ebcb512be6539e2a834e6dcd861fb4d2ac
        print("Length solution: " + str(len(path)))
        print(backtraceV2(path))
    if (algorithm == "3" or algorithm.lower() == "depth first search"):
        game = Gameboard(uploadBoard(path))
        results = depth_First_Search_without(game)
        print("Time: " + str(results["solvetime"]))
        print("Nodes: " + str(results["nodes"]))
        path = backtrace(results["archive"], results["solution"])
        print("Length solution: " + str(len(path)))
        print(backtraceV2(path))
