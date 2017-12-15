import sys
import csv
import random
import copy
import time
import queue
from RushClass import Gameboard, Vehicle
from collections import deque

def randomSolver(gameboard):
    start_time = time.time()
    newgameboard = gameboard
    steps=0
    while True:
        newgameboard = Gameboard(random.choice(newgameboard.checkformoves()))
        steps += 1
        if newgameboard.hasSolved():
            return {"solvetime": time.time() - start_time, "steps": steps}

def depth_First_Search_without(gameboard):
    start_time = time.time()
    Stack = []
    number = 0
    archive = {}
    archive[gameboard] = 0
    Stack.append(gameboard)
    # Stack.pop() if no value give between brackets, item at end of the list is returned
    while len(Stack) != 0 :
        # pop new board and path
        new_board = Stack.pop()

        number += 1

        # if board is solved, run backtraceV2
        if new_board.hasSolved():
            print ("found board")
            return {"solvetime": time.time() - start_time, "nodes": number, "archive": archive, "solution": new_board }

        # else add all possible boards to queue, if theyre not in visited
        else:
            for move in new_board.checkformoves():
                newgameboard = Gameboard(move)
                if newgameboard in archive:
                    pass
                else:
                    archive[newgameboard] = new_board
                    Stack.append(newgameboard)

def breadth_First_Search_without(gameboard):
    # get current time
    start_time = time.time()
    archive = {}
    # initialize
    boardsQueue = deque()

    archive  = {}
    archive[gameboard] = 0
    number = 0

    # put intial gameboard and empty tuple in queue
    boardsQueue.appendleft(gameboard)

    # add initial gameboard to archive
    archive[gameboard] = 0
    while len(boardsQueue) != 0 :
        # pop new board and path
        new_board = boardsQueue.pop()

        number += 1
        # if board is solved, run backtraceV2
        if new_board.hasSolved():
            print ("found board")
            return {"solvetime": time.time() - start_time, "nodes_popped": number, "archive": archive, "solution": new_board}

        # else add all possible boards to queue, if theyre not in visited
        else:
            for move in new_board.checkformoves():
                newgameboard = Gameboard(move)
                if newgameboard in archive:
                    pass
                else:
                    boardsQueue.appendleft(newgameboard)
                    archive[newgameboard] = new_board
