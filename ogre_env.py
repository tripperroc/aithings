import pdb
import copy 

class Gameboard:
	def __init__(self, w, h):
		self.width = w
		self.height = h


class Ogre:
	def __init__(self, size, gameboard):
		self.size = size
		self.gameboard = gameboard
		self.y = 0
		self.x = (gameboard.width-size)//2
		self.pieces = [[1 for i in range(size)] for j in range(size)]
		self.mass = size**2

	def move (self, x, y):
		""" should only move up or down one step"""
		self.x += x
		self.y += y

	def free (self):
		if self.y > self.gameboard.height - self.size:
			for i in range(self.size):
				for j in range(self.size):
					if self.y + j > self.gameboard.height and self.pieces[j][i] == 1:
						return True
		return False

	def num_pieces (self):
		counter = 0
		for row in self.pieces:
			counter += sum(row)

	def inbounds (self):
		if self.x < 0 or self.x > self.gameboard.width - self.size or self.y < 0:
			for i in range(self.size):
				for j in range(self.size):
					if (self.y + j < self.gameboard.height or self.x < 0 or self.x > self.gameboard.width) and self.pieces[j][i] == 1:
						return False
		return True
		
class Person:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.state = 1

class People:
	def __init__(self, count, gameboard):
		self.them = [Person(gameboard.width * i//count, gameboard.height-1) for i in range(count)]

	def dead(self):
		""" Return true if all people are dead
		"""
		for p in self.them:
			if p == 1:
				return False
		return True

	def bring_out_your_dead(self):
		newthem = []
		for p in self.them:
			if p.state == 1:
				newthem.append(p)
		self.them = newthem

class State:
	def __init__(self, gameboard, ogre, people):
		self.gameboard = gameboard
		self.ogre = ogre
		self.people = people

	def __str__(self, ):
		outstr = [[' '] * self.gameboard.width for i in range(self.gameboard.height)]
		for i in range(self.ogre.size):
			for j in range(self.ogre.size):
				if self.ogre.pieces[j][i] == 1:
					try:
						outstr[j+self.ogre.y][i+self.ogre.x] = 'O'
					except IndexError:
						pass
		for p in self.people.them:
			if p.state == 1:
				outstr[p.y][p.x] = 'f'
		outstr = ["".join(x) for x in outstr]
		outstr = "\n".join(outstr)
		return outstr

	def detect_collision(self):
		for p in self.people.them:
			if 0 <= p.x - self.ogre.x < self.ogre.size and 0 <= p.y - self.ogre.y < self.ogre.size:
					p.state = 0
					self.ogre.pieces[p.y - self.ogre.y][p.x - self.ogre.x] = 0


def the_max (state):
	max_val = -2
	print(state)
	for dx in [1,0,-1]:
		new_state = copy.deepcopy(state)
		new_state.ogre.x += dx
		new_state.ogre.y += 1
		new_state.detect_collision()
		new_state.people.bring_out_your_dead()
		if new_state.ogre.inbounds():
			if new_state.ogre.free():
				val = new_state.ogre.num_pieces()
			else:
				val = the_min(new_state)
		else:
			val = -1
		try:
			if val > max_val:
				state.next = new_state
				max_val = val
		except:
			pdb.set_trace()
	return max_val

def the_min (state):
	print(state)
	min_val = state.ogre.size ** 2
	for pi in range(len(state.people.them)):
		for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
			new_state = copy.deepcopy(state)
			p = state.people.them[pi]
			p.x += dx
			p.y += dy
			new_state.detect_collision()
			new_state.people.bring_out_your_dead()
			if new_state.ogre.inbounds():
				if new_state.ogre.free():
					val = new_state.ogre.num_pieces()
				else:
					val = the_max(new_state)
			else:
				val = -1
			if val < min_val:
				state.next = new_state
				min_val = val
	return min_val

g = Gameboard(10,10)
o = Ogre(4, g)
p = People(4,g)

initial_state = State(g,o,p)

print(initial_state)

print (the_max(initial_state))






