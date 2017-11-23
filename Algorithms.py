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



def breadth_First_Search(gameboard):
    newgameboard = copy.copy(gameboard)
    boardsQueue = queue.Queue()
    visited = set()
    boardsQueue.put(newgameboard)
    visited.add(gameboard)
    while boardsQueue.qsize() != 0 :
        new_board = boardsQueue.get()
        childList = new_board.checkformoves()

        for child in childList:
            newgameboard = Gameboard(child)
            if newgameboard.hasSolved():
                return  print(newgameboard)
            if newgameboard in visited:
                continue
            else:
                boardsQueue.put(newgameboard)
                visited.add(newgameboard)
