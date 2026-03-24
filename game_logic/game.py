import logging as lg
import os

class challengers_quest:
	def _create_log_file(self):
		if not os.path.exists("logs"):
			os.mkdir("logs")
		lg.basicConfig(filename="logs/game.log", level=lg.INFO, filemode="a", format="%(asctime)s - %(levelname)s - %(message)s")
		self.log = lg.getLogger(self.__class__.__name__)

	def __init__(self):
		self._create_log_file()
		self.log.info("Challenger Quest object created")

	def _select_char(self):

		while True:
			print("What character would you like to play as \
					[1] Warrior or [2] Magician")


	def game_start(self):
		print("---- WELCOME TO CHALLENGERS QUEST ----")

		self.player = self._select_char()



if __name__ == "__main__":
	cq = challengers_quest()
	cq.log.warning("Test2")



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

