

def find_loot_dict(item):
    for key1 in list(loot_table.keys()):
        if key1 == 'item':
            for key2 in list(loot_table[key1].keys()):
                for key3 in list(loot_table[key1][key2].keys()):
                    if item == key3:
                        return loot_table[key1][key2][key3]
        for key2 in list(loot_table[key1].keys()):
            if item == key2:
                return loot_table[key1][key2]

loot_table = {
        'main_hand':{
            'stick':{
                'name': 'stick',
                'slots': ['main_hand', 'off_hand'],
                'atk_mod': 1,
                'min_atk': 1,
                'max_atk': 1,
                'gp': 2
                },
            'wood_sword':{
                'name': 'wooden sword',
                'slots': ['main_hand', 'off_hand'],
                'atk_mod': 2,
                'min_atk': 1,
                'max_atk': 2,
                'gp': 4
                },
            'stone_club':{
                'name': 'stone club',
                'slots': ['main_hand', 'off_hand'],
                'atk_mod': 1,
                'min_atk': 2,
                'max_atk': 2,
                'gp': 8
                },
            'iron_mace':{
                'name': 'iron mace',
                'slots': ['main_hand', 'off_hand'],
                'atk_mod': 1,
                'min_atk': 2,
                'max_atk': 4,
                'gp': 20
                },
            'iron_axe':{
                'name': 'iron axe',
                'slots': ['main_hand', 'off_hand'],
                'atk_mod': 2,
                'min_atk': 1,
                'max_atk': 3,
                'gp': 20
                },
            'iron_sword':{
                'name': 'iron sword',
                'slots': ['main_hand', 'off_hand'],
                'atk_mod': 3,
                'min_atk': 1,
                'max_atk': 2,
                'gp': 20
                },
            'silver_mace':{
                'name': 'silver mace',
                'slots': ['main_hand', 'off_hand'],
                'atk_mod': 2,
                'min_atk': 3,
                'max_atk': 5,
                'gp': 20
                },
            'silver_axe':{
                'name': 'silver axe',
                'slots': ['main_hand', 'off_hand'],
                'atk_mod': 3,
                'min_atk': 2,
                'max_atk': 4,
                'gp': 20
                },
            'silver_sword':{
                'name': 'silver sword',
                'slots': ['main_hand', 'off_hand'],
                'atk_mod': 4,
                'min_atk': 2,
                'max_atk': 3,
                'gp': 20
                },
            },
        'off_hand':{
            'wood_shield':{
                'name': 'wood shield',
                'slots': 'off_hand',
                'armor': 1,
                'atk_mod': 0,
                'min_atk': 0,
                'max_atk': 0,
                'gp': 8
                },
            'spiked_shield':{
                'name': 'spiked shield',
                'slots': 'off_hand',
                'armor': 1,
                'atk_mod': 1,
                'min_atk': 0,
                'max_atk': 1,
                'gp': 10
                },
            'iron_shield':{
                'name': 'iron shield',
                'slots': 'off_hand',
                'armor': 2,
                'atk_mod': 0,
                'min_atk': 0,
                'max_atk': 0,
                'gp': 25
                },
            'razor_shield':{
                'name': 'razor shield',
                'slots': 'off_hand',
                'armor': 1,
                'atk_mod': 1,
                'min_atk': 0,
                'max_atk': 2,
                'gp': 30
                },
            'silver_shield':{
                'name': 'silver shield',
                'slots': 'off_hand',
                'armor': 3,
                'atk_mod': 0,
                'min_atk': 0,
                'max_atk': 0,
                'gp': 50
                }
            },
        'head':{
            'leather_helmet':{
                'name': 'leather helmet',
                'slots': 'head',
                'armor': 1,
                'gp': 10
                },
            'chain_helmet':{
                'name': 'chainmail helmet',
                'slots': 'head',
                'armor': 2,
                'gp': 20
                },
            'plate_helmet':{
                'name': 'iron plate helmet',
                'slots': 'head',
                'armor': 3,
                'gp': 40
                },
            'silver_helmet':{
                'name': 'silver plate helmet',
                'slots': 'head',
                'armor': 4,
                'gp': 80
                },
            'mithril_helmet':{
                'name': 'mithril chainmail helmet',
                'slots': 'head',
                'armor': 5,
                'gp': 120
                }
            },
        'chest':{
            'leather_tunic':{
                'name': 'leather tunic',
                'slots': 'chest',
                'armor': 1,
                'gp': 10
                },
            'chain_tunic':{
                'name': 'chainmail tunic',
                'slots': 'chest',
                'armor': 2,
                'gp': 20
                },
            'iron_tunic':{
                'name': 'iron plate tunic',
                'slots': 'chest',
                'armor': 3,
                'gp': 40
                },
            'silver_tunic':{
                'name': 'silver plate tunic',
                'slots': 'chest',
                'armor': 4,
                'gp': 80
                },
            'mithril_tunic':{
                'name': 'mithril chainmail tunic',
                'slots': 'chest',
                'armor': 5,
                'gp': 120
                },
            },
        'legs':{
            'leather_leggings':{
                'name': 'leather leggings',
                'slots': 'legs',
                'armor': 1,
                'gp': 10
                },
            'chain_leggings':{
                'name': 'chainmail leggings',
                'slots': 'legs',
                'armor': 2,
                'gp': 20
                },
            'iron_leggings':{
                'name': 'iron plate leggings',
                'slots': 'legs',
                'armor': 3,
                'gp': 40
                },
            'silver_leggings':{
                'name': 'silver plate leggings',
                'slots': 'legs',
                'armor': 4,
                'gp': 80
                },
            'mithril_leggings':{
                'name': 'mithril chainmail leggings',
                'slots': 'legs',
                'armor': 5,
                'gp': 120
                }
            },
        'item':{
            'potion':{
                'heal_pot1':{
                    'name': 'minor healing potion',
                    'heals': 2,
                    'gp': 10
                    },
                'heal_pot2':{
                    'name': 'healing potion',
                    'heals': 4,
                    'gp': 20
                    },
                'heal_pot3':{
                    'name': 'greater healing potion',
                    'heals': 8,
                    'gp': 40
                    },
                'heal_pot4':{
                    'name': 'grand healing potion',
                    'heals': 12,
                    'gp': 60
                    },
                'heal_pot5':{
                    'name': 'superior healing potion',
                    'heals': 16,
                    'gp': 90
                    },
                'heal_pot6':{
                    'name': 'supreme healing potion',
                    'heals': 20,
                    'gp': 120
                    },
                'heal_pot7':{
                    'name': 'elixir of health',
                    'heals': 25,
                    'gp': 200
                    }
                }
            }
        }

