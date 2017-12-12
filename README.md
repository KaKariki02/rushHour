# Rush Hour Solver

![alt text](http://heuristieken.nl/wiki/images/d/df/Rushhour.jpg)

The game Rush Hour is a puzzle on a 6x6 board where you have to move the red car to the exit. Other vehicles of length 2 or 3 block the way. It is only allowed to move the vehicles in their driving position, turning is not possible.  

Rush Hour Solver solves boards of size 6x6, 9x9 and 12x12 with three different algorithms as fast as possible. Rush Hour Solver contains the following games:  

6x6: game 1, game 2, game 3  
![alt text](http://heuristieken.nl/wiki/images/9/95/Rushhour6x6_1.jpg){ width=50% } ![alt text](http://heuristieken.nl/wiki/images/a/aa/Rushhour6x6_2.jpg){ width=50% } ![alt text](http://heuristieken.nl/wiki/images/c/c7/Rushhour6x6_3.jpg){ width=50% }  

RushHour.py is the main file where the user can choose the boardsize and the game and where the code is run.  

RushClass.py consist of two classes; the vehicle class gives information about the vehicles and the gameboard class fills the board, checks for possible moves and checks if the game is won.  

Algorithms.py contains three algorithms to solve the game: a random solver, a bread first search algorithm and a depth first search algorithm.  

## Getting Started  


## Update RushHour 23rd of november  

We have created three files. Algorithms.py contains the algorithms, RushClass.py contains the classes and RushHour is the main file.  

## Done:  
-Initialisation of a board with a grid system  
-The car id, x position, y position, orientation and length get retrieved from a CSV file.  
-Printing of a empty board  
-Printing of a start board  
-The programme prints a list of possible moves    
-Implement a random board solver: `randomSolver`  
-Capturing the lists of possible moves  
-A "win function"  
-Implement a breadth first search  
-Comparison between a breadth first search with and without an archive

## Todo:  
-backtracing the solution  
-counting number of steps to solution  
-pruning  
-visualization of the board  
-make our code applicable for other board sizes  
-Comments in code  
-scorefunction boards/ priority queue  
-gitignore  
