import sys
import numpy as np
import csv
import random
import copy
import time
import queue
from RushClass import Gameboard, Vehicle
from Algorithms2 import breadth_First_Search, randomSolver, depth_First_Search
import os
import dimensions

# Get vehicles from csv file and return as vehicle class
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
<<<<<<< HEAD
    # let user choose the boardsize, the game and the algorithm
    # load game in gameboard class and solve with the chosen algorithm
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
        path = path + input("Which board would you like to solve?\n")

    if (boardsize == "2" or boardsize == "9x9"):
        path = path + "9x9/"
        dimensions.width = 9
        dimensions.height = 9
        print("These 9x9 boards are available:")
        for item in os.listdir(path):
            print (item)
        path = path + input("Which board would you like to solve?\n")

    if (boardsize == "3" or boardsize == "12x12"):
        path = path + "12x12/"
        for item in os.listdir(path):
            print (item)
        dimensions.width = 12
        dimensions.height = 12
        path = path + "game7.csv"


    algorithm = input("Which algorithm would you like to use?\n 1. Random Solver\n 2. Breadth First Search\n 3. Depth First Search\n")
    if (algorithm == "1" or algorithm.lower() == "random solver"):
        randomSolver(Gameboard(uploadBoard(path)))
    if (algorithm == "2" or algorithm.lower() == "breadth first search"):
        breadth_First_Search(Gameboard(uploadBoard(path)))
    if (algorithm == "3" or algorithm.lower() == "depth first search"):
        depth_First_Search(Gameboard(uploadBoard(path)))
=======
<<<<<<< HEAD
    # dimensions.init()
    # boardsize = input("What board size would you like to solve?\n 1. 6x6\n 2. 9x9 \n 3. 12x12\n")
    # path = "Boards/"
    # if (boardsize == "1" or boardsize =="6x6"):
    #     path = path + "6x6/"
    #     dimensions.width = 6
    #     dimensions.height = 6
    #     print("These 6x6 boards are available:")
    #     for item in os.listdir(path):
    #         print (item)
    #     path = path + input("Which board would you like to solve?")
    #     breadth_First_Search(Gameboard(uploadBoard(path)))
    # if (boardsize == "2" or boardsize == "9x9"):
    #     path = path + "9x9/"
    #     dimensions.width = 9
    #     dimensions.height = 9
    #     print("These 9x9 boards are available:")
    #     for item in os.listdir(path):
    #         print (item)
    #     path = path + input("Which board would you like to solve?")
    #     depth_First_Search(Gameboard(uploadBoard(path)))
    # if (boardsize == "3" or boardsize == "12x12"):
    #     path = path + "12x12/"
    #     for item in os.listdir(path):
    #         print (item)
    #     width, height = 12, 12
=======
    # let user choose boardsize and the game
    # load game in gameboard class and solve with depth first search algorithm
>>>>>>> 4a2df917c2d1e2437508a483d232300c2e1e0e0e
    dimensions.init()
    dimensions.height = 6
    dimensions.width = 6
    p = Gameboard(uploadBoard("Boards/6x6/game2.csv"))
    print(p.vehicles)
    q = Gameboard(uploadBoard("Boards/6x6/game2.csv"))
    q= Gameboard(random.choice(q.checkformoves()))
    print(q.vehicles)
    v1 = list(p.vehicles)
    v2 = list(q.vehicles)
    v_origineel = list(set(v1) - set(v2))[0]
    v_nieuw = list(set(v2) - set(v1))[0]
    if v_origineel.x < v_nieuw.x:
        print("naar rechts")
>>>>>>> 7de90d29cf23d790cc4435036acf6bdcd14378d2
