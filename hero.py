default_vals = {
    'name': 'hero',
    'x': 0,
    'y': 0,
    'near_enemies': False,
    'in_combat': False,
    'hp': 10,
    'ac': 10,
    'atk_mod': 0,
    'min_atk': 0,
    'max_atk': 0,
    'gp': 0,
    'main_hand': 'stick',
    'off_hand': '',
    'head': 'leather_helmet',
    'chest': '',
    'legs': '',
    'inventory':{
        'slot1': '',
        'slot2': '',
        'slot3': '',
        'slot4': '',
        'slot5': '',
        'slot6': '',
        'slot7': '',
        'slot8': '',
        'slot9': '',
        'slot10': '',}
    }

class Hero:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)