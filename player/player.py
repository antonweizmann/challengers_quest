import random as rdm
from player.lootpool import loot_pool_manager as lpm

class Person:
    num_of_deaths = 0
    def __init__(self, name: str, health: float, stamina: float):
        self.name = name
        self._health = health
        self._stamina = stamina
        self._is_alive = True

    @property
    def is_alive(self):
        return self._is_alive

    @is_alive.setter
    def is_alive(self, new_state: bool):
        if self._is_alive == True and new_state == False:
            Person.num_of_deaths += 1
            print(f"{self.name} has died")
        elif self._is_alive == False and new_state == True:
            print(f"{self.name} has been resurected")
        self._is_alive = new_state

    @classmethod
    def get_death_toll(cls):
        return cls.num_of_deaths


class Warrior(Person):
    def __init__(self, name: str):
        super().__init__(name, self.gen_start_values(), self.gen_start_values())
        self.__items = {'weapons': None, 'consumables': []}
        self.__armour = self.gen_start_values()
        self.add_weapon()
        self.add_consumable()

    def __str__(self):
        person_sym = '\U0001F464'
        heart_sym = '\u2764'
        stamina_sym = '\u26A1'
        shield_sym = '\U0001F6E1'

        return (f"{person_sym} {self.name}\t{heart_sym} {self._health}\t{stamina_sym} {self._stamina}\t{shield_sym} {self.__armour}")

    @staticmethod
    def gen_start_values():
        return rdm.randint(70, 100)

    def get_damage(self):
        if self.__items['weapons']:
            return self.__items['weapons'].damage
        else:
            return 5

    def take_damage(self, damage_amt: int):
        if damage_amt > self.__armour:
            remaining_damage = damage_amt - self.__armour
            self.__armour = 0
            self._health -= remaining_damage
            if self._health < 0:
                self._health = 0
            print(f"{self.name} took {remaining_damage} damage! Remaining: {self._health}")
            if self._health <= 0:
                self._health = 0
                self.is_alive = False
        else:
            self.__armour -= damage_amt
            print(f"{self.name} lost {damage_amt} armour! Remaining: {self.__armour} armour and {self._health} health")


    def add_weapon(self):
        new_weapon = Weapon()
        print(f"You picked up {new_weapon}")
        self.__items['weapons'] = new_weapon

    def remove_weapon(self):
        self.__items['weapons'] = None

    def add_consumable(self):
        new_consumable = Consumable()
        print(f"You picked up {new_consumable}")
        self.__items['consumables'].append(new_consumable)

    def remove_consumable(self, consumablename: str):
        for consumable in self.__items['consumables']:
            if consumable.name == consumablename:
                self.__items['consumables'].remove(consumable)
                break

    def _select_consumable(self):
        if not self.__items['consumables']:
            print("Your inventory is empty!")
            return None
        while True:
            choice = input("Enter consumable name: ").strip().lower()
            target = next((item for item in self.__items['consumables'] if item.name.lower() == choice), None)
            if target:
                return target
            print(f"You do not have '{choice}'. Please enter a consumable you do have.")

    def apply_consumable(self):
        self.list_consumables()
        target_consumable = self._select_consumable()

        if target_consumable:
            match (target_consumable.use_type):
                case 'health':
                    self._health += target_consumable.effect_amt
                case 'stamina':
                    self._stamina += target_consumable.effect_amt
                case 'armour':
                    self.__armour += target_consumable.effect_amt

            print(f"+{target_consumable.effect_amt} {target_consumable.use_type}")
            self.remove_consumable(target_consumable.name)

    def list_consumables(self):
        print("Consumables in Inventory:\n")
        for cItem in self.__items['consumables']:
            print(cItem)

    def use_stamina(self):
        stamina_amt = self.__items['weapons'].stamina_use
        if self._stamina - stamina_amt < 0:
            print("Not enough stamina to attack")
            return 1
        else:
            self._stamina = self._stamina - stamina_amt
            print(f"-{stamina_amt} stamina from weapon")
            return 0

    def give_stamina(self):
        stamina_amt = rdm.randint(10, 10)
        self._stamina = self._stamina + stamina_amt
        print(f"+{stamina_amt} stamina")

    def open_chest(self):
        match (rdm.randint(0, 1)):
            case 0:
                self.add_weapon()
            case 1:
                self.add_consumable()

class Item:
    def __init__(self, name: str, rarity: str):
        self.name = name
        self._amount = 1
        self._rarity = rarity

    #to increase amount <itemname> += value
    def __iadd__(self, amt):
        self._amount += amt
        return self

    # @property
    # def name(self):
    #     return self.name

    @property
    def amount(self):
        return self._amount

    @property
    def rarity(self):
        return self._rarity

class Consumable(Item):
    def __init__(self):
        consumable_info_dict = lpm.get_random_consumable()
        super().__init__(consumable_info_dict['name'], consumable_info_dict['rarity'])
        self.__use_type = consumable_info_dict['use_type']
        self.__effect_amt = consumable_info_dict['effect_amt']

    def __str__(self):
        return f"{self.name} ({self._rarity}) -> {self.__use_type} +{self.__effect_amt}\n"

    @property
    def use_type(self):
        return self.__use_type

    @property
    def effect_amt(self):
        return self.__effect_amt


class Weapon(Item):
    def __init__(self):
        weapon_info_dict = lpm.get_random_weapon()
        super().__init__(weapon_info_dict['name'], weapon_info_dict['rarity'])
        self.__damage = weapon_info_dict['damage']
        self.__stamina_use = weapon_info_dict['stamina_use']

    def __str__(self):
        output = (f"{self.name} ({self._rarity}) Stats\n"
              f"Damage:\t{self.__damage}\n"
              f"Stamina Use:\t{self.__stamina_use}\n")
        return output

    @property
    def damage(self):
        return self.__damage

    @property
    def stamina_use(self):
            return self.__stamina_use






