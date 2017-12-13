# Rush Hour Solver

![alt text](http://heuristieken.nl/wiki/images/d/df/Rushhour.jpg)

The game Rush Hour is a puzzle on a 6x6 board where you have to move the red car to the exit. Other vehicles of length 2 or 3 block the way. It is only allowed to move the vehicles in their driving position, turning is not possible. Rush Hour Solver solves boards of size 6x6, 9x9 and 12x12 as fast as possible with three different algorithms; a Random Solver, a Breadth First Search and Depth First Search. Rush Hour Solver contains the following games:  

6x6: game 1, game 2, game 3  
<img src="http://heuristieken.nl/wiki/images/9/95/Rushhour6x6_1.jpg" width="150" />
<img src="http://heuristieken.nl/wiki/images/a/aa/Rushhour6x6_2.jpg" width="150" />
<img src="http://heuristieken.nl/wiki/images/c/c7/Rushhour6x6_3.jpg" width="150" />

9x9: game 4, game 5, game 6  
<img src="http://heuristieken.nl/wiki/images/9/96/Rushhour9x9_1.jpg" width="200" />
<img src="http://heuristieken.nl/wiki/images/1/1e/Rushhour9x9_2.jpg" width="200" />
<img src="http://heuristieken.nl/wiki/images/9/95/Rushhour9x9_3.jpg" width="200" />

12x12: game 7  
<img src="http://heuristieken.nl/wiki/images/2/26/Rushhour12x12_1.jpg" width="250" />

RushHour.py is the main file where the user can choose the boardsize and the game and where the code is run.  

RushClass.py consist of two classes; the vehicle class gives information about the vehicles and the gameboard class fills the board, checks for possible moves and checks if the game is won.  

Algorithms.py contains three algorithms to solve the game: a random solver, a bread first search algorithm and a depth first search algorithm.  

## Getting Started  

Roush Hour Solver let the user choose the board size and the game to solve. Then the user can decide what Algorithm will be used. When the game is solved the user can see the time it took, the number of nodes the Algorithm made, the number of steps to come to the solution and the moves that the cars have to make.  

### Run the program  

To use Rush Hour Solver it is necessary to have python 3 installed. You can run the program by entering python followed by the name of the RushHour document:  
```
$ python RushHour.py
```
When you are prompted to choose the board size, enter for example '1' or '6x6':  
What board size would you like to solve?
 1. 6x6  
 2. 9x9  
 3. 12x12  
 ```
 6x6
 ```  
When you are prompted to choose the game, type in the filename of the game:  
These 6x6 boards are available:
GameWon.csv
HardestGame.csv
game1.csv
game3.csv
game2.csv
Which board would you like to solve?  
```
game3.csv
```  
When you are prompted to choose the algorithm, enter for example '2' or 'breadth first search':  
Which algorithm would you like to use?
 1. Random Solver
 2. Breadth First Search
 3. Depth First Search  
 ```
 breadth first search
 ```  
 This will give the following results:
 ```
 Time: 0.17185306549072266
Nodes: 348
Length solution: 17
['A naar beneden', 'B naar beneden', 'C naar beneden', 'D naar beneden', 'A naar bened
en', 'B naar beneden', 'C naar beneden', 'D naar beneden', 'A naar beneden', '# naar r
echts', 'B naar beneden', 'C naar beneden', 'D naar beneden', '# naar rechts', '# naar
 rechts', '# naar rechts']
 ```  
 
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
