import tkinter as tk
import time 
import json
import tkinter
import time
import argparse
import random
import copy
import math
import pandas as pd
import asteroids_exp
import pdb


class SA_Agent():

	def __init__(self):
		"""initialize environment and intial solution"""
		self.args = asteroids_exp.parse_args()
		self.args['visual'] = True
		self.env_state, self.window_width, self.window_height  = asteroids_exp.init_asteroid_model(self.args)
		self.view = None
		
		# finish this method (10 points)


		"""simulate a solution, return a reward value (10 points) """

		"""choose a new random solution, via a local edit of current solution (10 points) """

		"""determine whether to move to new state or remain in same place (10 points) """

a = SA_Agent()
"""run high-level simulated annealing algorithm (30 points)"""

""" a.solution should be a list of ordered pairs of (directions, steps),
	just as in the asteroid_tree.py from hw4 
"""
df = pd.DataFrame(a.solution, columns=['direction','time'])
df.to_csv((".").join([a.args['in'].split(".")[0],"csv"]),index = False)
