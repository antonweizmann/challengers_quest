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
            line_count = sum(1 for line in file)
            line_to_get = gen_random_int(line_count - 1)
            for i, line in enumerate(file):
                if i == line_to_get:
                    name, rarity, damage, stamina_use = line.split('#')
                    break
        return {'name': name, 'rarity': rarity, 'damage': damage, 'stamina_use': stamina_use}
    except FileNotFoundError as e:
        print(e)

'''
comsumable_pool.txt lines contain an unique item using # seperater in the following format: 
<name>#<rarity>#<use_type>#<effect_amt>
'''
def get_random_consumable(in_file="consumable_pool.txt"):
    try:
        with open(in_file, "r") as file:
            line_count = sum(1 for line in file)
            line_to_get = gen_random_int(line_count - 1)
            for i, line in enumerate(file):
                if i == line_to_get:
                    name, rarity, use_type, effect_amt = line.split('#')
                    break  
        return {'name': name, 'rarity': rarity, 'use_type': use_type, 'effect_amt': effect_amt}           
    except FileNotFoundError as e:
        print(e)



    
            