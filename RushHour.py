import sys
#import numpy as np
import csv
import random
import copy
import time
import queue
from RushClass import Gameboard, Vehicle, Dimensions
from Algorithms import breadth_First_Search, randomSolver, depth_First_Search, backtrace, backtraceV2, breadth_First_Search_without, depth_First_Search_without
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
    # let user choose the boardsize, the game and the algorithm
    # load game in gameboard class and solve with the chosen algorithm
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


    algorithm = input("Which algorithm would you like to use?\n 1. Random Solver\n 2. Breadth First Search\n 3. Depth First Search\n")
    if (algorithm == "1" or algorithm.lower() == "random solver"):
        results = randomSolver(Gameboard(uploadBoard(path)))
        print(results["solvetime"])
        print(results["steps"])
    if (algorithm == "2" or algorithm.lower() == "breadth first search"):
        results = breadth_First_Search(Gameboard(uploadBoard(path)))
        print (backtraceV2(results["path"]))
        print(results["amount_steps"])
        print(results["solvetime"])
        print(results["nodes_popped"])
    if (algorithm == "3" or algorithm.lower() == "depth first search"):
        game = Gameboard(uploadBoard(path))
        print(game)
        results = depth_First_Search(game)
        print (backtraceV2(results["path"]))
        print(results["amount_steps"])
        print(results["solvetime"])
        print(results["nodes"])
        print(results["visited"])
    if (algorithm == "4" or algorithm.lower() == "breath first without"):
        game = Gameboard(uploadBoard(path))
        results = breadth_First_Search_without(game)
        print("Time: " + str(results["solvetime"]))
        print("Nodes: " + str(results["nodes_popped"]))
        path = backtrace(results["archive"], results["solution"])
        print("Length solution: " + str(len(path)))
        print(backtraceV2(path))
    if(algorithm  == "5"):
        game = Gameboard(uploadBoard(path))
        results = depth_First_Search_without(game)
        print("Time: " + str(results["solvetime"]))
        print("Nodes: " + str(results["nodes"]))
        path = backtrace(results["archive"], results["solution"])
        print("Length solution: " + str(len(path)))
        #print(backtraceV2(path))
