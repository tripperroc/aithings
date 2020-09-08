import tkinter as tk
import time 
import json
import tkinter
import time
import argparse
import copy
import pandas as pd
import asteroids_exp
import pdb

class Agent:

	def __init__(self):
		self.args = asteroids_exp.parse_args()
		self.args['visual'] = True
		self.state, self.window_width, self.window_height  = asteroids_exp.init_asteroid_model(self.args)
		self.view = None

	def act(self,state,direction,time):
		#pdb.set_trace()
		xv, yv = self.get_move(direction)
		state = asteroids_exp.move(state, xv, yv, time, self.window_width, self.window_height, self.args, lambda x: asteroids_exp.render(self.view, x))
		return state

	def get_move(self,key):
		return asteroids_exp.MOVES[key]

class Async_Agent(Agent):

	def __init__(self):
		super().__init__()
		self.view = asteroids_exp.init_asteroid_view(self.state, self.window_width, self.window_height)
		self.current_dir = 's'
		self.view.window.bind('<KeyPress>', self.down)
		self.run()
		tk.mainloop()


	def down(self, e):
	    """Handle down key stroke"""

	    self.current_dir = e.char

	def run(self):
		self.state = self.act(self.state,self.current_dir, 1)
		self.view.window.after(100,self.run)



agent = Async_Agent()




	   
