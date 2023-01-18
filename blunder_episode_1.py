# https://www.codingame.com/training/medium/blunder-episode-1

import sys
import math

l, c = [int(i) for i in input().split()]
map_list = []

for i in range(l):
    row = list(input())
    map_list.append(row)

def find_object(list, symbol):
    for i, x in enumerate(list):
        if symbol in x:
            return(i, x.index(symbol))

def next_location(y, x, index_of_direction):
    if index_of_direction == 0:
        return (y + 1, x)
    elif index_of_direction == 1:
        return (y, x + 1)
    elif index_of_direction == 2:
        return (y - 1, x)
    elif index_of_direction == 3:
        return (y, x - 1)

def obstacles(map_list, y, x, beer):
    if map_list[y][x] == '#':
        return True
    elif map_list[y][x] == 'X' and beer == False:
        return True
    else:
        return False

def teleporter(list, symbol, current_position):
    teleporter_locations = []
    
    for i, x in enumerate(list):
        if symbol in x:
            teleporter_locations.append([i, x.index(symbol)])

    if current_position == tuple(teleporter_locations[0]):
        return teleporter_locations[1]
    else:
        return teleporter_locations[0]

def print_result(list):
    for i in list:
        print(i)

def main():
    priority_list = ["SOUTH", "EAST", "NORTH", "WEST"]
    priority = True
    direction_list = []
    states = set()

    not_finish = True
    index_of_direction = 0
    beer = False

    current_position = find_object(map_list, '@')
    finish_position = find_object(map_list, '$')
    
    def check_location():
        nonlocal not_finish
        nonlocal index_of_direction
        nonlocal beer
        nonlocal current_position
        nonlocal priority
        map_item = map_list[current_position[0]][current_position[1]]

        if (current_position, index_of_direction, beer, priority) in states:
            not_finish = False
            direction_list.clear()
            print("LOOP")
        elif current_position == finish_position:
            not_finish = False
        elif map_item == 'S':
            index_of_direction = 0
        elif map_item == 'E':
            index_of_direction = 1
        elif map_item == 'N':
            index_of_direction = 2
        elif map_item == 'W':
            index_of_direction = 3
        elif map_item == 'B':
            beer = not beer
        elif map_item == 'T':
            current_position = tuple(teleporter(map_list, 'T', current_position))
        elif map_item == 'I':
            priority = not priority

    while not_finish:
        
        potential_next_position = next_location(current_position[0], current_position[1], index_of_direction)

        if map_list[potential_next_position[0]][potential_next_position[1]] == 'X' and beer:
            map_list[potential_next_position[0]][potential_next_position[1]] = ' '
            states = set()

        number_of_tries = 1
        while obstacles(map_list, potential_next_position[0], potential_next_position[1], beer):
            if priority:
                index_of_direction = number_of_tries - 1
                potential_next_position = next_location(current_position[0], current_position[1], index_of_direction)
                number_of_tries += 1
            else:
                index_of_direction = 4 - number_of_tries
                potential_next_position = next_location(current_position[0], current_position[1], index_of_direction)
                number_of_tries += 1

        states.add((current_position, index_of_direction, beer, priority))
        current_position = potential_next_position
        direction_list.append(priority_list[index_of_direction])
        
        check_location()
       
    print_result(direction_list)

main()