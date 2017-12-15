Random_dist.jpg
<img src=https://github.com/KaKariki02/rushHour/blob/master/Results/Random_dist.jpg width="800">  
The random solver randomly moves one car and continues with that board. It repeats this process untill it finds the solution. This figure shows a histogram of the distribution of steps it takes to solve a board. Interestingly, most boards are solved in a short time indicating that not many steps were needed, but some runs take more than 10 times the amount of time to solve the board. 

Results_table.jpg
<img src=https://github.com/KaKariki02/rushHour/blob/master/Results/Results_table.jpg width="800">

The results of the breadth first search and the depth first search show that the the first algorithm always finds the solution in less steps than the dept first search. It has to move the cars less number of times to get the red car to the exit. This is because the breadth first search algorithm first checks all the children of every node and then continues to the next 'generation' of children. However the depth first search is faster if you take a look at the total number of nodes it needs to make. It only checks one child of a node and continues with that child and so it continues. It doesn't check all the children of one node, causing a faster way to find a path to the solution.
The difference between the two algorithms is more or less equal for every gameboard.

We have tried to replace the red car to the bottom of the csv file. In that way the check for move function will check if the red can be moved after it has checked it for all the other cars. This will only happen the first time, when the check for move function checks for possible moves on the starting position of the game. The board where the red car is moved will get at the bottom of the stack with the depth first search algorithm and at the end of the queue with the breadth first search algorithm. Because this only applies for the first time, it doesn't result in a big difference.  
For example:  
Game 1, breadth first search:  
* Red car on top of the csv file:  
  83 steps to the solution
  8678 nodes 
* Red car at the bottom of the csv file:  
  steps to the solution 
  8678 nodes    
Game 1, depth first search:  
* Red car at the top:
  1764 steps to the solution and 
  4106 nodes 
* Red car at the bottom:
  1761 steps to the solution and 
  4110 nodes 
