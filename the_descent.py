# https://www.codingame.com/training/easy/the-descent

import sys
import math

while True:
    highest_mountain_height = 0
    highest_mountain_index = 0
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        if mountain_h > highest_mountain_height:
            highest_mountain_height = mountain_h
            highest_mountain_index = i

    print(highest_mountain_index)
