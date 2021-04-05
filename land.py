#map variables
land_size = 5
land_width = (land_size * 2) + 1

#room variables
room_description = [
    'a dimly lit barracks with several bunk beds lined up throughout. The stone walls are cracked and crumbling in spots.',
    'an empty room with several torches on the walls. Scattered bones lay across the floor and cobwebs are stuck to the walls.',
    'a corridor with a precarious bridge. A thin stone bridge separates you from the other sides of the room. Lava lays hundreds of feet below.',
    'an ominous mead hall. A weathered long table and a couple chairs sit by the soot filled firepit.',
    'a run-down armory. Axes, swords, tunics, and shields. They lay scattered about or hung on armor stands, nearly all either rusted or decayed from the passage of time.',
    'an abandoned alchemist workshop. Test tubes stand on a table with a torn up notebook. A cauldron bubbles with some unknown, glowing purple liquid. A shelf nearby houses a scant few ingredients.',
    'a simple hallway. A tattered red rug covers the length of the hall and a dull, iron brazier hangs from the ceiling, its last flames smoldering within.',
    'a small, cragly cavern. The faint sound of dripping water can be heard from the walls. A skeleton lays atop one of the rocks, clutching a torn and bloodied wood shield.',
    'a soot-stained throne room. The once decadent hall is covered in black ash. Charred skeletons can be found around the room, one notably sitting upon the thrown with a blackened crown',
    'a crypt. Carved pockets holding the final resting place of unfortunate souls line the walls. The rattling of bones can barely be heard nearby... or was it trick of the mind?',
    'a dusty library. Several bookshelves line the walls, but there are no torches lit to illuminate the knowledge they hold. There are several tables with cracked books and crumpled papers.',
    'an eerie alcove dug from the walls of the dungeon. It leads to a small cave with a paltry pool of water. A statue of a long-forgotten diety stands in the pool with vines crawling up its body.',
    'the remains of a bload-soaked battle. The fetid stench of rotting corpses fill the room and the bodies of all sorts of creatures can be seen laying in viscera.',
    'the shrine of an unknown entity. A depiction of a silhouette shrouded in blue and black robes is painted on the back wall and its skull has tendrils forming out of it. Someone or something has taken special care to maintain this shrine.',
    'the chambers of a long dead resident. A simple cot sits in the corner, a bedside dresser sits next to it, and a chest rests at the foot of the cot. The lock on the chest seems to be undone.',
    'a room with several jail cells. They seem vacant, but one of the iron-bar doors creaks as it hangs open in the hallway.',
    "the makeshift home of some unruly beast. At least that's what it seems from the bloody rambling scrawled upon the walls and the torn up furniture. The walls are covered in a language you don't understand.",
    'a pitch black room. Lighting your torch reveals a bare room with only a single chest as furniture.'
    ]

room_loot_chance = 70
shop_chance = 15

from random import choice, getrandbits, randrange, randint

#Pull room index based off position
def room_pull_pos(x, y):
    for index in range(len(rooms)):
        if rooms[index].x == x and rooms[index].y == y:
            return index

#describe room the hero just entered
def room_enter_desc(index):
    print(f'You enter {rooms[index].description}')
    
def room_enter_enemies(hero, index):
    print(f'There are {len(rooms[index].enemies)} enemies in this room.')
    enemy_number = 0
    for i in rooms[index].enemies:
        enemy_number += 1
        print(f'[{enemy_number}]: ' + getattr(rooms[index].enemies[enemy_number-1], 'name').title() + ' - HP: ' + str(getattr(rooms[index].enemies[enemy_number-1], 'hp')) + '/' + str(getattr(rooms[index].enemies[enemy_number-1], 'max_hp')))

##establishes true/false in .halls to call back to for each map generation step 
def room_set_halls(i):
    rooms[i].halls = [bool(rooms[i].n_hall), 
                      bool(rooms[i].s_hall), 
                      bool(rooms[i].e_hall), 
                      bool(rooms[i].w_hall)]

class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

        self.n_hall = bool(getrandbits(1))
        self.s_hall = bool(getrandbits(1))
        self.e_hall = bool(getrandbits(1))
        self.w_hall = bool(getrandbits(1))
        self.halls = [self.n_hall, self.s_hall, self.e_hall, self.w_hall]
        self.default_marker = ' '
        self.current_marker = ' '
        self.is_shop = False
        self.shop_item1 = ''
        self.shop_item2 = ''
        self.shop_item3 = ''
        self.shop_items = [self.shop_item1, self.shop_item2, self.shop_item3]
        self.description = ''
        self.loot = []
        self.enemies = []
    
#creation of rooms
rooms = []
for x in range(-land_size, (land_size + 1)):
    for y in range(-land_size, (land_size + 1)):
        rooms.append(Room(x, y))  
#random generation of room hallways
for i in range(len(rooms)):
    
    #bases west and south facing hall condition on east and north facing hall conditions 
    #of adjacent rooms
    if i > 0:
        if rooms[i-1].n_hall == True:
            rooms[i].s_hall = True
        else:
            rooms[i].s_hall = False 
        if i >= land_width:
            if rooms[i-land_width].e_hall == True:
                rooms[i].w_hall = True
            else:
                rooms[i].w_hall = False
                
    #set room at 0, 0 to have all four hallways            
    if i == room_pull_pos(0, 0):
        rooms[i].n_hall = True
        rooms[i].s_hall = True
        rooms[i].e_hall = True
        rooms[i].w_hall = True
    if i == room_pull_pos(0, 1):
        rooms[i].s_hall = True
    if i == room_pull_pos(0, -1):
        rooms[i].n_hall = True
    if i == room_pull_pos(1, 0):
        rooms[i].w_hall = True
    if i == room_pull_pos(-1, 0):
        rooms[i].e_hall = True
    
    #sets outside rooms to have walls along perimeter
    if rooms[i].y == land_size:
        rooms[i].n_hall = False
    if rooms[i].y == -land_size:
        rooms[i].s_hall = False
    if rooms[i].x == land_size:
        rooms[i].e_hall = False
    if rooms[i].x == -land_size:
        rooms[i].w_hall = False        
        
    room_set_halls(i)
   
#remove inaccessible double rooms
for i in range(len(rooms)):
    if rooms[i].halls.count(True) == 1:
        if rooms[i].n_hall == True:
            if rooms[i+1].halls.count(True) == 1 and rooms[i+1].s_hall == True:
                rooms[i].n_hall = False
                rooms[i+1].s_hall = False
        if rooms[i].e_hall == True:
            if rooms[i+land_width].halls.count(True) == 1 and rooms[i + land_width].w_hall == True:
                rooms[i].e_hall = False
                rooms[i+land_width].w_hall = False
    
    room_set_halls(i)

#random chance to take remaining deadends and turn them into an intersection
for i in range(len(rooms)):
    remove_blocked_percent = 60
    if rooms[i].halls.count(True) > 0:
        if randrange(100) < remove_blocked_percent:
            new_hall = choice(['north', 'east'])
            if new_hall == 'north' and rooms[i].y < land_size and rooms[i+1].halls.count(True) > 0:
                        rooms[i].n_hall = True
                        rooms[i+1].s_hall = True
            if new_hall == 'east' and rooms[i].x < land_size and rooms[i+land_width].halls.count(True) > 0:
                        rooms[i].e_hall = True
                        rooms[i+land_width].w_hall = True
    
    room_set_halls(i)        
                
    #set map markers
    if True in rooms[i].halls:
        rooms[i].default_marker = '☐'
    if rooms[i].halls[0] == True:
        rooms[i].default_marker = '∨'
    if rooms[i].halls[1] == True:
        rooms[i].default_marker = '∧'
    if rooms[i].halls[2] == True:
        rooms[i].default_marker = '<'
    if rooms[i].halls[3] == True:
        rooms[i].default_marker = '>'
    if rooms[i].halls[0] == True and rooms[i].halls[1] == True:
        rooms[i].default_marker = '┃'
    if rooms[i].halls[0] == True and rooms[i].halls[2] == True:
        rooms[i].default_marker = '┗'
    if rooms[i].halls[0] == True and rooms[i].halls[3] == True:
        rooms[i].default_marker = '┛'
    if rooms[i].halls[1] == True and rooms[i].halls[2] == True:
        rooms[i].default_marker = '┏'
    if rooms[i].halls[1] == True and rooms[i].halls[3] == True:
        rooms[i].default_marker = '┓'
    if rooms[i].halls[2] == True and rooms[i].halls[3] == True:
        rooms[i].default_marker = '━'
    if rooms[i].halls[0] == True and rooms[i].halls[1] == True and rooms[i].halls[2] == True:
        rooms[i].default_marker = '┣'
    if rooms[i].halls[0] == True and rooms[i].halls[2] == True and rooms[i].halls[3] == True:
        rooms[i].default_marker = '┻'
    if rooms[i].halls[0] == True and rooms[i].halls[1] == True and rooms[i].halls[3] == True:
        rooms[i].default_marker = '┫'
    if rooms[i].halls[1] == True and rooms[i].halls[2] == True and rooms[i].halls[3] == True:
        rooms[i].default_marker = '┳'
    if all(rooms[i].halls):
        rooms[i].default_marker = '╋'
    if not any(rooms[i].halls):
        rooms[i].default_marker = ' '
    
    rooms[i].current_marker = rooms[i].default_marker

#set hero map marker
rooms[room_pull_pos(0, 0)].current_marker = '*'
    
#adds accessible rooms to valid_room list
valid_rooms = []
for i in range(len(rooms)):
    if rooms[i].halls.count(True) > 0:
        valid_rooms.append(Room(rooms[i].x, rooms[i].y))
        
from loot import loot_table, find_loot_dict
from enemy import enemy_list, Enemy, find_enemy_dict

def room_shop_desc(index):
        print("Here's what's for sale in this shop. You can buy the listed items or sell items in your inventory for half their worth.")
        shop_number = 0
        for item in rooms[index].shop_items:
            shop_number +=1
            shop_item = find_loot_dict(item)
            if item == '':
                print(f'[{shop_number}]: ')
                continue
            print(f'[{shop_number}]: ' + shop_item['name'].title() + ' - ' + str(shop_item['gp']) + ' Gold')

# generates room attributes (loot, enemies, descriptions, etc.) in rooms list
# if the room is in valid_rooms list
for i in range(len(valid_rooms)):
    gen = room_pull_pos(valid_rooms[i].x, valid_rooms[i].y)
    if randrange(100) < shop_chance:
        rooms[gen].is_shop = True
        rooms[gen].description = 'a shop!'
        for i in range(len(rooms[gen].shop_items)):
            loot_type = choice(list(loot_table.keys()))
            if loot_type == 'item':
                loot_type = choice(list(loot_table['item'].keys()))
                rooms[gen].shop_items[i-1] = choice(list(loot_table['item'][loot_type].keys()))
            else:
                rooms[gen].shop_items[i-1] = choice(list(loot_table[loot_type].keys()))
        
        
    else:
        rooms[gen].description = choice(room_description)
        #loot generation in rooms
        if randrange(100) < room_loot_chance:
            loot_type = choice(list(loot_table.keys()))
            if loot_type == 'item':
                loot_type = choice(list(loot_table['item'].keys()))
                rooms[gen].loot.append(choice(list(loot_table['item'][loot_type].keys())))
            else:
                rooms[gen].loot.append(choice(list(loot_table[loot_type].keys())))
            
        rooms[gen].enemies = []
        if rooms[gen].x == 0 and rooms[gen].y == 0:
            enemy_amt =0
        else:
            enemy_amt = randint(0,3)
        for i in range(enemy_amt):
            enemy_type = choice(list(enemy_list.keys()))
            enemy = Enemy(find_enemy_dict(enemy_type))
            rooms[gen].enemies.append(enemy)
    
#clear valid_rooms since room generation is done and we do not need the copied Room x and y's
valid_rooms.clear()