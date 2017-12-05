![alt text](http://heuristieken.nl/wiki/images/d/df/Rushhour.jpg)

Rush Hour is a puzzle game on a 6x6 board where you have to move the red car to the exit. Other vehicles of length 2 or 3 block the way. It is only allowed to move the vehicles in their driving position, turning is not possible.  

With the Rush Hour project we implemented the board and wrote a code with three different algorithms to solve the game as fast as possible.  

RushHour.py is the main file where the user can choose the boardsize and the game and where the code is run.  

RushClass.py consist of two classes; the vehicle class gives information about the vehicles and the gameboard class fills the board, checks for possible moves and checks if the game is won.  

Algorithms.py contains three algorithms to solve the game: a random solver, a bread first search algorithm and a depth first search algorithm.  

# Update RushHour 23rd of november  

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
