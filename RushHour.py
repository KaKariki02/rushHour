#move check

import sys
import numpy as np
import csv
import random
import copy
import time
import queue
from RushClass import Gameboard, Vehicle
from Algorithms import breadth_First_Search, randomSolver

def uploadBoard(filepath):
    vehicles = []
    with open(filepath, 'r') as csvboard:
        boardreader = csv.DictReader(csvboard)
        for row in boardreader:
            vehicles.append(Vehicle(row['id'], row['x'], row['y'], row['orientation'], row['length']))

    return vehicles


if __name__ == "__main__":
    p = Gameboard(uploadBoard("Boards/game2.csv"))
    randomSolver(p)
