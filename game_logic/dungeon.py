import random as rnd
from enemies import enemy

class Dungeon:
	def __init__(self, log, player):
		# self.enemies = []
		self._log = log
		self._player = player
		self._cur_floor = 1
	@property
	def cur_floor(self):
		return self._cur_floor

	@cur_floor.setter
	def cur_floor(self, new):
		self._cur_floor = new

	@property
	def level(self):
		return self._level

	@level.setter
	def level(self, new):
		self._level = new

	@property
	def boss(self):
		return self._boss

	@boss.setter
	def boss(self, new):
		self._boss = new

	@property
	def floors(self):
		return self._floors

	@floors.setter
	def floors(self, new):
		self._floors = new

	@property
	def log(self):
		return self._log

	@property.setter
	def log(self, new):
		self._log = new

	@property
	def player(self):
		return self._player

	@player.setter
	def player(self, new):
		self._player = new

	@property
	def chests(self):
		return self._chests

	@chests.setter
	def chests(self, new):
		self._chests = new

	@property
	def enemies(self):
		return self._enemies

	@enemies.setter
	def enemies(self, new):
		self._enemies = new

	def create_floor(self):
		self._enemies = []
		self._chests = rnd.randint(0, 1)

	def enter_floor(self):
		total_len = len(self.enemies) + self.chests
		room = rnd.randint(0, total_len - 1)
		while room > 0:
			if self.chests == 1 and room == 1:
				self.player.open_chest()
			else:
				enemy = self.enemies[rnd.randint(0, len(self.enemies))]
				outcome = self._fight(enemy)
				self.enemies.remove(enemy)
				if outcome is 1:
					self._won_fight()
				else:
					print("You have perished, but worry not as there is always another try on which you could succeed")
					return ;
			total_len -= 1
		outcome = self._fight(self.boss)
		if outcome is 1 and self.cur_floor == self.floors:
			print("Congratulations you have finished this dungeon! We hope you enjoyed and will come back to venture further into the depths")
			return ;
		elif outcome is 1:
			self._won_boss_fight()
			self.create_floor()
			self.cur_floor += 1
			return self.enter_floor()
		else:
			print("You have perished, but worry not as there is always another try on which you could succeed")
			return ;

	@staticmethod
	def _won_boss_fight(self):
		print("Congratulation you have slain this floors Boss\n Would you like to:\n [1] Move to the next floor \n [2] Drink a consumable\n (You will move to the next floor after)")
		while True:
			choice = input()
			if choice is "1" or "2" :
				match int(choice):
					case 1:
						return;
					case 2:
						self.player.apply_consumable()
						self.log.info("player drank consumable")
						return;
			self.log.warning("Unknown Player Action selection")
			print("Unknown Player Action selection \n Would you like to:\n [1] Move to the next room \n [2] Drink a consumable")

	@staticmethod
	def _won_fight(self):
		print("Enemy slain\n Would you like to:\n [1] Move to the next room \n [2] Drink a consumable\n (You can only pick one the next fight will start after)")
		while True:
			choice = input()
			if choice is "1" or "2":
				match int(choice):
					case 1:
						return;
					case 2:
						self.player.apply_consumable()
						self.log.info("player drank consumable")
						return;
			self.log.warning("Unknown Player Action selection")
			print("Unknown Player Action selection \n Would you like to:\n [1] Move to the next room \n [2] Drink a consumable")

	@staticmethod
	def _player_action(self, enemy):
		while True:
			print("What would you like to do?\n [1] Attack the enemy \n [2] Drink a consumable")
			choice = input()
			if choice is "1" or "2":
				match int(choice):
					case 1:
						dmg = self.player.get_damage()
						enemy.take_damage(dmg)
						self.log.info("player attacked")
					case 2:
						self.player.apply_consumable()
						self.log.info("player drank consumable")
				return;
			self.log.warning("Unknown Player Action selection")
			print("Unknown Player Action selection \n Would you like to:\n [1] Attack the enemy \n [2] Drink a consumable")

	@staticmethod
	def _enemy_action(self, enemy):
		dmg = enemy.attack()
		self.player.take_damage(dmg)

	@staticmethod
	def _fight(self, enemy):
		first_action = rnd.randint(0,1)
		while enemy.health is not 0 and self.player.is_alive == True:
			if first_action == 1:
				self._enemy_action(enemy)
				first_action = 0
			if self.player.is_alive == True:
				self._player_action(enemy)
			if enemy.health is not 0:
				self._enemy_action(enemy)
		if enemy.health is 0:
			return 1;
		else:
			return 0;


class Easy_Dungeon(Dungeon):
	def __init__(self, log, player):
		super().__init__(log, player)
		self._floors = 2
		self._level = 1

	def create_floor(self):
		super().create_floor()
		self._enemies = [enemy.Bat(self.level), enemy.Brute(self.level)]
		self._boss = enemy.Boss()

class Hard_Dungeon(Dungeon):
	def __init__(self, log, player):
		super().__init__(log, player)
		self._floors = 4
		self._level = 3

	def create_floor(self):
		super().create_floor()
		self._enemies = [enemy.Bat(self.level), enemy.Brute(self.level)]
		self._boss = enemy.Boss()

