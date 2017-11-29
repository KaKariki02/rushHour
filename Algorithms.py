import sys
import numpy as np
import csv
import random
import copy
import time
import queue
from RushClass import Gameboard, Vehicle

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

def depth_First_Search(gameboard):
    beginposition = copy.copy(gameboard)
    Stack = []
    visited = set()
    boardnumbers = {}
    solutions = {}
    number = 0
    Stack.append(beginposition)
    visited.add(beginposition)
    boardnumbers[beginposition] = number
    number += 1
    # Stack.pop() if no value give between brackets, item at end of the list is returned
    while len(Stack) != 0 :
        new_board = Stack.pop()
        childList = new_board.checkformoves()

        for child in childList:
            newgameboard = Gameboard(child)
            boardnumbers[newgameboard] = number
            number += 1
            solutions[boardnumbers[newgameboard]] = boardnumbers[new_board]
            if newgameboard.hasSolved():
                solution = newgameboard
                print(backtrace(solutions, boardnumbers, beginposition, solution));
                return  print(newgameboard)
            if newgameboard in visited:
                continue
            else:
                Stack.append(newgameboard)
                visited.add(newgameboard)

def breadth_First_Search(gameboard):
    beginposition = copy.copy(gameboard)
    boardsQueue = queue.Queue()
    visited = set()
    boardnumbers = {}
    solutions = {}
    number = 0
    boardsQueue.put(beginposition)
    visited.add(beginposition)
    boardnumbers[beginposition] = number
    number += 1
    while boardsQueue.qsize() != 0 :
        new_board = boardsQueue.get()
        childList = new_board.checkformoves()
        for child in childList:
            newgameboard = Gameboard(child)
            boardnumbers[newgameboard] = number
            number += 1
            solutions[boardnumbers[newgameboard]] = boardnumbers[new_board]
            if newgameboard.hasSolved():
                solution = newgameboard
                print(backtrace(solutions, boardnumbers, beginposition, solution));
                return  print(newgameboard)
            if newgameboard in visited:
                continue
            else:
                boardsQueue.put(newgameboard)
                visited.add(newgameboard)

def backtrace(solutions, boardnumbers, beginposition, solution):
    numberofsteps = 0
    path = [boardnumbers[solution]]
    while path[-1] != 0:
        path.append(solutions[path[-1]])
        numberofsteps += 1
    path.reverse()
    return path, numberofsteps
