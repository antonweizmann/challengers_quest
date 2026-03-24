import random as rdm

def gen_random_int(upper_limit: int):
    return rdm.randint(0, upper_limit)

'''
weapon_pool.txt lines contain an unique item using # seperater in the following format:
<name>#<rarity>#<damage>#<stamina_use>
'''
def get_random_weapon(in_file="weapon_pool.txt"):
    try:
        with open(in_file, "r") as file:
            lines = file.readlines() # Reads everything into a list memory once
            line_to_get = gen_random_int(len(lines) - 1)
            line = lines[line_to_get]
            name, rarity, damage, stamina_use = line.strip().split('#')
        return {'name': name, 'rarity': rarity, 'damage': int(damage), 'stamina_use': int(stamina_use)}
    except FileNotFoundError as e:
        print(f"ERROR: Could not find {in_file}! Giving a default weapon instead.")
        return {'name': 'Broken Stick', 'rarity': 'Poor', 'damage': 10, 'stamina_use': 1}

'''
comsumable_pool.txt lines contain an unique item using # seperater in the following format:
<name>#<rarity>#<use_type>#<effect_amt>
'''
def get_random_consumable(in_file="consumable_pool.txt"):
    try:
        with open(in_file, "r") as file:
            lines = file.readlines() # Reads everything into a list memory once
            line_to_get = gen_random_int(len(lines) - 1)
            line = lines[line_to_get]
            name, rarity, use_type, effect_amt = line.strip().split('#')
        return {'name': name, 'rarity': rarity, 'use_type': use_type, 'effect_amt': int(effect_amt)}
    except FileNotFoundError as e:
        print(f"ERROR: Could not find {in_file}! Giving a default consumable instead.")
        return {'name': 'Mouldy Bread', 'rarity': 'Poor', 'use_type': 'health', 'effect_amt': 5}




