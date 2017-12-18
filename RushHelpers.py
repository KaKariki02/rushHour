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
