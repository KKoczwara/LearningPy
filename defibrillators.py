# https://www.codingame.com/training/easy/defibrillators

import sys
import math

def convert_to_float(word):
    return float(word.replace(',' , '.'))

def distance_calculator(user_lon, user_lat, short_defib_list, i, RADIUS_OF_EARTH):
    x = (user_lon - short_defib_list[i][1]) * math.cos((short_defib_list[i][2] + user_lat)/2)
    y = (user_lat - short_defib_list[i][2])
    return math.hypot(x, y) * RADIUS_OF_EARTH

def main():
    user_lon = input()
    user_lon = convert_to_float(user_lon)
    user_lat = input()
    user_lat = convert_to_float(user_lat)
    n = int(input())
    defib_list = []
    RADIUS_OF_EARTH = 6371

    for i in range(n):
        defib = input()
        defib_list.append(defib.split(';'))

    comma_to_dot = lambda data: (data[1], convert_to_float(data[4]), convert_to_float(data[5]))
    short_defib_list = list(map(comma_to_dot, defib_list))

    shortest_distance = distance_calculator(user_lon, user_lat, short_defib_list, 0, RADIUS_OF_EARTH)
    shortest_distance_index = 0

    for i in range(n):
        d = distance_calculator(user_lon, user_lat, short_defib_list, i, RADIUS_OF_EARTH)
        if shortest_distance > d:
            shortest_distance = d
            shortest_distance_index = i

    print(short_defib_list[shortest_distance_index][0])
       
#main()
a = ('x', 'y')

a[0] = 'c'
