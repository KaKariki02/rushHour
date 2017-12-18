def backtrace(dictionary, solution):

    # initialize list for path to the solution
    path = [solution]

    # while the end of the list is not 0(initial board), append parent to list
    while path[-1]  !=  0:
        path.append(dictionary[path[-1]])

    # remove initial board from list
    path = path[:-1]
    # reverse list, so path is in right order
    path.reverse()

    return path

def  backtraceV2(path):
    # initialize list for moves
    moves = []
    # iterate over boards in paths
    for i in range(len(path) - 1) :
        # get current and next board
        board1 = path[i]
        board2 = path[i+1]
        
        # get original and new vehicle
        original = list(set(board1.vehicles) - set(board2.vehicles))[0]
        new = list(set(board2.vehicles) - set(board1.vehicles))[0]

        # check which way the vehicle was moved by comparing the x and y positions
        if original.x < new.x:
            moves.append("{0} to the right".format(original.id))
        if original.x > new.x:
            moves.append("{0} to the left".format(original.id))
        if original.y < new.y:
            moves.append("{0} down".format(original.id))
        if original.y > new.y:
            moves.append("{0} up".format(original.id))
    # return list of moves
    return moves
