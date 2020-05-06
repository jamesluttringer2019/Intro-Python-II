import textwrap
import random
from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Declare items

items = {'map': Item('map', 'A map of the land.'), 
         'knife': Item('knife', 'A handy tool or weapon to have.'),
         'torch': Item('torch', 'Helpful to see at night or start fires.'),
         'rope': Item('rope', 'Ropes are useful.'),
         'chair': Item('chair', "It's a chair.")}

# Randomly spawn items in rooms
for x in room.values():
    for i in random.sample(items.keys(), random.randint(0,3)):
        x.items.append(items[i])
#
# Main
#
print('Welcome! Please enter a name for your player.')
# Make a new player object that is currently in the 'outside' room.
player = Player(input(), room['outside'])
print(f'''Alright {player.name}, let's get to it!\n\n
    ****************************************************\n
        To move, enter a direction (n, e, s, w)\n
        To pick up an item, type "get" and the item name\n
        To drop an item, type "drop" and the item name\n
        To view your inventory, type "i"\n
        Enter q to quit\n
    ****************************************************\n
''')
command = ''
moved = True
while command != 'q':
    if moved:
        print(f'Current Location: {player.curr_room.name}')
        print(f'*{textwrap.fill(player.curr_room.desc, 60)}*\n')
        print('In this room, there is...')
        for x in player.curr_room.items:
            print(f'A {x.name}: {x.desc}')
        print('\n')
    moved = False
    command = input()
    print('\n')
    if command in ['n', 's', 'e', 'w']:
        try:
            player.curr_room = getattr(player.curr_room, f'{command}_to')
            moved = True
        except:
            print(f'There is no room {command}, try again!')
            
    elif command == 'i':
        print('Inventory:')
        for i in player.inv:
            print(f'{i.name}: {i.desc}')

    elif command.split()[0] == 'get':
        try:
            item = items[command.split()[1]]
            player.curr_room.items.remove(item)
            player.inv.append(item)
            item.on_take()
        except:
            print('Object not found in room')
            
    elif command.split()[0] == 'drop':
        try:
            item = items[command.split()[1]]
            player.inv.remove(item)
            player.curr_room.items.append(item)
            item.on_drop()
        except:
            print('Object not in inventory')
            
    else:
        print('Command not found, try again')
        
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
