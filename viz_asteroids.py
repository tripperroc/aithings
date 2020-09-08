from matplotlib import pyplot as plt                                    
import numpy as np
import asteroids_exp
from asteroids_exp import State
import copy
from getkey import getkey
from mpl_toolkits.mplot3d import Axes3D 
import argparse

def parse_args():
    """Parse all command line arguments."""

    ap = argparse.ArgumentParser()

    # Add the arguments to the parser
    ap.add_argument("-g", "--in", required=True,
       help="Name of input file")
    args = vars(ap.parse_args())
    return args

TIME = 0
def render(state):
	"""Draw time-unwound 3D view of meteor field"""

	global TIME
	for a in state.asteroids:
		plot_extrude(a.x-a.s/2,a.x+a.s/2, 0, a.y-a.s/2, a.y+a.s/2, 0, TIME,1,"blue")
	TIME += 1

def plot_extrude(x1,x2,dx,y1,y2,dy,z,dz,color):
	"""Draw a time-unwound asteroid"""
	X = [[x1 if j < 2 else x2 for j in range(4)] for i in range(4)]
	X[1][1] = X[2][1] = x1 + dx
	X[1][2] = X[2][2] = x2 + dx
	np.array(X)
	Y = [[y1 if i < 2 else y2 for j in range(4)] for i in range(4)]
	Y[1][1] = Y[1][2] = y1 + dy
	Y[2][1] = Y[2][2] = y2 + dy
	np.array(Y)
	Z = np.array([[z if {i,j} - {1,2} else z+dz for j in range(4)] for i in range(4)])
	ax.plot_surface(X, Y, Z, color=color)


"""We don't have a main program here because we are using ipython"""
args = {}
args["in"] = "asteroid_game_2.json"
args["visual"] = True
initial_state, width, height = asteroids_exp.init_asteroid_model(args)
fig = plt.figure() 
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim3d(0, 200)
ax.set_ylim3d(0,200)
ax.set_zlim3d(0, 200)
state = copy.deepcopy(initial_state)
moves = [('e',40),('s',15),('d',20),('c',100)]
X = np.array([[0,width],[0,width]])
Y = np.array([[0,0],[height,height]])
Z = np.array([[-.1,-.1],[-.1,-.1]])
#ax.plot_surface(X, Y, Z, color="grey")

print(state.goal)




