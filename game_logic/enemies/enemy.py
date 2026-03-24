import random as rdm

class Enemy:
    total_enemies_created = 0

    def __init__(self, name: str, level: int):
        self.is_aggro = True
        self._name = name
        self.__level = level

        self._health = 20 * level
        self._base_damage = level * 4
        Enemy.total_enemies_created += 1

    @property
    def level(self):
        return self.__level

    @property
    def health(self):
        return self._health

    @property
    def name(self):
        return self._name

    @level.setter
    def level(self, value):
        if value > 0:
            self.__level = value

    @health.setter
    def health(self, value):
        self._health = max(0, value)

    #methods
    def attack(self):
        return rdm.randint(1, self._base_damage)


    def get_attack_dmg(self):

        return self.attack()

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
        print(f"{self._name} took {damage} damage! Remaining: {self.health}")

    def get_taken_dmg(self):
        return self.take_damage

    def check_status(self):
        return "Low" if self.health < 10 else "Fine"

    def __str__(self):
        return f"[Enemy]: {self._name} HP-[{self.health}] LVL-[{self.__level}]"

class Boss(Enemy):
    def __init__(self, level: int):
        lvl = self.gen_start_values()
        super().__init__("Gorlock-3000", lvl)
        self._health *= 3

    @staticmethod
    def gen_start_values():
        return rdm.randint(5, 20)

    def attack(self):
        return super().attack() +20

    def take_damage(self, damage):
        actual_dmg = max(0, damage - 10)
        super().take_damage(actual_dmg)


class Bat(Enemy):
    def __init__(self, level: int):
        super().__init__("Bat", self.gen_start_values())
        self._health *= 0.6
        self._base_damage = level * 4

    @staticmethod
    def gen_start_values():
        return rdm.randint(1, 10)

    def attack(self):
        number = rdm.randint(1, 10)
        if number >= 5:
            print(f"Bat's attack hit! ({self.get_attack_dmg()} DMG) ")
            return super().attack()
        else:
            print("Bat's attack missed! (0 DMG)")

    def take_damage(self, damage):
        number = rdm.randint(1, 10)
        if number >= 6:
            print(f"Bat got hit by the attack! ({self.get_taken_damage()} DMG)")
            super().take_damage(damage)
        else:
            print("Bat dodged the attack! (0 DMG)")


class Goblin(Enemy):
    def __init__(self, level: int):
        super().__init__("Goblin",level)

class Brute(Enemy):
    def __init__(self, level: int):
        super().__init__("Brute", 2 + level)
        self._health *= 0.8
        self._base_damage += 1

    def take_damage(self, damage):
        actual_dmg = max(0, damage - 5)
        super().take_damage(actual_dmg)



