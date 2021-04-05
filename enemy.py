class Enemy:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)
            
def find_enemy_dict(item):
    for key1 in list(enemy_list.keys()):
        if item == key1:
                return enemy_list[key1]
            
enemy_list = {
    'slime':{
        'name': 'slime',
        'max_hp': 1,
        'hp': 1,
        'ac': 7,
        'atk_mod': -1,
        'min_atk': 1,
        'max_atk': 1,
        'loot_chance': 5,
        'min_gold': 1,
        'max_gold': 5
        },
    'pixie':{
        'name': 'pixie',
        'max_hp': 1,
        'hp': 1,
        'ac': 8,
        'atk_mod': 0,
        'min_atk': 1,
        'max_atk': 1,
        'loot_chance': 5,
        'min_gold': 1,
        'max_gold': 5
        },
    'goblin':{
        'name': 'goblin',
        'max_hp': 3,
        'hp': 3,
        'ac': 10,
        'atk_mod': 0,
        'min_atk': 1,
        'max_atk': 2,
        'loot_chance': 20,
        'min_gold': 5,
        'max_gold': 20
        },
    'goblin chief':{
        'name': 'goblin chief',
        'max_hp': 5,
        'hp': 5,
        'ac': 7,
        'atk_mod': 1,
        'min_atk': 1,
        'max_atk': 2,
        'loot_chance': 40,
        'min_gold': 10,
        'max_gold': 30
        },
    'troll':{
        'name': 'troll',
        'max_hp': 6,
        'hp': 6,
        'ac': 14,
        'atk_mod': 1,
        'min_atk': 1,
        'max_atk': 3,
        'loot_chance': 50,
        'min_gold': 10,
        'max_gold': 30
        },
    'skeleton':{
        'name': 'skeleton',
        'max_hp': 5,
        'hp': 5,
        'ac': 10,
        'atk_mod': 1,
        'min_atk': 2,
        'max_atk': 2,
        'loot_chance': 90,
        'min_gold': 15,
        'max_gold': 25
        },
    'ghoul':{
        'name': 'ghoul',
        'max_hp': 6,
        'hp': 6,
        'ac': 11,
        'atk_mod': 0,
        'min_atk': 1,
        'max_atk': 2,
        'loot_chance': 90,
        'min_gold': 15,
        'max_gold': 25
        },
    'werewolf':{
        'name': 'werewolf',
        'max_hp': 8,
        'hp': 8,
        'ac': 13,
        'atk_mod': 2,
        'min_atk': 2,
        'max_atk': 3,
        'loot_chance': 100,
        'min_gold': 20,
        'max_gold': 35
        },
    'vampire':{
        'name': 'vampire',
        'max_hp': 7,
        'hp': 7,
        'ac': 14,
        'atk_mod': 1,
        'min_atk': 1,
        'max_atk': 4,
        'loot_chance': 100,
        'min_gold': 25,
        'max_gold': 50
        },
    }