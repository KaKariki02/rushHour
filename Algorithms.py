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


def depth_First_Search(gameboard):
    start_time = time.time()
    Stack = []
    number = 0
    visited = set()
    Stack.append((gameboard, tuple()))
    visited.add(gameboard)
    # Stack.pop() if no value give between brackets, item at end of the list is returned
    while len(Stack) != 0 :
        # pop new board and path
        new_board, new_boardPath = Stack.pop()

        number += 1

        # append path with new board
        new_boardPath = new_boardPath + tuple([new_board])

        # if board is not yet in visited, add it TODO
        if new_board in visited:
            pass
        else:
            visited.add(new_board)

        # if board is solved, run backtraceV2
        if new_board.hasSolved():
            print ("found board")
            return {"path": new_boardPath,"solvetime": time.time() - start_time,"nodes": number, "amount_steps": len(new_boardPath), "visited": len(visited)}

        # else add all possible boards to queue, if theyre not in visited
        else:
            for move in new_board.checkformoves():
                newgameboard = Gameboard(move)
                if newgameboard in visited:
                    pass
                else:
                    visited.add(newgameboard)
                    Stack.append((newgameboard, new_boardPath))

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


def breadth_First_Search(gameboard):
    # get current time
    start_time = time.time()

    # initialize
    boardsQueue = deque()
    visited = set()

    number = 0

    # put intial gameboard and empty tuple in queue
    boardsQueue.appendleft((gameboard, tuple()))

    # add initial gameboard to archive
    visited.add(gameboard)
    while len(boardsQueue) != 0 :
        # pop new board and path
        new_board, new_boardPath = boardsQueue.pop()

        number += 1

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
            return {"path": new_boardPath,"solvetime": time.time() - start_time, "nodes_popped": number, "amount_steps": len(new_boardPath)}

        # else add all possible boards to queue, if theyre not in visited
        else:
            for move in new_board.checkformoves():
                newgameboard = Gameboard(move)
                if newgameboard in visited:
                    pass
                else:
                    visited.add(newgameboard)
                    boardsQueue.appendleft((newgameboard, new_boardPath))


def backtrace(dictionary, solution):

    path = [solution]
    while path[-1]  !=  0:
        path.append(dictionary[path[-1]])

    path = path[:-1]
    path.reverse()
    return path

def  backtraceV2(path):
    moves = []
    for i in range(len(path) - 1) :
        board1 = path[i]
        board2 = path[i+1]
        original = list(set(board1.vehicles) - set(board2.vehicles))[0]
        nieuw = list(set(board2.vehicles) - set(board1.vehicles))[0]
        if original.x < nieuw.x:
            moves.append("{0} to the right".format(original.id))
        if original.x > nieuw.x:
            moves.append("{0} to the left".format(original.id))
        if original.y < nieuw.y:
            moves.append("{0} down".format(original.id))
        if original.y > nieuw.y:
            moves.append("{0} up".format(original.id))
    return moves

def visualize(path):
    for i in range(len(path)):
        path[i].plot()
