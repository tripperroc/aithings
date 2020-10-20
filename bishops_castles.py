import sys
import pandas as pd
import itertools

class Variable:
	def __init__(self, n, name):
		self.domain = set(itertools.product(range(n),range(n)))
		self.name = name

class Rook(Variable):
	pass

class Bishop(Variable):
	pass



