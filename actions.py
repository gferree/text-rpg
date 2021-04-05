from land import land_width, rooms, room_pull_pos, room_enter_enemies, room_shop_desc
from loot import find_loot_dict, loot_table
from random import randint, choice, randrange


#player commands
nav = ['north', 'south', 'east', 'west']
def move(hero, direction):
    rooms[room_pull_pos(hero.x, hero.y)].current_marker = rooms[room_pull_pos(hero.x, hero.y)].default_marker
    if direction == 'north':
        if rooms[room_pull_pos(hero.x, hero.y)].halls[0] == True:
            hero.y += 1
        else:
            rooms[room_pull_pos(hero.x, hero.y)].current_marker = '*'
            return print('You cannot go that way.')
    if direction == 'south':
        if rooms[room_pull_pos(hero.x, hero.y)].halls[1] == True:
            hero.y -= 1
        else:
            rooms[room_pull_pos(hero.x, hero.y)].current_marker = '*'
            return print('You cannot go that way.')
    if direction == 'east':
        if rooms[room_pull_pos(hero.x, hero.y)].halls[2] == True:
            hero.x += 1
        else:
            rooms[room_pull_pos(hero.x, hero.y)].current_marker = '*'
            return print('You cannot go that way.')
    if direction == 'west':
        if rooms[room_pull_pos(hero.x, hero.y)].halls[3] == True:
            hero.x -= 1
        else:
            rooms[room_pull_pos(hero.x, hero.y)].current_marker = '*'
            return print('You cannot go that way.')
    rooms[room_pull_pos(hero.x, hero.y)].current_marker = '*'
    print_map()
    return print(f'You go {direction}.')
        
def search_room(hero):
    if hero.near_enemies == True:
        return print("You can't search for loot, there are enemies in this room. Fight and defeat them to search for loot")
    else:
        if len(rooms[room_pull_pos(hero.x, hero.y)].loot) > 0:
            print("You've found some loot!")
            loot_number = 0
            for i in rooms[room_pull_pos(hero.x, hero.y)].loot:
                loot_item = find_loot_dict(i)
                loot_number += 1
                print(f'[{loot_number}]: ' + loot_item['name'].title())
        else:
            return print("There's no loot here.")
            
def pick_up(hero, item):
    room_ltable = rooms[room_pull_pos(hero.x, hero.y)].loot
    if isinstance(item, int) == False:
        return print("Pick a number from the room's loot list.")
    if int(item) > len(room_ltable) or int(item) < 1:
        return print("Pick a number from the room's loot list.")
    if len(room_ltable) == 0:
        return print("There's no loot to get in this room.")
    if all(list(hero.inventory.values())) == True:
        return print("Inventory is full. Drop items to make space.")
    taken_item = find_loot_dict(room_ltable[item - 1])
    for i in list(hero.inventory.keys()):
        if hero.inventory[i] == '':
            hero.inventory[i] = room_ltable[item - 1]
            room_ltable.remove(room_ltable[item - 1]) 
            return print('You took the ' + taken_item['name'].title()+ '.')

def drop(hero, item):
    if isinstance(item, int) == False:
        return print("Pick a number from your inventory list.")
    if int(item) > len(list(hero.inventory.values())) or int(item) < 1:
        return print("That's not a valid number from your inventory list.")
    if any(list(hero.inventory.values())) != True:
        return print("You have nothing to drop.")
    #first add item to room the hero is in, then remove from hero's inventory
    rooms[room_pull_pos(hero.x, hero.y)].loot.append(hero.inventory[f'slot{item}'])
    drop_item = find_loot_dict(hero.inventory[f'slot{item}'])
    print('You dropped the ' + drop_item['name'].title() + '.')
    hero.inventory[f'slot{item}'] = ''
    
def buy(hero, item, index):
    if isinstance(item, int) == False:
        return print("Pick a number from the shop list.")
    if int(item) > len(list(rooms[index].shop_items)) or int(item) < 1:
        return print("That's not a valid number from the shop list.")
    if any(list(rooms[index].shop_items)) != True:
        return print("This shop's sold out of items.")
    if rooms[index].shop_items[item-1] != '':
        item_buy = find_loot_dict(rooms[index].shop_items[item-1])
        if hero.gp >= item_buy['gp']:
            if all(list(hero.inventory.values())) == True:
                return print("Inventory is full. Make space in your inventory before buying something.")
            else:
                for i in list(hero.inventory.keys()):
                    if hero.inventory[i] == '':
                        hero.inventory[i] = rooms[index].shop_items[item-1]
                        hero.gp -= item_buy['gp']
                        rooms[index].shop_items[item-1] = ''
                        return print('You bought the ' + item_buy['name'].title() + ' for ' + str(item_buy['gp']) + ' Gold.')

        else:
            return print("You don't have enough money to buy that.")
    else:
        return print("There's nothing to buy in that slot.")

def sell(hero, item):
    if isinstance(item, int) == False:
        return print("Pick a number from your inventory list.")
    if int(item) > len(list(hero.inventory.values())) or int(item) < 1:
        return print("That's not a valid number from your inventory list.")
    if any(list(hero.inventory.values())) != True:
        return print("You have nothing to sell.")
    sell_item = find_loot_dict(hero.inventory[f'slot{item}'])
    sell_price = sell_item['gp']
    hero.gp += int(sell_price / 2)
    hero.inventory[f'slot{item}'] = ''
    print('You sold the ' + sell_item['name'].title() + ' for ' + str(int(sell_price/2)) + ' Gold.')

def inventory(hero):
    print(f'''HP: {hero.hp}; AC: {hero.ac}; Gold: {hero.gp}
Attack Mod: {str(hero.atk_mod)} ; Min DMG: {str(hero.min_atk)} ; Max DMG: {str(hero.max_atk)}
Main_Hand: {hero.main_hand.title()}; Off_Hand: {hero.off_hand.title()}; Helmet: {hero.head.title()}; Tunic: {hero.chest.title()}; Legs: {hero.legs.title()}''')
    inv_number = 0
    for i in hero.inventory.keys():
        inv_number +=1
        inv_item = find_loot_dict(hero.inventory[i])
        if hero.inventory[i] == '':
            print(f'[{inv_number}]: ')
            continue
        if rooms[room_pull_pos(hero.x, hero.y)].is_shop == False:
            print(f'[{inv_number}]: ' + inv_item['name'].title())
        else:
            print(f'[{inv_number}]: ' + inv_item['name'].title() + ' - ' + str(inv_item['gp']) + ' GP')
        
#sets hero stats based on gear that is equipped
def set_stats(hero):
    hero.atk_mod = 0
    hero.min_atk = 0
    hero.max_atk = 0
    hero.ac = 10
    if hero.main_hand != '':
        hero.atk_mod += find_loot_dict(hero.main_hand)['atk_mod']
        hero.min_atk += find_loot_dict(hero.main_hand)['min_atk']
        hero.max_atk += find_loot_dict(hero.main_hand)['max_atk']
    if hero.off_hand != '':
        hero.atk_mod += find_loot_dict(hero.off_hand)['atk_mod']
        hero.min_atk += find_loot_dict(hero.off_hand)['min_atk']
        hero.max_atk += find_loot_dict(hero.off_hand)['max_atk']  
        if 'armor' in list(find_loot_dict(hero.off_hand).keys()):
            hero.ac += find_loot_dict(hero.off_hand)['armor']
    if hero.head != '':
        hero.ac += find_loot_dict(hero.head)['armor']
    if hero.chest != '':
        hero.ac += find_loot_dict(hero.chest)['armor']
    if hero.legs != '':
        hero.ac += find_loot_dict(hero.legs)['armor']
    

def equip(hero, item, item2=''):
    if isinstance(item, int) == False:
        return print("Pick a number from your inventory list.")
    if int(item) > len(list(hero.inventory.values())) or int(item) < 1:
        return print("That's not a valid number from your inventory list.")
    if any(list(hero.inventory.values())) != True:
        return print("You have no items in your inventory to equip.")
    equip_item = find_loot_dict(hero.inventory[f'slot{item}'])
    if equip_item not in list(loot_table['item'].values()):
        if equip_item in list(loot_table['main_hand'].values()):
            if item2 == 'main_hand':
                if hero.main_hand == '':
                    hero.main_hand = hero.inventory[f'slot{item}']
                    hero.inventory[f'slot{item}'] = ''
                    set_stats(hero)
                    return print("You've equipped the " + equip_item['name'].title() + ' in your main hand.')
                else:
                    return print("You already have something in your main hand. Unequip it first.")
            if item2 == 'off_hand':
                if hero.off_hand == '':
                    hero.off_hand = hero.inventory[f'slot{item}']
                    hero.inventory[f'slot{item}'] = ''
                    set_stats(hero)
                    return print("You've equipped the " + equip_item['name'].title() + ' in your off hand.')
                else:
                    return print("You already have something in your off hand. Unequip it first.")         
            if item2 == '':
                return print("Which slot do you want to equip that to? Main_hand or Off_hand")
            else:
                return print("You can't equip a main hand item to that slot. Pick 'main' or 'off'.")
        equip_slot = equip_item['slots']
        if getattr(hero, equip_slot) == '':
            setattr(hero, equip_slot, hero.inventory[f'slot{item}'])
            hero.inventory[f'slot{item}'] = ''
            set_stats(hero)
            return print("You've equipped the " + equip_item['name'].title() + '.')
        else:
            return print('You have something already equipped in that slot. Unequip it first.')
    
def unequip(hero, item):
    slots = ['main_hand', 'off_hand', 'head', 'chest', 'legs']
    if item not in slots:
        return print('What do you want to unequip?')
    if getattr(hero, item) == '':
        return print('You have nothing in that slot to unequip.')
    unequipped_item = find_loot_dict(getattr(hero, item))
    if all(list(hero.inventory.values())) == True:
        room = rooms[room_pull_pos(hero.x, hero.y)]
        room.loot.append(getattr(hero, item))
        setattr(hero, item, '')
        return print('Your inventory is full. You have unequipped your ' + unequipped_item['name'].title() + ' and dropped it on the ground.')
    for i in list(hero.inventory.keys()):
        if hero.inventory[i] == '':
            hero.inventory[i] = getattr(hero, item)
            setattr(hero, item, '')
            set_stats(hero)
            return print('You have unequipped your ' + unequipped_item['name'].title() + ' and put it in your inventory.')
        
def use(hero, item):
    if isinstance(item, int) == False:
        return print("Pick a number from your inventory list.")
    if int(item) > len(list(hero.inventory.values())) or int(item) < 1:
        return print("That's not a valid number from your inventory list.")
    if any(list(hero.inventory.values())) != True:
        return print("You have no items in your inventory to use.")
    use_item = hero.inventory[f'slot{item}']
    if use_item in list(loot_table['item']['potion'].keys()):
        heal_amt = find_loot_dict(use_item)['heals']
        hero.hp += heal_amt
        print('You used the ' + find_loot_dict(use_item)['name'].title() + ' and healed yourself for ' + str(heal_amt) + ' health.')
        hero.inventory[f'slot{item}'] = ''
        return
    else:
        return print("That's not an item you can use.")
    
def check_enemies_combat(hero):
    if len(rooms[room_pull_pos(hero.x, hero.y)].enemies) > 0:
        hero.near_enemies = True
        combat(hero, rooms[room_pull_pos(hero.x, hero.y)].enemies)
    else:
        hero.near_enemies = False
    
def attack(attacker, defender):
    attack_roll = randint(1, 20) + attacker.atk_mod
    if attack_roll >= defender.ac:
        damage = randint(attacker.min_atk, attacker.max_atk)
        defender.hp -= damage
        print(f'The {attacker.name.title()} attacks the {defender.name.title()} and deals {damage} damage.')
    else:
        return print(f'The {attacker.name.title()} attacks the {defender.name.title()} and misses.')
    

def combat(hero, enemies):
    hero.in_combat = True
    combat_command = ''
    combat_action = ''
    combat_item = ''
    valid_actions = ['attack', 'inv', 'inventory', 'use', 'run', 'help']
    print('''
You've entered combat. You can attack, check your inventory, use an item, or run from the fight.''')
    while hero.in_combat == True:
        print(f'Hero Stats - HP: {hero.hp}; AC: {hero.ac}; Gold: {hero.gp}')
        room_enter_enemies(hero, room_pull_pos(hero.x, hero.y))
        combat_command = input(">")
        comb_com_str = combat_command.lower().split(' ')
        if len(comb_com_str) >= 1:
            combat_action = comb_com_str[0]
        if len(comb_com_str) >= 2:
            if comb_com_str[1].isdigit():
                combat_item = int(comb_com_str[1])
        if combat_action not in valid_actions:
            print("You can't do that right now. You can attack, check your inventory, use an item, or run from the fight.")
            continue
        if combat_action == 'run':
            print("You've ran away from the fight. You can move to another room or return to the fight.")
            hero.in_combat = False
            return
        if combat_action == 'inventory' or combat_action == 'inv':
            inventory(hero)
            continue
        if combat_action == 'attack':
            if isinstance(combat_item, int) == False:
                print("Pick a number from the enemy list.")
                continue
            if int(combat_item) > len(enemies) or int(combat_item) < 1:
                print("That's not a valid number the enemy list.")
                continue
            attack(hero, enemies[combat_item-1])
            for enemy in enemies:
                if enemy.hp <= 0:
                    print(f'The {enemy.name.title()} has died.')\
                    #give dropped gold to hero
                    enemy_gold = randrange(enemy.min_gold, enemy.max_gold)
                    print(f'The Hero got {enemy_gold} gold from the {enemy.name}.')
                    hero.gp += enemy_gold
                    #add loot to the room then remove the dead enemy
                    if randrange(100) < enemy.loot_chance:
                        print(f"The {enemy.name.title()} dropped some loot!")
                        loot_type = choice(list(loot_table.keys()))
                        if loot_type == 'item':
                             loot_type = choice(list(loot_table['item'].keys()))
                             rooms[room_pull_pos(hero.x, hero.y)].loot.append(choice(list(loot_table['item'][loot_type].keys())))
                        else:
                            rooms[room_pull_pos(hero.x, hero.y)].loot.append(choice(list(loot_table[loot_type].keys())))
                    enemies.remove(enemy)
            for enemy in enemies:        
                attack(enemy, hero)
            if hero.hp <= 0:
                hero.in_combat = False
                continue
            if len(enemies) == 0:
                print("You've defeated all the enemies in this room and can now search for loot.")
                hero.in_combat = False
                hero.near_enemies = False
                continue
        if combat_action == 'use':
            if isinstance(combat_item, int) and hero.inventory[f'slot{combat_item}'] in list(loot_table['item']['potion'].keys()):
                use(hero, combat_item)
                for enemy in enemies:
                    attack(enemy, hero)
            else:
                use(hero, combat_item)
            if hero.hp <= 0:
                hero.in_combat = False
                continue
        if combat_action == 'help':
            actions_list(hero)
            continue
        print('''
You're in combat. You can attack, check your inventory, use an item, or run from the fight.''')

    

def actions_list(hero):
    if rooms[room_pull_pos(hero.x, hero.y)].is_shop == True:
        return print("""Actions:
SHOP - shows items available to buy in a shop
BUY [shop slot #] - attempt to buy the item in that slot in the shop
SELL [inventory slot #] - sells the item in that slot in your inventory for half its worth. All sales are final
INV or INVENTORY - shows your inventory with gold value for each item and your stats
MOVE [north, south, east, west] - leave the ship and move in the direction you specify if that path is open
""")
    if hero.in_combat == True:
        return print("""Actions:
ATTACK [enemy #] - attempt to attack the enemy you specify in the room's enemy list then each enemy attempts to attack you
INV or INVENTORY - shows your inventory and your stats
USE [inventory slot #] - use the item in that slot of your inventory if its valid then each enemy attempts to attack you
RUN - you leave combat with the enemies but you stay in the same room. Enemies cannot attack you unless you choose to FIGHT them again
""")
    else:
        return print("""Actions:
MAP - shows a map of the dungeon. '*' is the hero's position and arrows such as '>' are deadends
INV or INVENTORY - shows your inventory with gold value for each item and your stats
MOVE [north, south, east, west] - moves you in the direction you specify if that path is open
SEARCH - returns a list of loot in the room. You can't search for loot while enemies are nearby
TAKE [search list #] - takes the item you specify if there's room in your inventory. Cannot do this while enemies are nearby
DROP [inventory slot #] -  removes the item from your inventory and drops it in the room as loot
EQUIP [inventory slot #] [main_hand, off_hand] - equips the item you specify from your inventory. You must specify main_hand or off_hand if it is a main hand item
UNEQUIP [main_hand, off_hand, head, chest, legs] - unequips the selected slot and either puts it in your inventory or drops it in the room if inventory is full
USE [inventory slot #] - uses the item in the selected inventory slot if its valid
FIGHT - you enter combat with enemies if there are enemies in your current room
""")
    
def print_map():
    for i in range(land_width):
        map_row = range(land_width - (1 + i),len(rooms) - i,land_width)
        for i in map_row:
            print(rooms[i].current_marker, end = " ")
            if map_row.index(i) / (land_width - 1) == 1:
                print()

#debug commands
def give(hero, gold):
    hero.gp += int(gold)        
        
        
        
        
        
        