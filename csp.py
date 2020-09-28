"""
Read two input arguments: the size of the board (as n) and the 
number of rooks and bishops each (as k) [5 points]
"""

# Create an object for each variable. [5 points]

"""
Each variable object must have as an attribute (called known_values) a set containing 
all of the possible values in the domain when the object is 
initialized [5 points]
"""

# Variable object should also have a boolean variable called assigned [5 points]

# Implement basic backtracking algorithm [35 points]

"""
At every level of the search tree: iterate over each constraint with
which the variable assigned at that level shares a constraint
(these may be hard-coded, but you should indicate where via a comment 
where you check the constraints) and use the known_values attributes to perform 
forward checking. [10 points]
"""

# Add minimum remaining values heuristic [10 points]

# Add least constraining values heuristic [10 points]

# Add an arc consistency heuristic [5 points]

"""
Output your solution into a file called "csp_n_k.csv," a csv file 
where n and k are the input arguments, and the headers are "name" and "value."
There should be one line per variable. You can name your variables 
however you like, but the convention should be obvious to the grader.
5 points per output file.
"""

