import sys
import numpy as np
import csv
import random
import copy
import time
import queue
from RushClass import Gameboard, Vehicle
from collections import deque

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
    start_time = time.time()
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
                elapsed_time = time.time() - start_time
                print("Solved the puzzle in: {}".format(elapsed_time))
                return  print(newgameboard)
            if newgameboard in visited:
                continue
            else:
                Stack.append(newgameboard)
                visited.add(newgameboard)

def breadth_First_Search(gameboard):
    # get current time
    start_time = time.time()

    # initialize
    boardsQueue = deque()
    visited = set()

    # put intial gameboard and empty tuple in queue
    boardsQueue.appendleft((gameboard, tuple()))

    # add initial gameboard to archive
    visited.add(gameboard)
    while len(boardsQueue) != 0 :
        # pop new board and path
        new_board, new_boardPath = boardsQueue.pop()

        # append path with new board
        new_boardPath = new_boardPath + tuple([new_board])

        # if board is not yet in visited, add it
        if new_board in visited:
            pass
        else:
            visited.add(new_board)

        # if board is solved, run backtraceV2
        if new_board.hasSolved():
            print ("found board")
            return {"path": new_boardPath,"solvetime": time.time() - start_time}

        # else add all possible boards to queue, if theyre not in visited
        else:
            for move in new_board.checkformoves():
                newgameboard = Gameboard(move)
                if newgameboard in visited:
                    pass
                else:
                    game = Gameboard(move)
                    visited.add(game)
                    pair = (game, new_boardPath)
                    boardsQueue.appendleft(pair)


def backtrace(solutions, boardnumbers, beginposition, solution):
    numberofsteps = 0
    path = [boardnumbers[solution]]
    while path[-1]  !=  0:
        path.append(solutions[path[-1]])
        numberofsteps += 1
    path.reverse()
    return path, numberofsteps

def  backtraceV2(path):
    for board in path:
        print(board)
