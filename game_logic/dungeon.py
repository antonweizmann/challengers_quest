import random as rnd
class Dungeon:
	def __init__(self, log):
		# self.enemies = []
		self.chests = rnd.randint(0, 1)
		self.log = log
	def enter_floor(self):
		self.total_len = len(self.enemies) + self.chests
		room = rnd.randint(0, self.total_len - 1)
		if self.chests == 1 &&


x	
