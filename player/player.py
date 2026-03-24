import random as rdm
import loot_pool_manager as lpm

#need to add operator overloads (<=+ damage maybe)
class Person:
    num_of_deaths = 0
    def __init__(self, name: str, health: float, hydration: float, stamina: float):
        self._name = name
        self._health = health
        self._hydration = hydration
        self._stamina = stamina
        self._is_alive = True

    def use_stamina(self, stamina_use: int):
        self._stamina = self._stamina - stamina_use
    
    def use_hydration(self, hydration_use: int):
        self._hydration = self._hydration - hydration_use
    
    @property
    def is_alive(self):
        return self._is_alive
    
    @is_alive.setter
    def is_alive(self, new_state: bool):
        if self._is_alive == True and new_state == False:
            Person.num_of_deaths += 1
        self._is_alive = new_state

    @classmethod
    def get_death_toll(cls):
        return cls.num_of_deaths
    

class Warrior(Person):
    def __init__(self, name: str):
        super().__init__(name, self.gen_start_values(), self.gen_start_values(), self.gen_start_values())
        self.__items = {'weapons': [], 'consumables': [], 'buffs': []}
        self.__armour = self.gen_start_values()

    def __str__(self):
        person_sym = '\U0001F464'
        heart_sym = '\u2764'
        water_sym = '\U0001F4A7'
        stamina_sym = '\u26A1'
        shield_sym = '\U0001F6E1'

        return f"{person_sym} {self._name}\t{heart_sym} {self._health}\t{water_sym} {self._hydration}\t{stamina_sym} {self._stamina}\t{shield_sym} {self.__armour}"

    @staticmethod
    def gen_start_values():
        return rdm.randint(70, 100)
    
    def take_damage(self, damage_amt: int):
        if damage_amt > self.__armour:
            remaining_damage = damage_amt - self.__armour
            self.__armour = 0
            if remaining_damage > self.__health:
                self.__health = 0
                self._is_alive = False
            else: 
                self.__health = self.__health - (damage_amt - self.__armour)
        else: self.__armour = self.__armour - damage_amt
        

    def add_weapon(self):
        new_weapon = Weapon()
        self.__items['weapons'].append(new_weapon)
    
    def remove_weapon(self, weapon_name: str):
        for weapon in self.__items['weapons']:
            if weapon.name == weapon_name:
                self.__items['weapons'].remove(weapon)

    def add_consumable(self):
        new_consumable = Consumable()
        self.__items['consumables'].append(new_consumable)
    
    def remove_consumable(self, consumable_name: str):
        for consumable in self.__items['consumables']:
            if consumable.name == consumable_name:
                self.__items['consumables'].remove(consumable)
    
    def add_buff(self):
        new_buff = Buff()
        self.__items['buffs'].append(new_buff)
    
    def remove_buff(self, buff_name):
        for buff in self.__items['buffs']:
            if buff.name == buff_name:
                self.__items['buffs'].remove(buff)

    def open_chest(self):
        match (rdm.randint(1, 100)):
            case n if 1 <= n <= 15:
                weapon = self.add_weapon()
                return weapon
            case n if 15 < n <= 50:
                buff = self.add_buff()
                return buff
            case _:
                consumable = self.add_consumable()
                return consumable
            
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

class Weapon(Item):
    def __init__(self):
        weapon_info_dict = lpm.get_random_weapon()
        super().__init__(weapon_info_dict['name'], weapon_info_dict['rarity'])
        self.__durability = rdm.randint(60, 100)
        self.__damage = weapon_info_dict['damage']
        self.__stamina_use = weapon_info_dict['stamina_use']

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
        

class Consumable(Item):
    def __init__(self):
        consumable_info_dict = lpm.get_random_consumable()
        super().__init__(consumable_info_dict['name'], consumable_info_dict['rarity'])
        self.__use_type = consumable_info_dict['use_type']
        self.__effect_amt = consumable_info_dict['effect_amt']

    #returns a tuple of (use_type, effect_amt)
    def get_consumable_info(self):
        return (self.__use_type, self.__effect_amt)
        
class Buff(Item):
    def __init__(self):
        buff_info_dict = lpm.get_random_buff()
        super().__init__(buff_info_dict['name'], buff_info_dict['rarity'])
        self.__buff_type = buff_info_dict['buff_type']
        self.__buff_percent = buff_info_dict['buff_percent']
        self.__buff_duration = buff_info_dict['buff_duration']

    #returns a tuple of (buff_type, buff_percent, buff_duration)
    def get_buff_info(self):
        return (self.__buff_type, self.__buff_percent, self.__buff_duration)
    
    def dec_duration(self):
        self.__buff_duration = self.__buff_duration - 1



