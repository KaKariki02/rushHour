Random_dist.jpg
<img src=https://github.com/KaKariki02/rushHour/blob/master/Results/Random_dist.jpg width="800">  
The random solver randomly moves one car and continues with that board. It repeats this process untill it finds the solution. This figure shows a histogram of the distribution of steps it takes to solve a board. Interestingly, most boards are solved in a short time indicating that not many steps were needed, but some runs take more than 10 times the amount of time to solve the board. 

Results_table.jpg
<img src=https://github.com/KaKariki02/rushHour/blob/master/Results/Results_table.jpg width="800">

The results of the breadth first search and the depth first search show that the the first algorithm always finds the solution in less steps than the dept first search. It has to move the cars less number of times to get the red car to the exit. This is because the breadth first search algorithm first checks all the children of every node and then continues to the next 'generation' of children. However the depth first search is faster if you take a look at the total number of nodes it needs to make. It only checks one child of a node and continues with that child and so it continues. It doesn't check all the children of one node, causing a faster way to find a path to the solution.
The difference between the two algorithms is more or less equal for every gameboard.

We have tried to replace the red car to the bottom of the csv file. In that way the check for move function will check if the red can be moved after it has checked it for all the other cars. This will only happen the first time, when the check for move function checks for possible moves on the starting position of the game. The board where the red car is moved will get at the bottom of the stack with the depth first search algorithm and at the end of the queue with the breadth first search algorithm. Because this only applies for the first time, it doesn't result in a big difference.  
For example: game 1  
Breadth first search:  
* Red car on top of the csv file:  
  83 steps to the solution,
  8678 nodes 
* Red car at the bottom of the csv file:  
  steps to the solution, 
  8678 nodes  
  
Depth first search:  
* Red car at the top:  
  1764 steps to the solution, 
  4106 nodes 
* Red car at the bottom:  
  1761 steps to the solution, 
  4110 nodes 
  
## Considering the state-space
Calculating the state-space in our case isn't very straightforward. We could define the state-space as all the possible configurations of the gameboard. Since every vehicle is restricted to moving in one axis, we can consider that a single car (length = 2) has 5 possible positions and a truck (length = 3) has 4 possible positions. If we allow vehicles to overlap, we can calculate the state-space for a board with three cars and one truck: 5 * 5 * 5 * 4 = 500 configurations, since every car has 5 possible positions and every truck has 4. A formula for calcutation the state-space would be:
![](http://latex.codecogs.com/gif.latex?5%5E%7Bnumber%20of%20cars%7D%20*%204%5E%7Bnumberoftrucks%7D%20%3D%20statespace)  
This formula assumes that the height and width of the board are both six. We can also write a formula in which height and width are variables (since the boards are all square and height and width are equal, we only use the width of the board):
![](http://latex.codecogs.com/gif.latex?%28width-1%29%5E%7Bnumber%20of%20cars%7D%20*%20%28width-2%29%5E%7Bnumberoftrucks%7D%20%3D%20statespace)  
Using this formula we can calculate the state-space for every board:
* Game 1 = 1.000.000
* Game 2 = 976.562.500
* Game 3 = 976.562.500
* Game 4 = 1,94E19
* Game 5 = 2,12E21
* Game 6 = 1,04E23
* Game 7 = 1,44E45

Even though these are extremely high numbers, they do not have much practical significance. This is because our algoritms do not consider boards where vehicles overlap. This constriction would drastically decrease the state-space of every game. It is also possible that a board with no overlapping vehicles could still not be reached from the starting position, so this board would be a possibility in the practical state space.
