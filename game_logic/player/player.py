import random as rdm
from player.lootpool import loot_pool_manager as lpm

class Person:
    num_of_deaths = 0
    def __init__(self, name: str, health: float, stamina: float):
        self._name = name
        self._health = health
        self._stamina = stamina
        self._is_alive = True

    def use_stamina(self, stamina_use: int):
        self._stamina = self._stamina - stamina_use

    @property
    def is_alive(self):
        return self._is_alive

    @is_alive.setter
    def is_alive(self, new_state: bool):
        if self._is_alive == True and new_state == False:
            Person.num_of_deaths += 1
            print(f"{self._name} has died")
        elif self._is_alive == False and new_state == True:
            print(f"{self._name} has been resurected")
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

    def __str__(self):
        person_sym = '\U0001F464'
        heart_sym = '\u2764'
        stamina_sym = '\u26A1'
        shield_sym = '\U0001F6E1'

        return (f"{person_sym} {self._name}\t{heart_sym} {self._health}\t{stamina_sym} {self._stamina}\t{shield_sym} {self.__armour}")

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
            print(f"{self._name} took {remaining_damage} damage! Remaining: {self._health}")
            if self._health <= 0:
                self._health = 0
                self.is_alive = False
        else:
            self.__armour -= damage_amt
            print(f"{self._name} lost {damage_amt} armour! Remaining: {self.__armour} armour and {self._health} health")


    def add_weapon(self):
        new_weapon = Weapon()
        self.__items['weapons'] = new_weapon

    def remove_weapon(self):
        self.__items['weapons'] = None

    def add_consumable(self):
        new_consumable = Consumable()
        print(f"You picked up {new_consumable}")
        self.__items['consumables'].append(new_consumable)

    def remove_consumable(self, consumable_name: str):
        for consumable in self.__items['consumables']:
            if consumable.name == consumable_name:
                self.__items['consumables'].remove(consumable)
                break


    def _select_consumable(self):
        while True:
            choice = input()
            if self.__items['consumables'].find(choice):
                return choice
            print("You do not have this consumable please enter a consumable you do have")

    def apply_consumable(self):
        self.list_consumables()
        consumable_name = self._select_consumable()

        target_consumable = None

        for consumable in self.__items['consumables']:
            if consumable.name == consumable_name:
                target_consumable = consumable
                break

        if target_consumable:
            match (target_consumable.use_type):
                case 'health':
                    self._health += target_consumable.effect_amt
                case 'stamina':
                    self._stamina += target_consumable.effect_amt
                case 'armour':
                    self.__armour += target_consumable.effect_amt

            print(f"+{target_consumable.effect_amt} {target_consumable.use_type}")
            self.remove_consumable(consumable_name)
        else:
            print("Consumable name doesn't exist in inventory")

    def list_consumables(self):
        print("Consumables in Inventory:\n")
        for cItem in self.__items['consumables']:
            print(cItem)


    def open_chest(self):
        match (rdm.randint(0, 1)):
            case 0:
                self.add_weapon()
            case 1:
                self.add_consumable()

class Item:
    def __init__(self, name: str, rarity: str):
        self._name = name
        self._amount = 1
        self._rarity = rarity

    #to increase amount <itemname> += value
    def __iadd__(self, amt):
        self._amount += amt
        return self

    @property
    def name(self):
        return self._name

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
        return f"{self._name} ({self._rarity}) -> {self.__use_type} +{self.__effect_amt}\n"

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
        self.__durability = rdm.randint(60, 100)
        self.__damage = weapon_info_dict['damage']
        self.__stamina_use = weapon_info_dict['stamina_use']

    def __str__(self):
        output = (f"{self._name} ({self._rarity}) Stats\n"
              f"Durability:\t{self.__durability}\n"
              f"Damage:\t{self.__damage}\n"
              f"Stamina Use:\t{self.__stamina_use}\n")
        return output

    @property
    def durability(self):
        return self.__durability

    def use_durability(self, durability_use):
        self.__durability = self.__durability - durability_use

    @property
    def damage(self):
        return self.__damage

    @property
    def stamina_use(self):
            return self.__stamina_use






