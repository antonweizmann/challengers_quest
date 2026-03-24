import random as rnd
from enemies import enemy

class Dungeon:

	dungeons_explored = 0
	def __init__(self, log, player):
		# self.enemies = []
		self._log = log
		self.__dungeon_id = rnd.randint(1000, 9999)
		self._log.info(f"Initialized dungeon {self.__dungeon_id}")
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

	@log.setter
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

	@classmethod
	def get_dungeons_explored(cls):
		return cls.dungeons_explored

	def create_floor(self):
		self._enemies = []
		self._chests = rnd.randint(0, 1)

	def enter_floor(self):
		events = (['enemy'] * len(self.enemies)) + (['chest'] * self.chests)
		rnd.shuffle(events)
		rnd.shuffle(self.enemies)
		for event in events:
			print(f"You enter the room and encounter a {event}")
			if event == 'chest':
				self.player.open_chest()
			else:
				opponent = self.enemies.pop()
				print(f"Its a {opponent.name}")
				outcome = self._fight(opponent)
				if outcome == 1:
					self._won_fight()
				else:
					print(f"You have perished under the might of {enemy.Enemy.total_enemies_created} enemies, but worry not as there is always another try on which you could succeed")
					return ;
		outcome = self._fight(self.boss)
		if outcome == 1 and self.cur_floor == self.floors:
			Dungeon.dungeons_explored += 1
			print(f"Congratulations you have finished this dungeon! You have ventured into {Dungeon.get_dungeons_explored()} We hope you enjoyed and will come back to venture further into the depths")
			return ;
		elif outcome == 1:
			self._won_boss_fight()
			self.create_floor()
			self.cur_floor += 1
			self.level += 1
			return self.enter_floor()
		else:
			print(f"You have perished under the might of {enemy.Enemy.total_enemies_created} enemies, but worry not as there is always another try on which you could succeed")
			return ;

	def _won_boss_fight(self):
		print("Congratulation you have slain this floors Boss\n Would you like to:\n [1] Move to the next floor \n [2] Drink a consumable\n (You will move to the next floor after)")
		while True:
			choice = input()
			if choice in ["1", "2"] :
				match int(choice):
					case 1:
						return;
					case 2:
						self.player.apply_consumable()
						self.log.info("player drank consumable")
						return;
			self.log.warning("Unknown Player Action selection")
			print("Unknown Player Action selection ")

	def _won_fight(self):
		print("Enemy slain\n Would you like to:\n [1] Move to the next room \n [2] Drink a consumable\n (You can only pick one the next fight will start after)")
		while True:
			choice = input()
			if choice in ["1", "2"]:
				match int(choice):
					case 1:
						return;
					case 2:
						self.player.apply_consumable()
						self.log.info("player drank consumable")
						return;
			self.log.warning("Unknown Player Action selection")
			print("Unknown Player Action selection ")

	def _player_action(self, enemy):
		while True:
			print("What would you like to do?\n [1] Attack the enemy \n [2] Drink a consumable")
			choice = input()
			if choice in ["1", "2"]:
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
			print("Unknown Player Action selection ")

	def _enemy_action(self, enemy):
		dmg = enemy.attack()
		self.player.take_damage(dmg)

	def _fight(self, enemy):
		first_action = rnd.randint(0,1)
		while enemy.health > 0 and self.player.is_alive == True:
			if first_action == 1:
				self._enemy_action(enemy)
				first_action = 0
				print("\n")
			# self.player.take_damage(1000)
			if self.player.is_alive == True:
				self._player_action(enemy)
				print("\n")
			if enemy.health > 0 and self.player.is_alive == True:
				self._enemy_action(enemy)
				print("\n")
		if enemy.health == 0:
			return 1;
		else:
			return 0;

	def __str__(self):
		return f"Dungeon Level: {self.level}, Current Floor: {self.cur_floor}"


class Easy_Dungeon(Dungeon):
	def __init__(self, log, player):
		super().__init__(log, player)
		self._floors = 2
		self._level = 1

	def create_floor(self):
		super().create_floor()
		available_enemies = [enemy.Bat, enemy.Bat, enemy.Brute, enemy.Goblin, enemy.Goblin, enemy.Goblin, enemy.Goblin]
		total_enemies = 3 * self.level
		self._enemies = [rnd.choice(available_enemies)(self.level) for _ in range(total_enemies)]
		self._boss = enemy.Boss(self.level)

class Hard_Dungeon(Dungeon):
	def __init__(self, log, player):
		super().__init__(log, player)
		self._floors = 3
		self._level = 3

	def create_floor(self):
		super().create_floor()
		available_enemies = [enemy.Bat, enemy.Bat, enemy.Brute, enemy.Goblin, enemy.Goblin]
		total_enemies = 3 * self.level
		self._enemies = [rnd.choice(available_enemies)(self.level) for _ in range(total_enemies)]
		self._boss = enemy.Boss(self.level)

	def _won_boss_fight(self):
		print("Congratulation you have bested this hard floors Boss\n Would you like to. We commend you \n As a reward take a new weapon")
		self.player.add_weapon()
		print("[1] Move to the next floor \n [2] Drink a consumable\n (You will move to the next floor after)")
		while True:
			choice = input()
			if choice in ["1", "2"] :
				match int(choice):
					case 1:
						return;
					case 2:
						self.player.apply_consumable()
						self.log.info("player drank consumable")
						return;
			self.log.warning("Unknown Player Action selection")
			print("Unknown Player Action selection ")

