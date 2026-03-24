import logging as lg
import os
from player import player as pl
import dungeon as dg
class challengers_quest:
	@property
	def log(self):
		return self._log

	@log.setter
	def log(self, new):
		self._log = new

	@property
	def player(self):
		return self._player

	@player.setter
	def player(self, new):
		self._player = new


	def _create_log_file(self):
		if not os.path.exists("logs"):
			os.mkdir("logs")
		lg.basicConfig(filename="logs/game.log", level=lg.INFO, filemode="a", format="%(asctime)s - %(levelname)s - %(message)s")
		self.log = lg.getLogger(self.__class__.__name__)

	def __init__(self):
		self._create_log_file()
		self.log.info("Challenger Quest object created")

	def _select_char(self):
		print("What name would you like to be called?")
		name = input()
		self.player = pl.Warrior(name)
		self.log.info("Player created")


	def _select_dungeon(self):
		while True:
			print("What dungeon would you like to enter\n [1] Easy\n [2] Hard")
			choice = input()
			if choice in ["1", "2"]:
				match int(choice):
					case 1:
						self.dungeon = dg.Easy_Dungeon(self.log, self.player)
					case 2:
						self.dungeon = dg.Hard_Dungeon(self.log, self.player)
				self.log.info("Dungeon selected")
				return;
			self.log.warning("Unknown Dungeon selection")
			print("Unknown Dungeon selection\n What dungeon would you like to enter\n [1] Easy\n [2] Hard")

	def game_start(self):
		print("---- WELCOME TO CHALLENGERS QUEST ----")
		self._select_char()
		self._select_dungeon()
		self.dungeon.create_floor()
		self.dungeon.enter_floor()
		print("Would you like to continue playing?\n [1] Yes\n [2] No")
		while True:
			choice = input()
			if choice in ["1", "2"]:
				if choice == "1":
					self.game_start()
					self.log.info("Game Restarted")
				else:
					self.log.info("Game Stopped")
					exit(0)
				return;
			self.log.warning("Unknown Choice selection")
			print("Unknown Choice selection\n Would you like to continue playing?\n [1] Yes\n [2] No")

import logging as lg
import os
from player import player as pl
import dungeon as dg
class challengers_quest:
	@property
	def log(self):
		return self._log

	@log.setter
	def log(self, new):
		self._log = new

	@property
	def player(self):
		return self._player

	@player.setter
	def player(self, new):
		self._player = new


	def _create_log_file(self):
		if not os.path.exists("logs"):
			os.mkdir("logs")
		lg.basicConfig(filename="logs/game.log", level=lg.INFO, filemode="a", format="%(asctime)s - %(levelname)s - %(message)s")
		self.log = lg.getLogger(self.__class__.__name__)

	def __init__(self):
		self._create_log_file()
		self.log.info("Challenger Quest object created")

	def _select_char(self):
		print("What name would you like to be called?")
		name = input()
		self.player = pl.Warrior(name)
		self.log.info("Player created")


	def _select_dungeon(self):
		while True:
			print("What dungeon would you like to enter\n [1] Easy\n [2] Hard")
			choice = input()
			if choice in ["1", "2"]:
				match int(choice):
					case 1:
						self.dungeon = dg.Easy_Dungeon(self.log, self.player)
					case 2:
						self.dungeon = dg.Hard_Dungeon(self.log, self.player)
				self.log.info("Dungeon selected")
				return;
			self.log.warning("Unknown Dungeon selection")
			print("Unknown Dungeon selection\n What dungeon would you like to enter\n [1] Easy\n [2] Hard")

	def game_start(self):
		print("---- WELCOME TO CHALLENGERS QUEST ----")
		self._select_char()
		self._select_dungeon()
		self.dungeon.create_floor()
		self.dungeon.enter_floor()
		print("Would you like to continue playing?\n [1] Yes\n [2] No")
		while True:
			choice = input()
			if choice in ["1", "2"]:
				if choice == "1":
					self.game_start()
					self.log.info("Game Restarted")
				else:
					self.log.info("Game Stopped")
					exit(0)
				return;
			self.log.warning("Unknown Choice selection")
			print("Unknown Choice selection\n Would you like to continue playing?\n [1] Yes\n [2] No")



# Game Class - responsible for handling main game loop
# 	tasks include starting game environment, holding player, loading dungeon floors, output logging, death handling

# 	Attributes:
# 		dungeon: Dungeon Class
# 		log_file: fd

# 	Methods:
# 		__init__: setup game environment,  open log_file in append.

# 		game_loop: handles main game loop

# 		game_start: welcome message to player, choose class, choose difficulty, initialize dungeon, start game_loop:

# 		game_exit: says taunting goodbye message, closes log_file

import logging as lg
import os
from player import player as pl
import dungeon as dg
class challengers_quest:
	@property
	def log(self):
		return self._log

	@log.setter
	def log(self, new):
		self._log = new

	@property
	def player(self):
		return self._player

	@player.setter
	def player(self, new):
		self._player = new


	def _create_log_file(self):
		if not os.path.exists("logs"):
			os.mkdir("logs")
		lg.basicConfig(filename="logs/game.log", level=lg.INFO, filemode="a", format="%(asctime)s - %(levelname)s - %(message)s")
		self.log = lg.getLogger(self.__class__.__name__)

	def __init__(self):
		self._create_log_file()
		self.log.info("Challenger Quest object created")

	def _select_char(self):
		print("What name would you like to be called?")
		name = input()
		self.player = pl.Warrior(name)
		self.log.info("Player created")


	def _select_dungeon(self):
		while True:
			print("What dungeon would you like to enter\n [1] Easy\n [2] Hard")
			choice = input()
			if choice in ["1", "2"]:
				match int(choice):
					case 1:
						self.dungeon = dg.Easy_Dungeon(self.log, self.player)
					case 2:
						self.dungeon = dg.Hard_Dungeon(self.log, self.player)
				self.log.info("Dungeon selected")
				return;
			self.log.warning("Unknown Dungeon selection")
			print("Unknown Dungeon selection\n What dungeon would you like to enter\n [1] Easy\n [2] Hard")

	def game_start(self):
		print("---- WELCOME TO CHALLENGERS QUEST ----")
		self._select_char()
		self._select_dungeon()
		self.dungeon.create_floor()
		self.dungeon.enter_floor()
		print("Would you like to continue playing?\n [1] Yes\n [2] No")
		while True:
			choice = input()
			if choice in ["1", "2"]:
				if choice == "1":
					self.game_start()
					self.log.info("Game Restarted")
				else:
					self.log.info("Game Stopped")
					exit(0)
				return;
			self.log.warning("Unknown Choice selection")
			print("Unknown Choice selection\n Would you like to continue playing?\n [1] Yes\n [2] No")



# Game Class - responsible for handling main game loop
# 	tasks include starting game environment, holding player, loading dungeon floors, output logging, death handling

# 	Attributes:
# 		dungeon: Dungeon Class
# 		log_file: fd

# 	Methods:
# 		__init__: setup game environment,  open log_file in append.

# 		game_loop: handles main game loop

# 		game_start: welcome message to player, choose class, choose difficulty, initialize dungeon, start game_loop:

# 		game_exit: says taunting goodbye message, closes log_file

import logging as lg
import os
from player import player as pl
import dungeon as dg
class challengers_quest:
	@property
	def log(self):
		return self._log

	@log.setter
	def log(self, new):
		self._log = new

	@property
	def player(self):
		return self._player

	@player.setter
	def player(self, new):
		self._player = new


	def _create_log_file(self):
		if not os.path.exists("logs"):
			os.mkdir("logs")
		lg.basicConfig(filename="logs/game.log", level=lg.INFO, filemode="a", format="%(asctime)s - %(levelname)s - %(message)s")
		self.log = lg.getLogger(self.__class__.__name__)

	def __init__(self):
		self._create_log_file()
		self.log.info("Challenger Quest object created")

	def _select_char(self):
		print("What name would you like to be called?")
		name = input()
		self.player = pl.Warrior(name)
		self.log.info("Player created")


	def _select_dungeon(self):
		while True:
			print("What dungeon would you like to enter\n [1] Easy\n [2] Hard")
			choice = input()
			if choice in ["1", "2"]:
				match int(choice):
					case 1:
						self.dungeon = dg.Easy_Dungeon(self.log, self.player)
					case 2:
						self.dungeon = dg.Hard_Dungeon(self.log, self.player)
				self.log.info("Dungeon selected")
				return;
			self.log.warning("Unknown Dungeon selection")
			print("Unknown Dungeon selection\n What dungeon would you like to enter\n [1] Easy\n [2] Hard")

	def game_start(self):
		print("---- WELCOME TO CHALLENGERS QUEST ----")
		self._select_char()
		self._select_dungeon()
		self.dungeon.create_floor()
		self.dungeon.enter_floor()
		print("Would you like to continue playing?\n [1] Yes\n [2] No")
		while True:
			choice = input()
			if choice in ["1", "2"]:
				if choice == "1":
					self.game_start()
					self.log.info("Game Restarted")
				else:
					self.log.info("Game Stopped")
					exit(0)
				return;
			self.log.warning("Unknown Choice selection")
			print("Unknown Choice selection\n Would you like to continue playing?\n [1] Yes\n [2] No")


if __name__ == "__main__":
	cp = challengers_quest()
	cp.game_start()
