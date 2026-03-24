import random as rdm

class Enemy:
    total_enemies_created = 0

    def __init__(self, name: str, level: int):
        self.is_aggro = True
        self.name = name
        self.__level = level

        self._health = 30 * level
        self._base_damage = level * 4
        Enemy.total_enemies_created += 1

    @property
    def level(self):
        return self.__level

    @property
    def health(self):
        return self._health

    # @property
    # def name(self):
    #     return self.name

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
        print(f"{self.name} took {damage} damage! Remaining: {self.health}")


    def check_status(self):
        return "Low" if self.health < 10 else "Fine"

    def regenerate(self):
        heal_amount = self.__level * 2
        self.health += heal_amount
        print(f"{self.name} regenerated {heal_amount} HP.")

    def get_difficulty_rating(self):
        return "Hard" if self.__level >= 3 else "Common"

    def __str__(self):
        return f"[Enemy]: {self.name} HP-[{self.health}] LVL-[{self.level}]"

class Boss(Enemy):
    def __init__(self, level: int):
        super().__init__("Gorlock-3000", level *2)
        self._health *= self.health_multiplier()

    @staticmethod
    def health_multiplier():
        return rdm.randint(1, 4)

    def attack(self):
        return super().attack() +20

    def take_damage(self, damage):
        actual_dmg = max(0, damage - 10)
        super().take_damage(actual_dmg)

    def __str__(self):
        return f"[Enemy]: {self.name} HP-[{self.health}] LVL-[{self.level}]"

class Bat(Enemy):
    def __init__(self, level: int):
        super().__init__("Bat", level)
        self._health *= 0.5
        self._base_damage -= 2


    def attack(self):
        number = rdm.randint(1, 10)
        if number > 3:
            dmg = super().attack()
            print(f"Bat's attack hit! ({dmg} DMG) ")
            return dmg
        else:
            print("Bat's attack missed! (0 DMG)")
            return 0

    def take_damage(self, damage):
        number = rdm.randint(1, 10)
        if number > 3:
            print(f"Bat got hit by the attack! ({self.health} HP)")
            super().take_damage(damage)
        else:
            print("Bat dodged the attack! (0 DMG)")
            return 0


    def __str__(self):
        return f"[Enemy]: {self.name} HP-[{self.health}] LVL-[{self.level}]"


class Goblin(Enemy):
    def __init__(self, level: int):
        super().__init__("Goblin",level)

    def __str__(self):
        return f"[Enemy]: {self.name} HP-[{self.health}] LVL-[{self.level}]"

class Brute(Enemy):
    def __init__(self, level: int):
        super().__init__("Brute", 5 + level)
        self._health *= 1.2
        self._base_damage += 1

    def take_damage(self, damage):
        actual_dmg = max(0, damage - 5)
        super().take_damage(actual_dmg)

    def __str__(self):
        return f"[Enemy]: {self.name} HP-[{self.health}] LVL-[{self.level}]"



