import sys
# from python import RED
# import numpy as np


def main():
#GRID = 6

# Create a grid
    width, height = 6, 6;
    #Matrix = [["X" for x in range(width)] for y in range(height)]
    a = 2
    b = 1
    c = 2
    grid_x=[]
    red = ""

    def RED():
        grid_x[a][b:(b+2)] = ['#', '#']
        red = grid_x[a][b:(b+2)]
        print (grid_x[a][b:c])


    def moveLeft():
        grid_x[a][b:(c+1)] = ['x', 'x']
        grid_x[a][(b+1):(c+2)] = ['#', '#']

    def hasWon():
        if red == grid_x[2][4:5]:
            print("you have won")

    grid_x = [["x" for x in range(6)]for y in range(6)]
    # for x in range(height):
    #     grid_y=[]
    #     for y in range (width):
    #         #
    #         grid_y.append(' ')
    #     grid_x.append(grid_y)

    RED()

    moveLeft()
    moveLeft()
    moveLeft()
    print(grid_x)
    hasWon()



    print(grid_x)

    #print(RED.position_x_R)


    # for i in range(height):
    #     for j in range (width):
    #         print("  ", end='')
    #         print(grid_x[i][j], end='')
    #         print("  ", end='')
    #     print('\n')

if __name__ == "__main__":
    main()
