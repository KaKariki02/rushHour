class RED(object):
    """docstring for RED.
    following properties: Put on board, Move left, Move right

    """
    def __init__(self):
        super(RED, self).__init__()
        self.position_x_R = 2
        self.position_y_R = 1,2
        self.symbol_R = '#'

    def putOnBoard(self, position):


    def moveLeft(self, position):
        while True:
            try:
                print ('give a x and y coordinate for WHITE KING')
                destination_x_R = int(input())
                destination_y_R = int(input())

    def moveRight(self, position):    
