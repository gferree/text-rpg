import land
from hero import default_vals, Hero
import actions

hero = Hero(default_vals)
actions.set_stats(hero)

debug = False

#describe starting room to hero
print(f'You start in {land.rooms[land.room_pull_pos(hero.x, hero.y)].description}')
if land.rooms[land.room_pull_pos(hero.x, hero.y)].is_shop == True:
    land.room_shop_desc(land.room_pull_pos(hero.x, hero.y))
else:
    land.room_enter_enemies(hero, land.room_pull_pos(hero.x, hero.y))

command = ""
action = ""
item = ""
item2 = ''
while command.lower() != "quit":
    #if hero is dead, end game
    if hero.hp <= 0:
        print("The Hero has died. Better luck next time.")
        break
    command = input(">")
    command_str = command.lower().split(' ')
    #command length variables
    if len(command_str) >= 1:
        action = command_str[0]
        if len(command_str) >= 2:
            if command_str[1].isdigit():
                item = int(command_str[1])
            else:
                item = command_str[1]
            if len(command_str) >= 3:
                item2 = command_str[2]
        
    #command actions
    if action == "help":
        actions.actions_list(hero)
        continue
    if action == 'move':
        if item in actions.nav:
            old_room = land.room_pull_pos(hero.x, hero.y)
            actions.move(hero, item)
            new_room = land.room_pull_pos(hero.x, hero.y)
            if new_room != old_room:
                land.room_enter_desc(land.room_pull_pos(hero.x, hero.y))
                actions.check_enemies_combat(hero)
                if land.rooms[land.room_pull_pos(hero.x, hero.y)].is_shop == True:
                    land.room_shop_desc(land.room_pull_pos(hero.x, hero.y))
                continue
            else:
                continue
        else:
            print("Which way?")
            continue
    if action == "fight":
        if len(land.rooms[land.room_pull_pos(hero.x, hero.y)].enemies) > 0:
            actions.check_enemies_combat(hero)
            continue
        else:
            print("There's nothing to fight.")
            continue
    if action == 'search':
        actions.search_room(hero)
        continue
    if action == 'take':
        if item != '':
            actions.pick_up(hero, item)
            continue
        else:
            print("Take what?")
            continue
    if action == 'drop':
        if item != '':
            actions.drop(hero, item)
            continue
        else:
            print("Drop what?")
    if action == 'equip':
        if item != '':
            actions.equip(hero, item, item2)
            continue
        else:
            print("Equip what?")
            continue
    if action == 'unequip':
        if item != '':
            actions.unequip(hero, item)
            continue
        else:
            print("Unequip what?")
            continue
    if action == 'use':
        if item != '':
            actions.use(hero, item)
            continue
        else:
            print("Use what?")
            continue
    if action == 'inventory' or action == 'inv':
        actions.inventory(hero)
        continue
    if action == 'shop':
        if land.rooms[land.room_pull_pos(hero.x, hero.y)].is_shop == True:
            land.room_shop_desc(land.room_pull_pos(hero.x, hero.y))
            continue
        else:
            print("This room isn't a shop.")
            continue
    if action == 'buy':
        if land.rooms[land.room_pull_pos(hero.x, hero.y)].is_shop == True:
            actions.buy(hero, item, land.room_pull_pos(hero.x, hero.y))
            continue
        else:
            print("This room isn't a shop. You can't buy anything here.")
            continue
    if action == 'sell':
        if land.rooms[land.room_pull_pos(hero.x, hero.y)].is_shop == True:
            actions.sell(hero, item)
            continue
        else:
            print("This room isn't a shop. You can't sell anything here.")
            continue
    if action == 'map':
        actions.print_map()
        continue

        
        
    #debug actions
    if action == 'debug' and debug == False:
        debug = True
        print('Debug On')
        continue
    if action == 'debug' and debug == True:
        debug = False
        print('Debug Off')
        continue
    if debug == True:
        if action == 'hp':
            print(f'{hero.hp}')
            continue
        if action == 'weapon':
            print(f'{hero.weapon}')
            continue
        if action == 'tp':
            hero.x = int(item)
            hero.y = int(item2)
            continue
        if action == 'give':
            actions.give(hero, item)
            print(f"You cheated in {str(item)} gold for yourself.")
            continue
    
    if action == "quit":
        break
    else:
        print("I do not know what you mean.")
    